import pytest
import tabula
import pandas as pd

import settings
from extract_tables import FILE, TEMPLATES_FILE, PANDAS_OPTIONS, read_table, \
    read_table_with_template, get_template
from formatters import format_balanco_gas_geral, format_demanda_por_mercado, format_balanco_gas_interligada

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
    name = 'balanco-brasil'
    settings_ = settings.TABELAS.get(name)
    kwargs = settings_['args']
    df = read_table_with_template(FILE, TEMPLATES_FILE, settings_['titulo'])
    balanco = format_balanco_gas_geral(df, **kwargs)
    assert balanco.shape == (13,18)


def test_format_demanda_por_mercados():
    name = 'demanda-mercado-brasil'
    settings_ = settings.TABELAS.get(name)
    kwargs = settings_['args']
    df = read_table_with_template(FILE, TEMPLATES_FILE, settings_['titulo'])
    balanco = format_demanda_por_mercado(df, **kwargs)
    assert balanco.shape == (8,18)


def test_format_balanco_malha_interligada():
    name = 'balanco-malha-interligada'
    settings_ = settings.TABELAS.get(name)
    df = read_table_with_template(FILE, TEMPLATES_FILE, settings_['titulo'])
    kwargs = settings_['args']
    balanco = format_balanco_gas_geral(df, **kwargs)
    assert balanco.shape == (12,17)

def test_format_demanda_por_mercado_interligada():
    name = 'demanda-malha-interligada'
    settings_ = settings.TABELAS.get(name)
    kwargs = settings_['args']
    df = read_table_with_template(FILE, TEMPLATES_FILE, settings_['titulo'])
    balanco = format_demanda_por_mercado(df, **kwargs)
    assert balanco.shape == (8,17)

def test_format_balanco_malha_isolada():
    name = 'balanco-sistemas-isolados'
    settings_ = settings.TABELAS.get(name)
    kwargs = settings_['args']
    df = read_table_with_template(FILE, TEMPLATES_FILE, settings_['titulo'])
    balanco = format_balanco_gas_geral(df, **kwargs)
    assert balanco.shape == (6,17)

def test_format_demanda_por_mercado_isolados():
    name = 'demanda-malha-interligada'
    settings_ = settings.TABELAS.get(name)
    kwargs = settings_['args']
    df = read_table_with_template(FILE, TEMPLATES_FILE, settings_['titulo'])
    balanco = format_demanda_por_mercado(df, **kwargs)
    assert balanco.shape == (8,17)

