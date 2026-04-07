# ==========================================
# MÓDULO: ALVENARIA E ESTRUTURA
# Responsáveis: Nicolas Cleik ; Ana Clara ;
# ==========================================

def calcular_area_em_m2(altura, comprimento):
    """
    Calcula a área total de uma superfície em metros quadrados (m²).

    Parâmetros:
        altura (float): A medida da altura da superfície.
        comprimento (float): A medida do comprimento da superfície.

    Retorno:
        float: O resultado da multiplicação da altura pelo comprimento.
    """

    if type(altura) != int and type(altura) != float:
        raise ValueError("ALTURA deve ser um número")

    if type(comprimento) != int and type(comprimento) != float:
        raise ValueError("COMPRIMENTO deve ser um número")

    if altura <= 0 or comprimento <= 0:
        raise ValueError("Os valores de ALTURA e COMPRIMENTO devem ser maiores que zero")

    area_m2 = altura * comprimento

    return area_m2

# ------------------------------------------

def calcular_tijolos_por_parede(area_parede_m2, area_tijolo_m2):
    """
    Calcula a quantidade estimada de tijolos necessários para preencher uma parede.

    Parâmetros:
        area_parede_m2 (float): A área total da parede em metros quadrados.
        area_tijolo_m2 (float): A área que um único tijolo ocupa em metros quadrados.

    Retorno:
        float: A quantidade de tijolos (blocos) necessários, arredondada para duas casas decimais.
    """
    
    if type(area_parede_m2) != int and type(area_parede_m2) != float:
        raise ValueError("AREA_PAREDE deve ser um número")

    if type(area_tijolo_m2) != int and type(area_tijolo_m2) != float:
        raise ValueError("AREA_TIJOLO deve ser um número")

    if area_parede_m2 <= 0 or area_tijolo_m2 <= 0:
        raise ValueError("Os valores de AREA_PAREDE e AREA_TIJO devem ser maiores que zero! A função 'calcular_area_em_m2(altura, comprimento)' vai te ajudar entregando o resultado final em m2")

    quantidade_de_blocos = round((area_parede_m2 / area_tijolo_m2), 2)

    return quantidade_de_blocos

# ------------------------------------------

def calcular_volume_concreto(largura_m, comprimento_m, espessura_m):
    #Calcula o volume total de uma superfície em m³
    
    """
    Parâmetros:
    largura_m: largura em metros
    comprimento_m: comprimento em metros
    espessura_m: espessura em metros
    volume: retorno do volume da superfície em m³
    """

    if largura_m <= 0 or comprimento_m <= 0 or espessura_m <= 0:
        raise ValueError('Nenhum dos parâmetros deve ser menor ou igual a 0')
    
    volume = largura_m * comprimento_m * espessura_m
    #Calcula e retorna o volume
    return volume

# ------------------------------------------

def calcular_sacos_cimento(volume_concreto_m3, rendimento_saco_m3):
    #Calcula quantidade de sacos de cimento que serão ultilizados na obra
    
    """
    Parâmetros:
    volume_concreto_m3: volume da superfície em m³
    rendimento_saco_m3: rendimento de um saco de cimento por m³
    qnt_sacos: retorna a quantidade de sacos necessitados
    """

    if volume_concreto_m3 <= 0 or rendimento_saco_m3 <= 0:
        raise ValueError('Nenhum dos parâmetros deve ser menor ou igual a 0')
    
    qnt_sacos = math.ceil(volume_concreto_m3 / rendimento_saco_m3)
    #Calcula e retorna quantidade de sacos necessários
    return qnt_sacos

# ==========================================
# MÓDULO: ACABAMENTO E PINTURA
# Responsáveis: Pedro Gustavo;
# ==========================================

import math

def calcular_caixas_piso(area_ambiente_m2, rendimento_caixa_m2):
    # Calcula a quantidade de caixas de piso necessárias para um ambiente.
    
    # Parâmetros:
    # area_ambiente_m2: A área do ambiente em metros quadrados.
    # rendimento_caixa_m2: Quantos metros quadrados uma caixa cobre
    if rendimento_caixa_m2 <= 0:
        raise ValueError("Erro: O rendimento da caixa deve ser maior que zero.")
        
    # Divide a área exata pelo rendimento e arredonda para cima
    qtd_caixas = math.ceil(area_ambiente_m2 / rendimento_caixa_m2)
    
    return qtd_caixas

def calcular_rejunte_necessario(area_revestimento_m2, consumo_rejunte_kg_m2):
    # Calcula a quantidade de rejunte necessária para um ambiente.
    
    # Parâmetros:
    # area_revestimento_m2 : A área total de revestimento em metros quadrados.
    # consumo_rejunte_kg_m2 : Consumo de rejunte em kg por metro quadrado.
    # tamanho_pacote_kg : O peso de cada pacote de rejunte em kg (padrão é 1kg).
    if consumo_rejunte_kg_m2 <= 0:
        raise ValueError("Erro: O consumo de rejunte deve ser maior que zero.")
        
    # Calcula a quantidade total exata em kg (área * consumo)
    total_kg = area_revestimento_m2 * consumo_rejunte_kg_m2
    
    return total_kg
   

def calcular_litros_tinta(area_pintura_m2, rendimento_lata_m2, quantidade_demaos):
    # Calcula a quantidade de latas/litros de tinta necessárias.
    
    # Parâmetros:
    # area_pintura_m2: A área total a ser pintada em metros quadrados.
    # rendimento_lata_m2: Quantos metros quadrados a embalagem de tinta cobre por demão.
    # quantidade_demaos: Número de demãos (camadas) que serão aplicadas.
    if rendimento_lata_m2 <= 0:
        raise ValueError("Erro: O rendimento da lata deve ser maior que zero.")
        
    # Multiplica a área pelo número de demãos para saber a área total de cobertura exigida
    area_total_cobertura = area_pintura_m2 * quantidade_demaos
    
    # Divide a área total de cobertura pelo rendimento da lata e arredonda para cima
    qtd_latas = math.ceil(area_total_cobertura / rendimento_lata_m2)
    
    return qtd_latas

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
    # Validação de tipo (seguindo o padrão do Nicolas/Ana Clara)
    if type(distancia_km) != int and type(distancia_km) != float:
        raise ValueError("DISTANCIA deve ser um número")

    if type(peso_carga_kg) != int and type(peso_carga_kg) != float:
        raise ValueError("PESO deve ser um número")

    # Validação de valores positivos
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
    # Validação de tipo
    if type(peso_total_pedido_kg) != int and type(peso_total_pedido_kg) != float:
        raise ValueError("PESO deve ser um número")

    if type(capacidade_maxima_veiculo_kg) != int and type(capacidade_maxima_veiculo_kg) != float:
        raise ValueError("CAPACIDADE deve ser um número")

    # Validação de valores positivos
    if peso_total_pedido_kg <= 0 or capacidade_maxima_veiculo_kg <= 0:
        raise ValueError("Digite um número maior que zero")
    
    return capacidade_maxima_veiculo_kg >= peso_total_pedido_kg