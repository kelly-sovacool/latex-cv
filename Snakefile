# Usage: snakemake filename.pdf
import os

ruleorder:  tex2pdf_with_bib > tex2pdf_without_bib

names = [fn.strip(".tex") for fn in os.listdir() if fn.endswith(".tex")]

rule targets:
    input:
        expand("docs/{name}.pdf", name=names)

# rule repair_months:
#     input:
#         code='replace-months.sh',
#         bib="cv_KLS.Zotero.bib"
#     output:
#         bib="cv_KLS.bib"
#     shell:
#         """
#         bash {input.code} {input.bib} {output.bib}
#         """

rule tex2pdf_with_bib:
    input:
        tex='{name}.tex',
        bib='{name}.bib',
        bst='kls.bst'
    output:
        pdf='docs/{name}.pdf'
    shell:
        """
        xelatex {wildcards.name}
        bibtex {wildcards.name}
        xelatex {wildcards.name}
        xelatex {wildcards.name}
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
        "rm -f cv_KLS.pdf *.out *.log *.aux *.bbl *.blg *.synctex.gz *.fls *.flx *.fdb_latexmk "
