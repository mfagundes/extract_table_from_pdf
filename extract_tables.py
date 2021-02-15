import tabula
import matplotlib
import pandas as pd

import settings

pd.set_option('display.max_columns', 9999)
from pathlib import Path
import json

import argparse

INPUT = Path('pdf')
OUTPUT = Path('csv')
TEMPLATES = Path('templates')
FILE = INPUT / 'boletim-mensal-acompanhamento-mercado-gas-novembro_2020.pdf'
TEMPLATES_FILE = TEMPLATES / 'balancos-template.json'
PANDAS_OPTIONS={
    'header': None
}


def read_table(file, pages):
    tables = tabula.read_pdf(file, pages=str(pages), pandas_options=PANDAS_OPTIONS, stream=True)
    return tables


class TemplateException(Exception):
    pass


def get_template(template_file, template_name):
    with open(template_file, 'r') as f:
        templates = json.loads(f.read())
    template_json = [template for template in templates if template['name'] == template_name]
    if len(template_json) != 1:
        raise TemplateException(f"Error in template: {len(template_json)} instances found")

    return list(template_json)


def read_table_with_template(file, template_file, template_name, fmt_func=None, args=None):
    if args is None:
        args = {}
    template = get_template(template_file, template_name)
    with open('template.json', 'w') as json_file:
        json_file.write(json.dumps(template))
    table = tabula.read_pdf_with_template(file, 'template.json', pandas_options={'header':None})[0]
    if fmt_func:
        table = fmt_func(table, **args)
    return table


if __name__== '__main__':
    from formatters import format_balanco_gas_geral, format_demanda_por_mercado
    from slugify import slugify
    parser = argparse.ArgumentParser(prog='main',
                                     description='Conversor de tabelas do Gás Natural',
                                     formatter_class=argparse.RawTextHelpFormatter
                                     )
    tabelas = settings.TABELAS
    import textwrap
    tabelas_help = textwrap.dedent('''\
    Tabela a ser extraída. Valores válidos:
    ---------------------------------------
    ''')
    for tabela in tabelas.items():
        tabelas_help += textwrap.indent(
            f"{tabela[0]}: {tabela[1]['titulo']}\n",
            prefix='+')
    parser.add_argument(
        '--tabela',
        '-t',
        help=tabelas_help,
        required=True
    )

    args = parser.parse_args()
    if args.tabela in tabelas:
        titulo = tabelas[args.tabela]['titulo']
        tab_definitions = tabelas[args.tabela]
        func = tab_definitions['format_function']
        args = tab_definitions.get('args', None)
        df = read_table_with_template(FILE, TEMPLATES_FILE, titulo, func, args)
        df.to_csv(f'csv/{slugify(titulo)}.csv')

