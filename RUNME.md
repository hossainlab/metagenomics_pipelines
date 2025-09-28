# Metagenomics & AMR Pipelines — Sample Project (v1.1)

This bundle ships **three pipelines** with **toy sample data** for smoke‑testing on Ubuntu:

- A) **16S rRNA amplicon** (QIIME 2 / DADA2)
- B) **Shotgun ARG functional** (read‑based core; DIAMOND placeholder for toy run)
- C) **Bacterial WGS** for resistance pattern analysis (Illumina; Snakemake)

> The toy FASTQ files are only for validating your setup. Use real data + real databases for meaningful results.

---

## 1) Prerequisites (Ubuntu 22.04 / 24.04)

```bash
sudo apt-get update
sudo apt-get install -y build-essential wget curl git pigz unzip
```

### Install a fast Conda front‑end (choose one)

**Option A — Micromamba (tiny, recommended)**
```bash
"${SHELL}" <(curl -L micro.mamba.pm/install.sh)
micromamba shell init -s bash -p ~/micromamba
exec bash
```
Use it like conda: `micromamba create -n test python=3.10 -y && micromamba activate test`

**Option B — Miniforge (includes mamba)**
```bash
curl -LO https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh
bash Miniforge3-Linux-x86_64.sh -b -p $HOME/miniforge3
source ~/miniforge3/etc/profile.d/conda.sh
conda activate base
```

Set channels once (if using conda):
```bash
conda config --add channels conda-forge
conda config --add channels bioconda
conda config --set channel_priority strict
```

---

## 2) Get the project ready

Unzip this bundle somewhere (e.g., `~/projects/`) and enter the folder:
```bash
cd metagenomics_pipelines_v1
```

### Option 1 — One unified environment **with QIIME 2 (Amplicon 2024.10)**
> Easiest path if your solver is happy with a larger env.

```bash
# With mamba (preferred) or micromamba:
mamba env create -f deepbio-metagenomics-with-qiime2.yml   # file is in the project root
conda activate deepbio-metagenomics
qiime --help   # quick sanity check
```

### Option 2 — Smaller per‑pipeline envs (QIIME 2 separate)
> More robust on some systems; Snakemake will auto‑create envs with `--use-conda`.

```bash
# Create generic runner env (optional if using micromamba directly):
conda create -y -n snakemake snakemake=7.32 python=3.11
conda activate snakemake

# Pre‑create tool envs (optional; Snakemake can create them on‑demand)
conda env create -f envs/base-qc.yml
conda env create -f envs/metagenome.yml
conda env create -f envs/wgs.yml

# Install QIIME 2 in its own env per official 2024.10 instructions if you choose this route.
```

---

## 3) Databases (required for real analyses)

- **16S taxonomy**: SILVA or GTDB QIIME 2 classifier artifact.
- **Resistome**: CARD / MEGARes / ResFinder (for DIAMOND/RGI/AMRFinderPlus/ABRicate).
- **Taxonomic profiling**: Kraken2 “standard” or custom DBs.

Register absolute paths in `resources/dbs/registry.yaml`. This bundle contains placeholders only.

---

## 4) Run smoke tests with toy data

### 16S (minimal)
```bash
# Build a QIIME 2 manifest with absolute paths
python scripts/make_qiime_manifest.py --root "$(pwd)" --out metadata/samples_16s_manifest.tsv

# If QIIME 2 is active, you can proceed with import/denoise/classify as per workflows/16S/RUNBOOK.md
```

### Shotgun ARG (Snakemake)
```bash
snakemake -s workflows/shotgun_ARG/Snakefile --use-conda --conda-frontend mamba -j 4
```
*Note:* The toy run uses a **dummy DIAMOND step** so it finishes without real DBs. For real runs, point `config.yaml` to actual DBs and remove the dummy rule.

### WGS AMR (Snakemake)
```bash
snakemake -s workflows/WGS_AMR/Snakefile --use-conda --conda-frontend mamba -j 4
```
*Note:* The `shovill` step is stubbed for the toy run; replace with the real assembler call for production.

**Host decontamination:** If you don’t build a host Bowtie2 index, the pipeline falls back to copying reads so the toy run succeeds.

---

## 5) Contents

- `envs/` — Conda env YAMLs (base-qc, metagenome, wgs)
- `workflows/` — Snakemake skeletons + helper scripts
- `metadata/` — Sample sheets and a manifest generator
- `data/raw/` — Tiny toy FASTQ for each pipeline
- `resources/dbs/registry.yaml` — DB path placeholders
- `deepbio-metagenomics-with-qiime2.yml` — **Unified env** including QIIME 2 (2024.10)
- `RUNME.md` — This guide
- `RUNBOOK.md` — Operational notes & commands

---

## 6) Next steps

- Replace toy data in `data/raw/` with **real datasets** and update metadata files accordingly.
- Download and register **databases** in `resources/dbs/registry.yaml`.
- Prefer `--use-conda --conda-frontend mamba` for speed and reproducibility.
- Consider switching to **Nextflow** and containers for large projects.

---

## 7) Troubleshooting

- **Solver stuck**: Try Option 2 (separate envs) or use **micromamba**.
- **Permissions on HPC**: Use **Apptainer**/Docker images mirroring the YAMLs.
- **QIIME 2 plugin errors**: Ensure the `qiime2-amplicon=2024.10.*` env is active.

---

© DeepBio — Sample materials for pipeline validation.
