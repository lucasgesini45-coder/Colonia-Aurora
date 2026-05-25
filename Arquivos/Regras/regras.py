import pandas as pd
import time

def regras_Do_sistema(colonia):


    consumo = colonia["energia_solar"]["Consumo"]
    energia = colonia["energia_solar"]["energia"]
    combustivel = colonia["energia_solar"]["Combustivel"]

    print(f"\nEnergia Atual: {energia}%")
    print(f"Consumo Atual: {consumo}%")
    print(f"Combustível: {combustivel}%")

    # ==========================
    # ALERTA CRÍTICO
    # ==========================

    if consumo > 70 and energia < 40:

        print("\n🚨 CONSUMO CRÍTICO 🚨")
        print("Ativando modo economia de energia...")

        time.sleep(1)

        # Desligando sistemas não essenciais
        colonia["Laboratorio"]["Status"] = "OFF"
        colonia["Iluminaçao"]["Status"] = "OFF"

        print("\nSistemas não essenciais desligados!")

        dados = [
            ["Laboratorio", "OFF"],
            ["Iluminaçao", "OFF"]
        ]

        tabela = pd.DataFrame(
            dados,
            columns=["Sistema", "Status"]
        )

        print("\n")
        print(tabela)

    # ==========================
    # ALERTA MODERADO
    # ==========================
    elif consumo > 50 and energia < 60:

        print("\n⚠ ALERTA MODERADO ⚠")
        print("Reduzindo consumo energético...")
        time.sleep(1)

    # ==========================
    # SISTEMA ESTÁVEL
    # ==========================
    else:
        print("\n✅ Energia Estável")