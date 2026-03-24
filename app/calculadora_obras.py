# ==========================================
# MÓDULO: ALVENARIA E ESTRUTURA
# Responsáveis: Nicolas Cleik ; SEU_NOME
# ==========================================

def calcular_area_em_m2(altura, comprimento):
    try:
        altura = float(altura)
        comprimento = float(comprimento)
    except ValueError:
        raise TypeError("O valor informado deve ser um número válido e não uma letra.")

    if altura <= 0 or comprimento <= 0:
        raise ValueError("Os valores de ALTURA e COMPRIMENTO devem ser maiores que zero")

    area_m2 = altura * comprimento

    return area_m2

def calcular_tijolos_por_parede(area_parede_m2, area_tijolo_m2):
    try:
        area_parede_m2 = float(area_parede_m2)
        area_tijolo_m2 = float(area_tijolo_m2)
    except ValueError:
        raise TypeError("O valor informado deve ser um número válido e não uma letra.")

    if area_parede_m2 <= 0 or area_tijolo_m2 <= 0:
        raise ValueError("Os valores de AREA_PAREDE e AREA_TIJO devem ser maiores que zero! A função 'calcular_area_em_m2(altura, comprimento)' vai te ajudar entregando o resultado final em m2")


    quantidade_de_blocos = round((area_parede_m2 / area_tijolo_m2), 2)

    return quantidade_de_blocos

# ==========================================
# MÓDULO: ACABAMENTO E PINTURA
# Responsáveis: SEU_NOME
# ==========================================,

# ==========================================
# MÓDULO: LOGISTICA E ORÇAMENTO
# Responsáveis: SEU_NOME
# ==========================================