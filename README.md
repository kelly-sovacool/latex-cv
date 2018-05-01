# LaTeX templates
A collection of LaTex templates + a Snakemake pipeline for compiling tex to pdf.
The Snakefile was shamelessly copied from [the Snakemake documentation](http://snakemake.readthedocs.io/en/stable/getting_started/examples.html#building-a-paper-with-latex).

## Setup

You can download this repository with:
```
$ git clone https://github.com/kelly-sovacool/latex-templates.git
```

If you want to use the Snakemake pipeline, be sure to install [`snakemake`](http://snakemake.readthedocs.io/en/stable/getting_started/installation.html) and a [LaTeX distribution](https://en.wikibooks.org/wiki/LaTeX/Installation#Distributions) which includes `pdflatex` and `bibtex`.

Otherwise, go right ahead editing the .tex templates to your liking with your favorite text editor.
I use [Atom](https://atom.io/) with the [language-latex](https://atom.io/packages/language-latex) package.

## Usage

You can convert tex files to pdf using:
```
$ snakemake paper.pdf
```
Snakemake will use `pdflatex` to generate `paper.pdf` from `paper.tex`.
If `paper.bib` exists, it will use `bibtex` to generate the bibliography.

Clean up intermediate files with:
```
$ snakemake texclean
```

See the [Snakemake documentation](http://snakemake.readthedocs.io/en/stable/index.html) for more details on using and customizing Snakemake pipelines.

## Templates

See ![alt ref](paper.pdf) and ![alt ref](assignment.pdf) for template examples.
