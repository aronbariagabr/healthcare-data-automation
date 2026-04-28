import pandas as pd
from scripts.validate_data import validate_patient_data

def test_validate_patient_data_valid():
    df = pd.DataFrame({
        "patient_id": [1, 2],
        "age": [30, 45],
        "diagnosis": ["A", "B"]
    })
    assert validate_patient_data(df) is True

def test_validate_patient_data_missing_column():
    df = pd.DataFrame({
        "patient_id": [1],
        "age": [30]
    })
    assert validate_patient_data(df) is False

def test_validate_patient_data_with_nulls():
    df = pd.DataFrame({
        "patient_id": [1],
        "age": [None],
        "diagnosis": ["A"]
    })
    assert validate_patient_data(df) is False
