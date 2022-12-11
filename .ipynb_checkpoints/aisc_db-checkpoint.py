import pandas as pd



def load_aisc_db(units = 'si') -> pd.DataFrame:
    """
    Returns a DataFrame of the AISC database table contained in the file.
    """
    if units.lower() == 'si':
        return pd.read_csv('aisc_db_si.csv')
    elif units.lower() == 'us':
        return pd.read_csv('aisc_db_us.csv')
    else:
        print("Acceptable units are either 'us' or 'si'")
        
def sections_by_type(aisc_db: pd.DataFrame, section_type: str) -> pd.DataFrame:
    """
    Returns df with sections of that type
    """
    return aisc_db.loc[aisc_db.Type == section_type]