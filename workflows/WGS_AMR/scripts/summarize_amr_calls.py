#!/usr/bin/env python3
import sys, pandas as pd, os
amrf, rgi, abri = sys.argv[1], sys.argv[2], sys.argv[3]
# Create a minimal merged summary for the toy run
df1 = pd.read_csv(amrf, sep="\t")
df2 = pd.read_csv(rgi, sep="\t")
df3 = pd.read_csv(abri, sep="\t")
out = pd.DataFrame({
    "gene": df1["gene"].iloc[:1] if "gene" in df1 else ["NA"],
    "drug_class": df1["drug_class"].iloc[:1] if "drug_class" in df1 else ["NA"],
    "ARO": df2["ARO"].iloc[:1] if "ARO" in df2 else ["NA"],
    "abricate_gene": df3["GENE"].iloc[:1] if "GENE" in df3 else ["NA"]
})
out_path = os.path.join(os.path.dirname(amrf), "..", "reports", "amr_summary.tsv")
os.makedirs(os.path.dirname(out_path), exist_ok=True)
out.to_csv(out_path, sep="\t", index=False)
print(f"Wrote {out_path}")
