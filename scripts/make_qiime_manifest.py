#!/usr/bin/env python3
import argparse, os, csv, sys
p = argparse.ArgumentParser()
p.add_argument("--root", required=True)
p.add_argument("--out", required=True)
args = p.parse_args()
root = os.path.abspath(args.root)
rows = [
    ["sample-id","forward-absolute-filepath","reverse-absolute-filepath"]
]
samples = ["S1","S2"]
for s in samples:
    r1 = os.path.join(root, "data", "raw", f"{s}_R1.fastq.gz")
    r2 = os.path.join(root, "data", "raw", f"{s}_R2.fastq.gz")
    rows.append([s, r1, r2])
with open(args.out,"w",newline="") as f:
    w = csv.writer(f, delimiter=",")
    w.writerows(rows)
print(f"Wrote manifest to {args.out}", file=sys.stderr)
