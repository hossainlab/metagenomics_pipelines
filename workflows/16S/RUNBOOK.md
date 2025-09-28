# 16S RUNBOOK (toy data)
- Manifest: generate with scripts/make_qiime_manifest.py (uses absolute paths).
- Use QIIME 2 to import and run DADA2 with trunc lengths informed by quality plots.
- Classify with SILVA/GTDB classifier registered in resources/dbs/registry.yaml.
