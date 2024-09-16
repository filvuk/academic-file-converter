# Map BibTeX publication types to universal CSL types
PUB_TYPES_BIBTEX_TO_CSL = {
    "article": "article-journal",
    "book": "book",
    "conference": "paper-conference",
    "inbook": "chapter",
    "incollection": "chapter",
    "inproceedings": "paper-conference",
    "manual": "book",
    "mastersthesis": "thesis",
    "patent": "patent",
    "phdthesis": "thesis",
    "proceedings": "book",
    "report": "report",
    "thesis": "thesis",
    "techreport": "report",
    "unpublished": "manuscript",
}

# adapted from https://docs.citationstyles.org/en/stable/specification.html#appendix-iii-types
PUB_TYPES_RIS_TO_CSL = {
    "JOUR": "article-journal",
    "EJOUR": "article-journal",
    "BOOK": "book",
    "EBOOK": "book",
    "EDBOOK": "book",
    "CPAPER": "paper-conference",
    "CHAP": "chapter",
    "ECHAP": "chapter",
    "CONF": "paper-conference",
    "THES": "thesis",
    "PAT": "patent",
    "RPRT": "report",
    "UNPB": "manuscript",
    "UNPD": "manuscript",
    "MANSCPT": "manuscript",
    "DATA": "dataset",
}
