import pandas as pd


def find_index(data: pd.DataFrame, method: pd.DataFrame) -> pd.DataFrame:
    df = data
    data_replace = method
    for index in data_replace.index:
        df.original[index] = data_replace[index].original
    return df
