#!/usr/bin/env python3
"""Build PQI master + 50 blinded source-order batches from the 12 recovered Drive CSVs.

Usage: python review_audit/tools/build_master_from_recovered.py
Uses only Python standard library. Never turns old AI labels into validated review decisions.
"""
import csv
from pathlib import Path
from collections import Counter,defaultdict

ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/"source"/"original_screening"
OUTPUT=ROOT/"source"
BLIND=ROOT/"batches"

def write_csv(path, rows, names):
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=names,extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)

def main():
    rec=[]
    for block in range(1,13):
        path=SOURCE/f"block_{block:02d}_source.csv"
        with path.open(newline="",encoding="utf-8-sig") as f:
            rows=list(csv.DictReader(f))
        for n,row in enumerate(rows):
            # Older exported CSVs lost numeric zero (0 became an empty string).
            # Recover the original row index from its position in the block.
            original_index = row["source_row_index"].strip()
            if original_index == "" and n == 0:
                row["source_row_index"] = "0"
            elif original_index == "":
                raise ValueError(f"Missing source index in {path} at source row {n}")
            assert int(row["source_row_index"]) == n, (path, n)
            assert row["source_block"]==f"Bloco{block}",(path,n)
            assert len(row["pdf_sha1"])==40,(path,n)
            # Stable IDs: retain source order including duplicates, never reorder by title.
            row["record_id"]=f"PQI-R{len(rec)+1:05d}"
            row["study_id"]="" # deferred until DOI/title/version reconciliation
            row["eligibility_status"]="NOT_VERIFIED"
            rec.append(row)
    assert len(rec)==2662, f"Expected 2662, found {len(rec)}"
    hashes=Counter(r["pdf_sha1"] for r in rec)
    for row in rec:
        row["same_hash_record_count"]=hashes[row["pdf_sha1"]]
    names=["record_id","study_id","source_row_id","source_block","source_row_index","pdf_filename","pdf_sha1","same_hash_record_count","title","abstract","publication_signal","eligibility_status","relevance_label_previous","needs_manual_review","source_csv_id"]
    write_csv(OUTPUT/"corpus_master_2662.csv",rec,names)

    # Blind reviewer files exclude prior labels, confidence, previous model decisions,
    # and historical screening signal; don't leak labels through source filenames.
    clean=["record_id","source_block","source_row_index","pdf_filename","title","abstract"]
    for b in range(50):
        lo=b*53 if b<38 else 38*53+(b-38)*54
        size=53 if b<38 else 54
        subset=rec[lo:lo+size]
        assert len(subset)==size
        write_csv(BLIND/f"batch_{b+1:02d}"/"blind_input.csv",subset,clean)
        write_csv(BLIND/f"batch_{b+1:02d}"/"assistant_decisions_template.csv",[
            dict(record_id=r["record_id"],screening_stage="",decision="",primary_reason="",evidence_location="",publication_verification="",reviewer_id="") for r in subset
        ],["record_id","screening_stage","decision","primary_reason","evidence_location","publication_verification","reviewer_id"])

    print("Source records:",len(rec),"global distinct PDF SHA-1:",len(hashes),"duplicate file occurrences:",len(rec)-len(hashes))
    print("Historic blocks:",dict(Counter(r["source_block"] for r in rec)))
    print("Created 50 blind source-order batches.")

if __name__=="__main__":main()
