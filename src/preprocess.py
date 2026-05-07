import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def load_data(path):

    if path.endswith(".parquet"):
        df = pd.read_parquet(path)
    else:
        df = pd.read_csv(path)

    df.columns = df.columns.str.strip()

    return df


def clean_data(df):

    df = df.replace([np.inf, -np.inf], np.nan)

    df = df.dropna()

    df = df.drop_duplicates()

    return df


def prepare_features(df):

    label_col = "Label"

    y = df[label_col].copy()

    X = df.drop(columns=[label_col])

    X = X.select_dtypes(include=["int64", "float64"])

    scaler = StandardScaler()

    X_scaled = scaler.fit_transform(X)

    return X_scaled, y, X.columns