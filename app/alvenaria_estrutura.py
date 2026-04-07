# ==========================================
# MÓDULO: ALVENARIA E ESTRUTURA
# Responsáveis: Nicolas Cleik ; Ana Clara ;
# ==========================================
import math
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
