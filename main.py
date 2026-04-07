from app.acabamento_pintura import *
from app.alvenaria_estrutura import *
from app.logística_orcamento import *

def iniciar_sistema():
    print("=" * 50)
    print("   BEM-VINDO À CALCULADORA DE MATERIAIS DE OBRA")
    print("=" * 50)

    while True:
        print("\n" + "-" * 30)
        print("MENU PRINCIPAL:")
        print("1 - Calcular Área (m²)")
        print("2 - Calcular Tijolos por Parede")
        print("3 - Calcular Volume de Concreto (m³)")
        print("4 - Calcular Sacos de Cimento")
        print("5 - Calcular Caixas de Piso")
        print("6 - Calcular Rejunte (kg)")
        print("7 - Calcular Litros de Tinta")
        print("8 - Calcular Frete de Entrega")
        print("9 - Verificar Capacidade do Caminhão")
        print("0 - Sair do Sistema")
        print("-" * 30)

        opcao = input("Escolha a opção desejada (0 a 9): ")

        if opcao == '0':
            print("\nEncerrando o sistema. Muito obrigado!")
            break

        try:
            # === ALVENARIA E ESTRUTURA ===
            if opcao == '1':
                alt = float(input("Digite a altura em metros: "))
                comp = float(input("Digite o comprimento em metros: "))
                resultado = calcular_area_em_m2(alt, comp)
                print(f">>> RESULTADO: A área total é de {resultado} m²")

            elif opcao == '2':
                area_par = float(input("Digite a área da parede (m²): "))
                area_tij = float(input("Digite a área do tijolo (m²): "))
                resultado = calcular_tijolos_por_parede(area_par, area_tij)
                print(f">>> RESULTADO: Serão necessários {resultado} tijolos.")

            elif opcao == '3':
                larg = float(input("Digite a largura (m): "))
                comp = float(input("Digite o comprimento (m): "))
                esp = float(input("Digite a espessura (m): "))
                resultado = calcular_volume_concreto(larg, comp, esp)
                print(f">>> RESULTADO: O volume é de {resultado} m³")

            elif opcao == '4':
                vol = float(input("Digite o volume de concreto (m³): "))
                rend = float(input("Digite o rendimento do saco de cimento (m³): "))
                resultado = calcular_sacos_cimento(vol, rend)
                print(f">>> RESULTADO: Serão necessários {resultado} sacos de cimento.")

            # === ACABAMENTO E PINTURA ===
            elif opcao == '5':
                area = float(input("Digite a área do ambiente (m²): "))
                rend = float(input("Digite o rendimento da caixa de piso (m²): "))
                resultado = calcular_caixas_piso(area, rend)
                print(f">>> RESULTADO: Serão necessárias {resultado} caixas de piso.")

            elif opcao == '6':
                area = float(input("Digite a área de revestimento (m²): "))
                cons = float(input("Digite o consumo de rejunte (kg/m²): "))
                resultado = calcular_rejunte_necessario(area, cons)
                print(f">>> RESULTADO: Serão necessários {resultado} kg de rejunte.")

            elif opcao == '7':
                area = float(input("Digite a área de pintura (m²): "))
                rend = float(input("Digite o rendimento da lata (m²): "))
                demaos = int(input("Digite a quantidade de demãos: "))
                resultado = calcular_litros_tinta(area, rend, demaos)
                print(f">>> RESULTADO: Serão necessárias {resultado} latas de tinta.")

            # === LOGÍSTICA E ORÇAMENTO ===
            elif opcao == '8':
                dist = float(input("Digite a distância (km): "))
                peso = float(input("Digite o peso da carga (kg): "))
                resultado = calcular_frete_entrega(dist, peso)
                print(f">>> RESULTADO: O valor do frete é R$ {resultado}")

            elif opcao == '9':
                peso = float(input("Digite o peso do pedido (kg): "))
                cap = float(input("Digite a capacidade do caminhão (kg): "))
                resultado = capacidade_caminhao(peso, cap)
                if resultado:
                    print(">>> RESULTADO: O caminhão SUPORTA a carga.")
                else:
                    print(">>> RESULTADO: O caminhão NÃO SUPORTA a carga.")

            else:
                print("Opção inválida! Por favor, digite um número de 0 a 9.")

        # Esse bloco captura as validações criadas na calculadora
        except ValueError as e:
            print(f"\n[!] ERRO DE VALIDAÇÃO: {e}")
            print("Tente novamente digitando valores válidos.")

iniciar_sistema()