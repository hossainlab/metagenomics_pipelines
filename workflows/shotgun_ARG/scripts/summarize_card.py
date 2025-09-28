#!/usr/bin/env python3
import sys, pandas as pd, os
tsv = sys.argv[1]
df = pd.read_csv(tsv, sep="\t")
# Collapse by sseqid (ARG id) and count hits
if "sseqid" in df.columns:
    out = df.groupby("sseqid").size().reset_index(name="count")
else:
    out = pd.DataFrame({"sseqid":[], "count":[]})
out_path = os.path.join(os.path.dirname(tsv), "arg_abundance.tsv")
out.to_csv(out_path, sep="\t", index=False)
print(f"Wrote {out_path}")
