import pandas as pd

def validate_patient_data(df: pd.DataFrame) -> bool:
    """
    Validate patient dataset by checking required columns and missing values.
    
    Args:
        df (pd.DataFrame): Patient data
    
    Returns:
        bool: True if dataset is valid, False otherwise
    """
    required_cols = {"patient_id", "age", "diagnosis"}
    if not required_cols.issubset(df.columns):
        return False
    return not df.isnull().any().any()
