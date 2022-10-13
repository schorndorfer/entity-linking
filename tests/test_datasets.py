import os
from pathlib import Path
from elinker import datasets as D


dir_path = Path(os.path.dirname(os.path.realpath(__file__)))


def test_med_mentions():
    doc_data, mention_data = D.med_mentions(dir_path/"../data/MedMentions/full/data/corpus_pubtator.txt")
    assert doc_data.shape == (4392, 3)
    assert mention_data.shape == (352496, 6)
    assert mention_data['pmid'].nunique() == doc_data['pmid'].nunique()
    assert len(set(mention_data['pmid'])) == 4392
