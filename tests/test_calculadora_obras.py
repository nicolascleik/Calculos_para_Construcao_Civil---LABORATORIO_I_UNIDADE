import pytest
from app.calculadora_obras import calcular_area_em_m2, calcular_tijolos_por_parede, calcular_volume_concreto, calcular_sacos_cimento

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

def test_calcular_area_em_m2_erro_de_digitacao():
    with pytest.raises(TypeError):
        calcular_area_em_m2("cem", 10)

# ------------------------------------------

def test_calcular_tijolos_por_parede_valores_esperados():
    area_do_tijolo = calcular_area_em_m2(altura=0.20, comprimento=0.30)
    area_da_parede = calcular_area_em_m2(altura=5, comprimento=10)

    resultado = calcular_tijolos_por_parede(area_parede_m2 = area_da_parede, area_tijolo_m2 = area_do_tijolo)

    assert resultado == 833.33

def test_calcular_tijolos_por_parede_valores_negativos_igual_a_zero():
    with pytest.raises(ValueError) as info_erro:
        calcular_tijolos_por_parede(0, -20)

    assert "Os valores de AREA_PAREDE e AREA_TIJO devem ser maiores que zero! A função 'calcular_area_em_m2(altura, comprimento)' vai te ajudar entregando o resultado final em m2" in str(info_erro.value)

def test_calcular_tijolos_por_parede_erro_de_digitacao():
    with pytest.raises(TypeError):
        calcular_tijolos_por_parede("cem", 10)

# ------------------------------------------

def test_calcular_volume_concreto_esperado():
    valor = calcular_volume_concreto(1,2,3)
    assert valor == 6

def test_calcular_volume_concreto_zero():
    valor = calcular_volume_concreto(0,2,2)
    assert 'Nenhum dos parâmetros deve ser menor ou igual a 0'

# ------------------------------------------

def test_calcular_sacos_cimento_esperado():
    valor = calcular_sacos_cimento(25,5)
    assert valor == 5

def test_calcular_sacos_cimento_zero():
    valor = calcular_sacos_cimento(25,0)
    assert 'Nenhum dos parâmetros deve ser menor ou igual a 0'
        
# ==========================================
# MÓDULO: ACABAMENTO E PINTURA
# Responsáveis: SEU_NOME
# ==========================================,

# ==========================================
# MÓDULO: LOGISTICA E ORÇAMENTO
# Responsáveis: SEU_NOME
# ==========================================
