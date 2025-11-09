# Epistemic State Updates in LLM Agents

## Overview
This repository contains the LaTeX manuscript *Epistemic State Updates in LLM Agents via Public Announcement and Graded Modal Logic*. The paper develops a workflow for giving large language model agents explicit epistemic state tracking, combines public announcement logic with lightweight grading of belief strength, and illustrates the ideas with small Python prototypes and TikZ figures. A prebuilt PDF (`main.pdf`) is generated from `main.tex` for quick reference.

## Repository Layout
- `main.tex` – master document that assembles the manuscript, loads packages, and includes each section file.
- `sections/` – chapter-wise LaTeX sources (`01-...` through `06-...`) produced from the working doc; edit these to update the paper body.
- `figures/` – TikZ assets, e.g. `knowledge-update-flow.tex` renders the epistemic update loop diagram.
- `references.bib` – BibTeX database covering epistemic logic, graded modal logic, and agent benchmarks.
- `code/` – toy Python modules (`knowledge_base.py`, `pipeline_loop.py`) that demonstrate the knowledge-base API discussed in the text.

Auxiliary build outputs (`main.aux`, `main.log`, etc.) are committed for convenience but can be regenerated at any time.

## Build Instructions
Ensure a full TeX distribution with `latexmk`, `pdflatex`, `bibtex`, `tikz`, and the packages loaded in `main.tex` (`geometry`, `booktabs`, `tabularx`, `hyperref`, `enumitem`, `listings`, `xcolor`, etc.).

Common build paths:

```bash
# Preferred: automatically handles reruns/bibliography
latexmk -pdf main.tex

# Manual: when latexmk is unavailable
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

To clean auxiliary files while keeping the PDF:

```bash
latexmk -c main.tex
```

The compiled paper is written to `main.pdf` in the repository root.

## Working With Content
- **Editing prose**: modify the corresponding file in `sections/` and rerun the build. Section headers align with LaTeX `\section` commands already present.
- **Adding figures**: place new TikZ or image assets in `figures/` and include them from a section with `\input{figures/<name>}` or `\includegraphics`.
- **Citations**: append entries to `references.bib` and cite them in the text with `\cite{key}`; rebuild so `bibtex` refreshes the bibliography.
- **Python examples**: run `python code/pipeline_loop.py` to exercise the illustrative knowledge-base loop described in the manuscript. Extend `code/` as needed for richer demonstrations.

