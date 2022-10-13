from pathlib import Path
from elinker import datasets as D


def test_med_mentions():
    doc_data, mention_data = D.med_mentions(Path("../data/medmentions/full/corpus_pubtator.txt"))
    print(doc_data.head())
    print(mention_data.head())
