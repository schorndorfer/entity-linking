from typing import Tuple
from pathlib import Path
import pandas as pd
import re


def med_mentions(file_path: Path) -> Tuple[pd.DataFrame, pd.DataFrame]:
    title_pattern = re.compile(r"^(\d+)\|t\|(.+)$", re.MULTILINE)
    abstract_pattern = re.compile(r"^(\d+)\|a\|(.+)$", re.MULTILINE)
    assert file_path.exists()
    doc_data = {}
    mention_data = {
        "pmid": [],
        "start_index": [],
        "end_index": [],
        "text_segment": [],
        "sem_type_id": [],
        "entity_id": [],
    }
    with open(file_path) as file:
        for line in file:
            match = title_pattern.match(line)
            if match:
                doc_data[match.group(1)] = {
                    "title": match.group(2),
                }
            else:
                match = abstract_pattern.match(line)
                if match:
                    doc_data[match.group(1)]["abstract"] = match.group(2)
                else:
                    parts = line.split("\t")
                    if len(parts) == 6:
                        mention_data["pmid"].append(parts[0].strip())
                        mention_data["start_index"].append(parts[1].strip())
                        mention_data["end_index"].append(parts[2].strip())
                        mention_data["text_segment"].append(parts[3].strip())
                        mention_data["sem_type_id"].append(parts[4].strip())
                        mention_data["entity_id"].append(parts[5].strip())

    pmids = []
    titles = []
    abstracts = []
    for k, v in doc_data.items():
        pmids.append(k)
        titles.append(v["title"])
        abstracts.append(v["abstract"])

    return pd.DataFrame(
        {"pmid": pmids, "title": titles, "abstract": abstracts}
    ), pd.DataFrame(mention_data)


def umls_concepts() -> pd.DataFrame:
    return pd.DataFrame()
