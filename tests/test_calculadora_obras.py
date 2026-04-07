import pytest
from app.calculadora_obras import *

# ==========================================
# MÓDULO: ALVENARIA E ESTRUTURA
# Responsáveis: Nicolas Cleik ; Ana Clara
# ==========================================

def test_calcular_area_em_m2_valores_esperados():
    altura_do_objeto = 10
    comprimento_do_objeto = 30

    resultado = calcular_area_em_m2(altura=altura_do_objeto, comprimento=comprimento_do_objeto)

    assert resultado == 300

def test_calcular_area_em_m2_valores_negativos_igual_a_zero():
    with pytest.raises(ValueError) as info_erro:
        calcular_area_em_m2(0, -20)

    assert "Os valores de ALTURA e COMPRIMENTO devem ser maiores que zero" in str(info_erro.value)

def test_calcular_area_em_m2_altura_nao_numerica():
    with pytest.raises(ValueError) as info_erro:
        calcular_area_em_m2("cem", 10)

    assert "ALTURA deve ser um número" in str(info_erro.value)


def test_calcular_area_em_m2_comprimento_nao_numerico():
    with pytest.raises(ValueError) as info_erro:
        calcular_area_em_m2(10, "trinta")

    assert "COMPRIMENTO deve ser um número" in str(info_erro.value)

# ------------------------------------------

def test_calcular_tijolos_por_parede_valores_esperados():
    area_do_tijolo = calcular_area_em_m2(altura=0.20, comprimento=0.30)
    area_da_parede = calcular_area_em_m2(altura=5, comprimento=10)

    resultado = calcular_tijolos_por_parede(area_parede_m2 = area_da_parede, area_tijolo_m2 = area_do_tijolo)

    assert resultado == 833.33

def test_calcular_tijolos_por_parede_valores_negativos_igual_a_zero():
    with pytest.raises(ValueError) as info_erro:
        calcular_tijolos_por_parede(0, -20)

    assert "maiores que zero" in str(info_erro.value)


def test_calcular_tijolos_por_parede_area_parede_nao_numerica():
    with pytest.raises(ValueError) as erro:
        calcular_tijolos_por_parede("cinquenta", 0.06)

    assert "AREA_PAREDE deve ser um número" in str(erro.value)


def test_calcular_tijolos_por_parede_area_tijolo_nao_numerica():
    with pytest.raises(ValueError) as erro:
        calcular_tijolos_por_parede(50, "seis")

    assert "AREA_TIJOLO deve ser um número" in str(erro.value)

# ------------------------------------------

def test_calcular_volume_concreto_esperado():
    valor = calcular_volume_concreto(1,2,3)
    assert valor == 6

def test_calcular_volume_concreto_zero():
    with pytest.raises(ValueError) as info_erro:
        calcular_volume_concreto(0, 2, 2)

    assert 'Nenhum dos parâmetros deve ser menor ou igual a 0' in str(info_erro.value)

# ------------------------------------------

def test_calcular_sacos_cimento_esperado():
    valor = calcular_sacos_cimento(25,5)
    assert valor == 5

def test_calcular_sacos_cimento_zero():
    with pytest.raises(ValueError) as info_erro:
        calcular_sacos_cimento(25, 0)
    
    assert "Nenhum dos parâmetros deve ser menor ou igual a 0" in str(info_erro.value)
        
# ==========================================
# MÓDULO: ACABAMENTO E PINTURA
# Responsáveis: Pedro Gustavo;
# ==========================================

def test_calcular_caixas_piso_resultado():
    resultado = calcular_caixas_piso(area_ambiente_m2=200, rendimento_caixa_m2=2)
    assert resultado == 100

def test_calcular_caixas_piso_zero_negativo():
    with pytest.raises(ValueError) as info_erro:
        calcular_caixas_piso(area_ambiente_m2=10, rendimento_caixa_m2=0)
    
    assert "Erro: O rendimento da caixa deve ser maior que zero." in str(info_erro.value)

# ------------------------------------------


def test_calcular_rejunte_necessario_resultado():
    resultado = calcular_rejunte_necessario(10,2)
    assert resultado == 20

def test_calcular_rejunte_necessario_zero_negativo():
    with pytest.raises(ValueError) as info_erro:
        calcular_rejunte_necessario(10, 0)
    
    assert "Erro: O consumo de rejunte deve ser maior que zero." in str(info_erro.value)


# ------------------------------------------

def test_calcular_litros_tinta_resultado():
    resultado = calcular_litros_tinta(area_pintura_m2=20, rendimento_lata_m2=2, quantidade_demaos=2)
    assert resultado == 20

def test_calcular_litros_tinta_zero_negativo():
    with pytest.raises(ValueError) as info_erro:
        calcular_litros_tinta(area_pintura_m2=20, rendimento_lata_m2=0, quantidade_demaos=2)
    
    assert "Erro: O rendimento da lata deve ser maior que zero." in str(info_erro.value)

# ==========================================
# MÓDULO: LOGISTICA E ORÇAMENTO
# Responsáveis: Felipe
# ==========================================

def test_calcular_frete_entrega_resultado():
    """
    Testa o cálculo correto do frete.
    Cenário: 100km de distância e 500kg de carga.
    Cálculo: (100 * 2.0) + (500 * 0.5) = 200 + 250 = 450.0.
    Esperado: Retorno 450.0.
    """
    resultado = calcular_frete_entrega(100, 500)

    assert resultado == 450

def test_calcular_frete_entrega_valor_negativo():
    """
    Valida a proteção contra números negativos ou zero.
    Cenário: Distância de -10km.
    Esperado: Levantar um ValueError.
    """
    with pytest.raises(ValueError) as info:
        calcular_frete_entrega(-10, 50)
    assert "maiores que zero" in str(info.value)

def test_calcular_frete_entrega_valor_invalido():
    """
    Valida a proteção contra entradas que não são números (letras).
    Cenário: Distância informada como o texto "cem".
    Esperado: Levantar um TypeError (conforme o seu tratamento no except).
    """
    with pytest.raises(ValueError) as info:
        calcular_frete_entrega("cem", 500)
    assert "DISTANCIA deve ser um número" in str(info.value)

# ------------------------------------------

def test_capacidade_caminhao_resultado():
    """
    Testa se a logica basica funciona (capacidade maior que peso).
    Cenário: Cria um cenário real onde o peso (1200kg) é menor que a capacidade (2000kg).
    Esperado: "É verdade que o resultado foi True?". Como 1200 cabe em 2000, o teste passa.
    """
    assert capacidade_caminhao(1200, 2000) is True

def test_capacidade_caminhao_excedida():
    """
    Inverte a logica basica (peso maior que capacidade).
    Cenário: Coloca uma carga de 2000kg para um caminhão que só aguenta 1000kg.
    Esperado: "É verdade que o resultado foi False?". Como 2000 não cabe em 1000, o teste passa.
    """
    assert capacidade_caminhao(2000, 1000) is False

def test_capacidade_caminhao_valor_invalido():
    """
    Força um erro proposital enviando um número negativo.
    Cenário: with pytest.raises(ValueError): diz ao Python: "Eu sei que a linha de baixo vai dar um erro de valor, e eu quero que isso aconteça".
    Esperado: "É verdade que a função retornou ValueError?". Como -500 é negativo, o teste passa.
    """
    with pytest.raises(ValueError) as info:
        capacidade_caminhao(-500, 2000)
    assert "maior que zero" in str(info.value)