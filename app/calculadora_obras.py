def calcular_area_em_m2(altura, comprimento):
    area_m2 = altura * comprimento

    return area_m2

def calcular_tijolos_por_parede(area_parede_m2, area_tijolo_m2):
    quantidade_de_blocos = round((area_parede_m2 / area_tijolo_m2), 2)

    return quantidade_de_blocos
