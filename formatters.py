import pandas as pd

def format_balanco_gas_geral(df: pd.DataFrame):
    df.dropna(how='all', axis=1, inplace=True)
    df.drop(columns=['BALANÇO DE GÁS NATURAL'], inplace=True)
    df.dropna(how='all', axis=0, inplace=True)
    df['BALANÇO DE GÁS NATURAL'] = ['0',
                   'Produção nacional',
                   'Reinjeção',
                   'Queima e perda',
                   'Consumo nas unidades de E&P',
                   'Absorção em UPGNs (GLP, C5+)',
                   'OFERTA NACIONAL',
                   'Importação - Bolívia',
                   'Regaseificação de GNL',
                   'OFERTA IMPORTADA',
                   'OFERTA TOTAL',
                   'Consumo - GASBOL',
                   'Consumo em outros gasodutos, desequilibrio, perdas e ajustes',
                   'Consumo nos gasodutos, desequilíbrio, perdas e ajustes'
                   ]
    df.set_index('BALANÇO DE GÁS NATURAL', inplace=True)
    df.drop(index=['0'], inplace=True)

    new_columns=[
        'media-2015',
        'media-2016',
        'media-2017',
        'media-2018',
        'media-2019',
        'jan',
        'fev',
        'mar',
        'abr',
        'mai',
        'jun',
        'jul',
        'ago',
        'set',
        'out',
        'nov',
        'dez',
        'media-2020'
    ]
    df.columns = new_columns
    return df


