import tabula
import matplotlib
import pandas as pd


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


def read_table_with_template(file, template_file, template_name, fmt_func=None):
    template = get_template(template_file, template_name)
    with open('template.json', 'w') as json_file:
        json_file.write(json.dumps(template))
    table = tabula.read_pdf_with_template(file, 'template.json')[0]
    table.reindex()
    if fmt_func:
        format_balanco_gas_geral(table)
    return table


if __name__== '__main__':
    from formatters import format_balanco_gas_geral
    from slugify import slugify
    parser = argparse.ArgumentParser(prog='main',
                                     description='Conversor de tabelas do Gás Natural')
    tabelas = {
        'balanco-brasil': {
            'titulo': 'Balanço de Gás Natural - Brasil',
            'format_function': format_balanco_gas_geral
        }
    }
    parser.add_argument('--tabela', '-t', help='Tabela a ser extraída', required=True)

    args = parser.parse_args()
    if args.tabela in tabelas:
        titulo = tabelas[args.tabela]['titulo']
        func = tabelas[args.tabela]['format_function']
        df = read_table_with_template(FILE, TEMPLATES_FILE, titulo, func)
        df.to_csv(f'csv/{slugify(titulo)}.csv')

