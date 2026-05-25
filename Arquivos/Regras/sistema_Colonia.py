import pandas as pd
import random
def  sistema_colonia():
    colonia = {

        "energia_solar": {
            "energia": random.randint(30, 100),
            "Consumo": random.randint(40, 100),
            "Combustivel": random.randint(65, 100),
        },
        "Suporte_vida": {
            "suporte vida": True,
            "status": "ON",
            "Consumo de Energia":random.randint(0, 100),
        },

        "Comunicaçao": {
            "comunicacao": True,
            "Status": "ON",
            "Consumo De Energia":random.randint(0, 100),
        },
        "Iluminaçao": {
            "iluminacao_externa": True,
            "Status": "ON",
            "Consumo de Energia": random.randint(0, 100),
        },
        "Laboratorio": {
            "laboratorio": True,
            "Status": "ON",
            "Consumo De Energia": random.randint(25,50)
        }
    }
    dados = [
        ["Energia Solar", random.randint(0,100), "ON"],
        ["Suporte Vida", random.randint(0,100), "ON"],
        ["Comunicação", random.randint(0,100), "ON"],
        ["Iluminação", random.randint(0,100), "ON"],
        ["Laboratório", random.randint(25,50), "ON"]
    ]

    tabela = pd.DataFrame(
        dados,
        columns=["Sistema", "Consumo De Energia", "Status"]
    )
    print(tabela)
    return colonia