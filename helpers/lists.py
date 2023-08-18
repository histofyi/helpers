from typing import List
import hashlib
import json


def hash_array(arr) -> str:
    """
    This function takes an array and returns a hash of the sorted array

    Args:
        arr (array): the array to be hashed
    
    Returns:
        str: the hash of the sorted array
    """
    # sort the array
    sorted_array = sorted(arr)
    # join the array into a string
    sorted_array_str = ''.join(map(str, sorted_array))
    # return the hash of the string
    return hashlib.sha256(sorted_array_str.encode()).hexdigest()


def hash_dict(dictionary) -> str:
    dict_string = json.dumps(dictionary, sort_keys=True).encode()
    return hashlib.sha256(dict_string).hexdigest()


def deduplicate_list(pdb_code_list:List) -> List:
    """
    This function takes a list of PDB codes and returns a deduplicated list of PDB codes

    Args:
        pdb_code_list (List): the list of PDB codes
    
    Returns:
        List: the deduplicated list of PDB codes
    """
    deduplicated_list = [pdb_code for pdb_code in set(pdb_code_list)]
    sorted_list = sorted(deduplicated_list)
    return sorted_list