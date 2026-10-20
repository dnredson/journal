#!/usr/bin/env python3
"""Rebuild a provenance-preserving PQI master from local ZIPs and screening exports.

Run in a checkout of dnredson/journal:
  python review_audit/tools/rebuild_corpus.py --zips "C:/Users/.../PQI Artigos" --out review_audit/source
No network dependencies; does not infer unknown bibliographic data or peer-review.
"""
import argparse, csv, hashlib, pathlib, re, zipfile, collections

def get_block(path):
    m = re.search(r"bloco\s*0*([1-9]|1[0-2])", str(path), re.I)
    return int(m.group(1)) if m else None

def zip_records(root):
    rows = []
    for zpath in sorted(root.rglob("*.zip")):
        block=get_block(zpath)
        if block is None: continue
        with zipfile.ZipFile(zpath) as archive:
            for member in archive.infolist():
                if member.is_dir() or not member.filename.lower().endswith(".pdf"): continue
                h=hashlib.sha1()
                with archive.open(member) as f:
                    for chunk in iter(lambda:f.read(1<<20), b""):h.update(chunk)
                rows.append(dict(original_block=f"Bloco {block}",source_archive=str(zpath.relative_to(root)),
                                 filename=member.filename,pdf_sha1=h.hexdigest(),source="original_zip",
                                 title="",doi="",venue="",abstract="",peer_review_status="UNVERIFIED"))
    return rows

def existing_screens(root):
    out=[]
    for path in sorted((root/"review_audit"/"assistant").glob("*.csv")):
        with path.open(encoding="utf-8-sig",newline="") as f:
            for row in csv.DictReader(f):
                block=row.get("source_block") or row.get("original_block")
                idx=row.get("source_row") or row.get("original_row")
                if not block or idx is None:continue
                out.append(dict(original_block=block,original_row=idx,
                                filename=row.get("filename",""),pdf_sha1=row.get("sha1") or row.get("pdf_sha1") or "",
                                title=row.get("title",""),source=str(path.relative_to(root)),
                                preliminary_label=row.get("provisional_label") or row.get("preliminary_decision") or "",
                                peer_review_status="UNVERIFIED"))
    return out

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--zips",type=pathlib.Path,help="folder holding historical Bloco*.zip archives")
    p.add_argument("--repo",type=pathlib.Path,default=pathlib.Path(__file__).resolve().parents[2])
    p.add_argument("--out",type=pathlib.Path,default=None)
    args=p.parse_args()
    repo=args.repo.resolve(); dest=args.out or repo/"review_audit"/"source";dest.mkdir(parents=True,exist_ok=True)
    rows=zip_records(args.zips) if args.zips else []
    prior=existing_screens(repo)
    # Match known screening rows to PDFs by hash, never assume a file name is unique.
    by_hash=collections.defaultdict(list)
    for item in rows:by_hash[item["pdf_sha1"]].append(item)
    unresolved=[]
    for item in prior:
        matched=by_hash.get(item["pdf_sha1"],[])
        if len(matched)==1:
            match=matched[0]
            if item.get("title") and not match.get("title"):match["title"]=item["title"]
            match.setdefault("screening_sources",[]).append(item["source"])
        elif not rows:
            unresolved.append(item)
        else:
            unresolved.append(item)
    # When ZIPs are absent, derive partial master from available screening decisions;
    # duplicate screening entries for a source row collapse to one record.
    if not rows:
        seen=set()
        for item in prior:
            key=(item["original_block"],item["original_row"])
            if key not in seen:
                seen.add(key);rows.append(item)
    cols=["record_id","original_block","original_row","source_archive","filename","pdf_sha1","title","doi","venue","abstract","peer_review_status","source","preliminary_label","screening_sources"]
    rows.sort(key=lambda v:(get_block(v["original_block"]) or 99,int(v.get("original_row",-1) or -1),v.get("filename","")))
    for n,item in enumerate(rows,1):item["record_id"]=f"PQI-R{n:05d}"
    out=dest/("corpus_master_from_zips.csv" if args.zips else "corpus_master_partial.csv")
    with out.open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=cols,extrasaction="ignore");w.writeheader()
        for item in rows:
            item=dict(item);item["screening_sources"]=";".join(item.get("screening_sources",[]))
            w.writerow(item)
    print(f"{len(rows)} rows -> {out}")
    if unresolved:print(f"{len(unresolved)} screening row(s) unmatched/ambiguous; inspect manually.")
    if args.zips:print("Compare output to expected 2662 historical source records; hash-only matches are not study-level deduplication.")
if __name__=="__main__":main()
