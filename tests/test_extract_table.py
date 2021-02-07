import pytest
import tabula
import pandas as pd

from extract_tables import FILE, TEMPLATES_FILE, PANDAS_OPTIONS, read_table, \
    read_table_with_template, get_template
from formatters import format_balanco_gas_geral, format_demanda_por_mercado

pd.set_option('display.max_columns', 9999)


# @pytest.mark.parametrize('file, pages', (
#     (FILE, 2),
# ))
# def test_read_pdf_page(file, pages):
#     tables = read_table(file, pages)
#     assert len(tables) == 2

@pytest.mark.parametrize('template_file, template_name', (
        (TEMPLATES_FILE, 'Balanço de Gás Natural - Brasil'),
))
def test_get_template(template_file, template_name):
    template = get_template(template_file, template_name)[0]
    assert template.get('name') == template_name
    assert 'page' in template


@pytest.mark.parametrize('file, template_file, template_name', (
        (FILE, TEMPLATES_FILE, 'Balanço de Gás Natural - Brasil'),
))
def test_read_table_with_templates(file, template_file, template_name):
    table = read_table_with_template(file, template_file, template_name)
    assert isinstance(table, pd.core.frame.DataFrame)



def test_format_balanco_gas_natural():
    df = read_table_with_template(FILE, TEMPLATES_FILE, 'Balanço de Gás Natural - Brasil')
    balanco = format_balanco_gas_geral(df)
    assert balanco.shape == (13,18)


def test_format_demanda_por_mercados():
    df = read_table_with_template(FILE, TEMPLATES_FILE, 'Demanda por mercado - Brasil')
    balanco = format_demanda_por_mercado(df)
    assert balanco.shape == (8,18)