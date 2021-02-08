import pandas as pd



def format_balanco_gas_geral(df: pd.DataFrame, **kwargs):
    drop_rows = kwargs.get('drop_rows', 2)
    rows = kwargs.get('rows')
    cols = kwargs.get('cols')
    adjusts = kwargs.get('adjusts', None)
    index_name = kwargs.get('index_name')

    if adjusts:
        for adj in adjusts:
            df.loc[adj[0], adj[1]] = adj[2]

    df.set_index(df.columns[0], inplace=True)
    df.dropna(how='all', axis=1, inplace=True)
    df.dropna(how='all', axis=0, inplace=True)
    df = df.iloc[drop_rows:]
    df.index = rows
    df.columns = cols
    df.index.names = [index_name]
    return df


def format_demanda_por_mercado(df: pd.DataFrame, **kwargs):
    drop_rows = kwargs.get('drop_rows', 2)
    rows = kwargs.get('rows')
    cols = kwargs.get('cols')
    index_name = kwargs.get('index_name')

    df.set_index(df.columns[0], inplace=True)
    df.index.names = [index_name]
    df.columns = cols
    return df


def format_balanco_gas_interligada(df: pd.DataFrame, **kwargs):
    drop_rows = kwargs.get('drop_rows', 2)
    rows = kwargs.get('rows')
    cols = kwargs.get('cols')

    df.loc[1, 16] = 'dez'

    df.set_index(df.columns[0], inplace=True)
    df.dropna(how='all', axis=1, inplace=True)
    df.dropna(how='all', axis=0, inplace=True)
    df = df.iloc[drop_rows:]
    df.index = rows
    df.columns = cols
    return df


