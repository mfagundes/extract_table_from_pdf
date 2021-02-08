from formatters import format_balanco_gas_geral, format_demanda_por_mercado

BALANCO_COLS_2020 = [
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

BALANCO_INDEX_2020 = [
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

BALANCO_INDEX_INTERLIGADA_2020 = [
    'Produção na malha interligada',
    'Reinjeção',
    'Queima e perda',
    'Consumo nas unidades de E&P + Absorção em UPGNs (GLP, C5+)',
    'OFERTA NA MALHA INTERLIGADA',
    'Importação - Bolívia',
    'Regaseificação de GNL',
    'OFERTA IMPORTADA',
    'TOTAL OFERTA',
    'Consumo - GASBOL',
    'Consumo em outros gasodutos, desequilibrio, perdas e ajustes',
    'Consumo nos gasodutos, desequilíbrio, perdas e ajustes'
]

BALANCO_INDEX_ISOLADOS_2020 = [
    'Produção nos sistemas isolados',
    'Reinjeção',
    'Queima e perda',
    'Consumo nas unidades de E&P + Absorção em UPGNs (GLP, C5+)',
    'OFERTA NOS SISTEMAS ISOLADOS',
    'Desequilíbrios, perdas e ajustes',
]


BALANCO_COLS_INTERLIGADA_2020 = [
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

TABELAS = {
        'balanco-brasil': {
            'titulo': 'Balanço de Gás Natural - Brasil',
            'format_function': format_balanco_gas_geral,
            'args': {
                'index_name': 'balanco-brasil',
                'rows': BALANCO_INDEX_2020,
                'cols': BALANCO_COLS_2020
            }
        },
        'demanda-mercado-brasil': {
            'titulo': 'Demanda por mercado - Brasil',
            'format_function': format_demanda_por_mercado,
            'args': {
                'index_name': 'demanda-por-mercado-brasil',
                'cols': BALANCO_COLS_2020
            }
        },
        'balanco-malha-interligada': {
            'titulo': 'Balanço de Gás Natural - Malha Interligada',
            'format_function': format_balanco_gas_geral,
            'args': {
                'index_name': 'balanco-gas-natural',
                'rows': BALANCO_INDEX_INTERLIGADA_2020,
                'cols': BALANCO_COLS_INTERLIGADA_2020,
                'adjusts': [
                    (1, 16, 'dez')
                ]
            }
        },
        'demanda-malha-interligada': {
            'titulo': 'Demanda por mercado - Malha Interligada',
            'format_function': format_demanda_por_mercado,
            'args': {
                'index_name': 'demanda-por-mercado',
                'cols': BALANCO_COLS_INTERLIGADA_2020,
            }
        },
        'balanco-sistemas-isolados': {
            'titulo': 'Balanço de gás natural - Sistemas Isolados',
            'format_function': format_balanco_gas_geral,
            'args': {
                'index_name': 'balanco-gas-natural',
                'rows': BALANCO_INDEX_ISOLADOS_2020,
                'cols': BALANCO_COLS_INTERLIGADA_2020
            }
        },
        'demanda-sistemas-isolados': {
            'titulo': 'Demanda por mercado - Sistemas Isolados',
            'format_function': format_demanda_por_mercado,
            'args': {
                'index_name': 'demanda-por-mercado',
                'cols': BALANCO_COLS_INTERLIGADA_2020
            }
        }
    }

