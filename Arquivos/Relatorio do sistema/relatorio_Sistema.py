import pandas as pd
from tabulate import tabulate
def relatorio_Sistema(colonia):
    print(f"""
    ============RElATORIO DA COLONIA ============
    """)
    consumo = colonia["energia_solar"]["Consumo"]
    energia = colonia["energia_solar"]["energia"]
    combustivel = colonia["energia_solar"]["Combustivel"]

    tabela2 = pd.DataFrame({
        "Energia Atual (%)": [energia],
        "Consumo Atual (%)": [consumo],
        "Combustivel (%)": [combustivel]
    })
    print(tabulate(tabela2, headers='keys', tablefmt='fancy_grid'))
    print("\n===== RELATORIO DA COLONIA =====\n")
    print(f"Energia: {energia}%")
    print(f"Consumo: {consumo}%")
    print(f"Combustivel: {combustivel}%")

    print("\nSTATUS:")
#Regras Do Sistema
    if consumo > 70 and energia < 40:

        print("🚨 Sistema em estado crítico")
        print("⚠ Laboratório desligado")
        print("⚠ Iluminação desligada")
        print("🔋 Eficiência energética: BAIXA")

    elif consumo > 50 and energia < 60:

        print("⚠ Sistema em alerta moderado")
        print("🔋 Eficiência energética: MÉDIA")

    elif energia > 80 and consumo < 40:

        print("✅ Sistema Estável")
        print("🚀 Eficiência energética: EXCELENTE")
        print("🔋 Energia excedente disponível")

    else:

        print("✅ Sistema Estável")
        print("🚀 Eficiência energética: BOA")

