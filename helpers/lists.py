from typing import List

def deduplicate_list(pdb_code_list:List) -> List:
    deduplicated_list = [pdb_code for pdb_code in set(pdb_code_list)]
    sorted_list = sorted(deduplicated_list)
    return sorted_list