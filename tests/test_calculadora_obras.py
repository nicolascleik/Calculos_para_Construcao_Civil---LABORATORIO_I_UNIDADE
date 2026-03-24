import pytest
from app.calculadora_obras import calcular_area_em_m2

# ==========================================
# MÓDULO: ALVENARIA E ESTRUTURA
# Responsáveis: Nicolas Cleik ; SEU_NOME
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


# ==========================================
# MÓDULO: ACABAMENTO E PINTURA
# Responsáveis: SEU_NOME
# ==========================================,

# ==========================================
# MÓDULO: LOGISTICA E ORÇAMENTO
# Responsáveis: SEU_NOME
# ==========================================