import pandas as pd

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transform patient dataset by normalizing age values.
    
    Args:
        df (pd.DataFrame): Patient data
    
    Returns:
        pd.DataFrame: DataFrame with normalized age column
    """
    df["age_normalized"] = (df["age"] - df["age"].mean()) / df["age"].std()
    return df
