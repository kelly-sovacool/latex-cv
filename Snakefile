# Usage: snakemake filename.pdf
import os

ruleorder:  tex2pdf_with_bib > tex2pdf_without_bib

names = [fn.strip(".tex") for fn in os.listdir() if fn.endswith(".tex")]

rule targets:
    input:
        expand("docs/{name}.pdf", name=names)

rule tex2pdf_with_bib:
    input:
        tex='{name}.tex',
        bib='{name}.bib'
    output:
        pdf='docs/{name}.pdf'
    shell:
        """
        pdflatex {wildcards.name}
        bibtex {wildcards.name}
        pdflatex {wildcards.name}
        pdflatex {wildcards.name}
        mv {wildcards.name}.pdf {output.pdf}
        rm -f *.out *.log *.aux *.bbl *.blg *.synctex.gz *.fls *.flx *.fdb_latexmk
        """

rule tex2pdf_without_bib:
    input:
        '{name}.tex'
    output:
        pdf='docs/{name}.pdf'
    shell:
        """
        xelatex {wildcards.name}
        mv {wildcards.name}.pdf {output.pdf}
        rm -f *.out *.log *.aux *.bbl *.blg *.synctex.gz *.fls *.flx *.fdb_latexmk
        """

rule texclean:
    shell:
        "rm -f *.out *.log *.aux *.bbl *.blg *.synctex.gz *.fls *.flx *.fdb_latexmk"
