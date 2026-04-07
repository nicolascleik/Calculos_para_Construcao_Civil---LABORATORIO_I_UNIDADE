
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
