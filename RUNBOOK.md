# RUNBOOK — Pipelines & Commands

This runbook summarizes how to execute each pipeline. See the canvas or the design doc for a full rationale.

## A) 16S (QIIME 2)
1) QC with fastp (optional smoke test only).
2) Import using QIIME 2 with a paired-end manifest (Phred33V2).
3) Trimming with q2-cutadapt.
4) Denoise with DADA2.
5) Taxonomy with pre-trained SILVA/GTDB classifier.
6) Phylogeny and diversity metrics.
7) Visualizations & exports.

## B) Shotgun ARG (read-based core)
1) QC → host decontamination (keeps unmapped).
2) Optional taxonomy (Kraken2/Bracken).
3) DIAMOND vs CARD/MEGARes (requires DB).
4) Summarize to gene/class/mechanism levels.
5) MultiQC & reports.

## C) WGS AMR (isolates)
1) QC → assembly (Shovill).
2) Annotation (Bakta).
3) AMR calls: AMRFinderPlus + RGI + ABRicate.
4) MLST + plasmids; optional SNP phylogeny.

> See each `workflows/*/Snakefile` and `metadata/*` files for sample names and config.
