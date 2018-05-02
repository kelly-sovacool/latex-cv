# LaTeX templates
A collection of LaTeX templates + a Snakemake pipeline for compiling tex to pdf.
The Snakefile was shamelessly copied from [the Snakemake documentation examples](http://snakemake.readthedocs.io/en/stable/getting_started/examples.html#building-a-paper-with-latex).

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

* `assignment.tex`: for homework assignments such as problem sets from a textbook.
* `paper.tex`: for short papers, essays, and other writing assignments.
* `cv_res.tex`: an old-style curriculum vitae, uses `res.cls`.
* `cv_KLS.tex`: my actual curriculum vitae, uses `moderncv.cls`.

## Motivation

While using the world's most popular word processor to write a fairly large research paper, I ran into some frustrating issues: cross-references not updating automatically, the program hanging up when adjusting figure boundaries, weird/ugly placement of figures, etc. I decided enough was enough; I needed to make the jump to LaTeX -- preferably before undertaking another large writing task. So, here we are. Hopefully, the tex files stored here will grow in number and complexity as I learn more about LaTeX.

## TODO

* cv template: fix alignment of contact info.
* cv bib: get journal for `inproceedings` entry to show up in bibliography.
* scientific manuscript template.
