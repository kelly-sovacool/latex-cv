# LaTeX CV

My curriculum vitae in LaTeX + a Snakemake pipeline for compiling tex to pdf.
The Snakefile was shamelessly copied from [the Snakemake documentation examples](http://snakemake.readthedocs.io/en/stable/getting_started/examples.html#building-a-paper-with-latex).

## Setup

You can download this repository with:
```
$ git clone https://github.com/kelly-sovacool/latex-templates.git
```

If you want to use the Snakemake pipeline, be sure to install [Snakemake](http://snakemake.readthedocs.io/en/stable/getting_started/installation.html) and a [LaTeX distribution](https://en.wikibooks.org/wiki/LaTeX/Installation#Distributions) which includes `pdflatex` and `bibtex`.

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


## Examples

* [`cv_KLS.tex`](cv_KLS.tex): my actual curriculum vitae for science using `moderncv.cls`: based on a template from the [moderncv repo](https://github.com/xdanaux/moderncv).
* [`sound.tex`](sound.tex): my CV for live sound engineering, also using `moderncv.cls`.
* [`res/res_KLS.tex`](res/res_KLS.tex): an old-style curriculum vitae using `res.cls`: based on a template from [LaTeXTemplates.com](http://www.LaTeXTemplates.com).
* [`other_templates/`](other_templates/): templates for homework assignments, essays, etc.


## Motivation

While using the world's most popular word processor to write a fairly large research paper, 
I ran into some frustrating issues: cross-references not updating automatically, 
the program hanging up when adjusting figure boundaries, weird/ugly placement of figures, etc. 
I decided enough was enough; I needed to make the jump to LaTeX -- preferably before undertaking another large writing task. 
So I began creating simple templates and updated my CV with LaTeX to learn the ropes, and now here we are. 
Here's hoping I never have to use a WYSIWYG again...

For writing scientific manuscripts with collaborators, it may make more sense to use Markdown or R Markdown, then convert to LaTeX for submission. Examples:

* https://github.com/greenelab/meta-review
* https://oleb.net/blog/2016/02/collaborative-writing-on-github/
* https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4945047/pdf/pcbi.1004947.pdf
* https://github.com/ypriverol/github-paper
* https://github.com/SchlossLab/Westcott_OptiClust_mSphere_2017

