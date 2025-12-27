import pytest
import pandas as pd
import numpy as np
from data_processing_old import load_and_clean_data


def test_cleaning():
    sample_data = pd.DataFrame(
        {
            "age": [63, 37],
            "sex": [1, 1],
            "cp": [1, 2],
            "trestbps": [145, 130],
            "chol": [233, 250],
            "fbs": [1, 0],
            "restecg": [0, 1],
            "thalach": [150, 187],
            "exang": [0, 0],
            "oldpeak": [2.3, 3.5],
            "slope": [0, 2],
            "ca": ["0", "?"],
            "thal": ["1", "?"],
            "target": [1, 0],
        }
    )
    df_clean = load_and_clean_data(sample_data)
    assert df_clean.isnull().sum().sum() == 0
    assert set(df_clean["target"].unique()).issubset({0, 1})
    assert df_clean.shape == (2, 14)
