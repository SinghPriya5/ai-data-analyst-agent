import pandas as pd

def clean_data(df):

    # remove duplicates
    df = df.drop_duplicates()

    # fill missing values
    df = df.fillna(df.mean(numeric_only=True))

    return df