# Usage: snakemake filename.pdf

ruleorder:  tex2pdf_with_bib > tex2pdf_without_bib

rule tex2pdf_with_bib:
    input:
        tex='{name}.tex',
        bib='{name}.bib'
    output:
        'docs/{name}.pdf'
    shell:
        """
        pdflatex {wildcards.name}
        bibtex {wildcards.name}
        pdflatex {wildcards.name}
        pdflatex {wildcards.name}
        mv {wildcards.name}.pdf {output}
        """

rule tex2pdf_without_bib:
    input:
        '{name}.tex'
    output:
        'docs/{name}.pdf'
    shell:
        """
        xelatex {wildcards.name}
        mv {wildcards.name}.pdf {output}
        """

rule texclean:
    shell:
        "rm -f *.out *.log *.aux *.bbl *.blg *.synctex.gz *.fls *.flx *.fdb_latexmk"
