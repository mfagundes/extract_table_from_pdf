import pandas as pd

from settings import BALANCO_COLS_2020, BALANCO_INDEX_2020

def format_balanco_gas_geral(df: pd.DataFrame, drop_rows=2):
    df.set_index(df.columns[0], inplace=True)
    df.dropna(how='all', axis=1, inplace=True)
    df.dropna(how='all', axis=0, inplace=True)
    df = df.iloc[drop_rows:]
    df.index = BALANCO_INDEX_2020

    df.columns = BALANCO_COLS_2020
    return df


def format_demanda_por_mercado(df: pd.DataFrame):
    df.set_index(df.columns[0], inplace=True)
    df.index.names = ['Mercados']
    df.columns = BALANCO_COLS_2020
    return df