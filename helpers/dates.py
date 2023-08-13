import datetime

def parse_pdbdate_to_isoformat(datestring:str) -> str:
    """
        This function takes an 8 digit datestring from the PDBe return and delivers an ISO formated date string
    """
    try:
        date = datetime.date(int(datestring[0:4]), int(datestring[4:6]), int(datestring[6:8]))
        return date.isoformat()
    except:
        return datestring

def parse_pdbdate_to_year(datestring:str) -> str:
    """
        This function takes an 8 digit datestring from the PDBe return and delivers a four digit year as a string
    """
    return datestring[0:4]