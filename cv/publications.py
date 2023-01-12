"""
Format publication entries for my personal website
"""

import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import *
import datetime
import yaml
import sys

MONTHS = {'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6, 
          'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
          }

def main(bib_filename, yml_filename):
    with open(yml_filename, 'w') as file:
        yaml.dump([entry.__dict__ for entry in parse_entries(bib_filename)], file)

# adapted from https://bibtexparser.readthedocs.io/en/master/tutorial.html#step-4-add-salt-and-pep per
def parse_entries(bibtex_filename):
    with open(bibtex_filename, 'r') as bibtex_file:
        parser = BibTexParser()
        parser.customization = customizations
        bib_database = bibtexparser.load(bibtex_file, parser=parser)
    return sorted([BibEntry(record) for record in bib_database.entries], 
                  key = lambda x: x.year_mo, reverse = True)

# from https://bibtexparser.readthedocs.io/en/master/tutorial.html#step-4-add-salt-and-pepper
def customizations(record):
    """Use some functions delivered by the library

    :param record: a record
    :returns: -- customized record
    """
    record = convert_to_unicode(record)
    record = type(record)
    record = author(record)
    record = editor(record)
    record = journal(record)
    record = keyword(record)
    record = link(record)
    record = page_double_hyphen(record)
    record = doi(record)
    return record

def format_author(name, bold = 'Sovacool, Kelly'):
    last_firstmi = name.split(',')
    lastname = last_firstmi[0]
    if lastname.startswith('*'):
        lastname = f'\{lastname}' # escape asterisks for co-first authorship
    first_mi = last_firstmi[1].split()
    first_inits = first_mi[0][0] + first_mi[1][0] if len(first_mi) == 2 else first_mi[0][0]
    author = f'{lastname} {first_inits}'
    if bold in name:
        author = f'**{author}**'
    return author


class BibEntry:

    def __init__(self, record):
        self.id = record['ID']
        self.entry_type = record['ENTRYTYPE']
        self.doi = record['doi']
        self.doi_link = record['link'][0]['url']
        self.authors = record['author']
        self.title = record['title']
        self.title_md = f"[{self.title}]({self.doi_link})"
        self.authors_md = ', '.join([format_author(author) for author in record['author']])
        self.year = record['year']
        self.month = record['month'].capitalize()
        self.month_num = MONTHS[record['month'].lower()]
        self.year_mo = datetime.datetime.strptime(f"{record['year']}-{MONTHS[record['month'].lower()]}", '%Y-%m')
        self.date = f"{self.month} {self.year}"
        self.journal = record['journal']['name']
        self.link_md = f"[{record['doi']}]({self.doi_link})"
        self.journal_md = f"[{self.journal}]({self.doi_link})"
        self.title_journal = f"{self.title}.  _{self.journal_md}_"
        self.bib_md = f"{self.authors_md}. {self.month} " \
                f"{self.year}. " \
                f"{self.title}. _{self.journal}_. {self.link_md} "
        self.bib_tex = f"{self.authors_md}. {self.month}  {self.year}. {self.title}. \\textit{{{ self.journal }}}. \hyperref{{{ self.doi_link }}}{{{ record['doi'] }}} "
        self.github_link = record['github'] if 'github' in record else ''
        self.github_icon = f'<a href="{self.github_link}"> <i class="fa-brands fa-github" style="font-size:20px;"></i> </a>' if self.github_link else ''
        self.github_badge = f"[![GitHub](https://img.shields.io/static/v1?style=flat&logo=GitHub&label=+&message=GitHub&color=black)]({self.github_link})" if self.github_link else ''
        self.altmetrics_badge = f'<div data-badge-popover="right" data-badge-type="medium_badge" data-doi="{record["doi"]}" data-condensed="true" data-hide-no-mentions="false" class="altmetric-embed"></div>'
        self.dimensions_badge = f'<span class="__dimensions_badge_embed__" data-doi="{record["doi"]}" data-hide-zero-citations="true" data-style="small_rectangle" data-legend="hover-right"></span>'
        self.badges = f"{self.github_icon} {self.altmetrics_badge} {self.dimensions_badge}"

    def __repr__(self):
        return self.bib_md

    def github(self, 
                     font_size_px=20):
        return f'<a href="{self.github_link}"> <i class="fa-brands fa-github" style="font-size:{font_size_px}px;"></i> </a>' if self.github_link else ''

    def altmetrics(self, 
                  badge_type = 'donut', 
                  data_hide = "false"):
        return f'<div data-badge-popover="right" data-badge-type="{badge_type}" data-doi="{self.record["doi"]}" data-condensed="true" data-hide-no-mentions="{data_hide}" class="altmetric-embed"></div>'

    def dimensions(self,
                         data_hide = "true",
                         data_style = "small_circle",
                         data_legend = 'hover-right'):
        # https://badge.dimensions.ai/
        return f'<span class="__dimensions_badge_embed__" data-doi="{self.record["doi"]}" data-hide-zero-citations="{data_hide}" data-style="{data_style}" data-legend="{data_legend}"></span>'


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
