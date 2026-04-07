
# ==========================================
# MÓDULO: LOGISTICA E ORÇAMENTO
# Responsáveis: Felipe
# ==========================================

def calcular_frete_entrega(distancia_km, peso_carga_kg):
    """
    Calcula o frete de uma entrega baseado na distancia e peso da carga, R$ 2,00 por KM + R$ 0,50 por KG.
    Args:
        distancia_km (float): A distancia que será percorrida em KM.
        peso_carga_kg (float): O peso que será transportado em KG.
    Returns:
        float: O preço do frete arredondado.
    """
    if type(distancia_km) != int and type(distancia_km) != float:
        raise ValueError("DISTANCIA deve ser um número")

    if type(peso_carga_kg) != int and type(peso_carga_kg) != float:
        raise ValueError("PESO deve ser um número")

    if distancia_km <= 0 or peso_carga_kg <= 0:
        raise ValueError("Os números de distancia e peso devem ser maiores que zero")
    
    frete = (distancia_km * 2) + (peso_carga_kg * 0.5)

    return round(frete, 2)

def capacidade_caminhao(peso_total_pedido_kg, capacidade_maxima_veiculo_kg):
    """
    Verifica se o peso total cabe na capacidade do caminhão.
    Args:
        peso_total_pedido_kg (float): O peso total do pedido.
        capacidade_maxima_veiculo_kg (float): A capacidade maxima que pode ser transportada pelo caminhão.
    Returns:
        bool: True se couber, False se exceder.
    """
    if type(peso_total_pedido_kg) != int and type(peso_total_pedido_kg) != float:
        raise ValueError("PESO deve ser um número")

    if type(capacidade_maxima_veiculo_kg) != int and type(capacidade_maxima_veiculo_kg) != float:
        raise ValueError("CAPACIDADE deve ser um número")

    if peso_total_pedido_kg <= 0 or capacidade_maxima_veiculo_kg <= 0:
        raise ValueError("Digite um número maior que zero")
    
    return capacidade_maxima_veiculo_kg >= peso_total_pedido_kg