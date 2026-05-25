import random
import matplotlib.pyplot as plt

def regressao_linear() -> None:
# Dados simulados
    vento = [0, 30, 45, 60,65,75,80,85,95,100]
    energia_gerada = [20, 25, 30, 35, 40,50,65,85,95,100]

    # Médias
    media_x = sum(vento) / len(vento)
    media_y = sum(energia_gerada) / len(energia_gerada)

    numerador = 0
    denominador = 0

    # Cálculo da regressão
    for i in range(len(vento)):
        numerador += (vento[i] - media_x) * (energia_gerada[i] - media_y)
        denominador += (vento[i] - media_x) ** 2

        # Coeficientes da reta
    a = numerador / denominador
    b = media_y - a * media_x

    # Novo vento aleatório
    novo_vento = random.randint(50, 100)

    # Previsão
    previsao = a * novo_vento + b

    print("\n===== PREVISÃO ENERGÉTICA =====")
    print(f"Velocidade do vento: {media_y} km/h")
    print(f"Energia prevista: {media_x:.2f}%")

    # =========================
    # LINHA DA REGRESSÃO
    # =========================

    linha_x = vento
    linha_y = []

    for x in linha_x:
        y = a * x + b
        linha_y.append(y)

        # =========================
        # GRÁFICO
        # =========================

    plt.scatter(vento, energia_gerada, s=100, color = "deepskyblue", edgecolors = "black")
    plt.plot(linha_x, linha_y, color = "limegreen", linewidth=3)
    plt.scatter(novo_vento, previsao, s=150, color = "red", edgecolors = "black")

    plt.title("Previsão de Energia Eólica", fontsize =18, fontweight = "bold")
    plt.xlabel("Velocidade do vento", fontsize = 12)
    plt.ylabel("Energia Gerada", fontsize = 12)

    plt.grid(True, linestyle="--", alpha = 0.5, color = "black")
    ax = plt.gca()
    ax.set_facecolor("lightblue")
    plt.tight_layout()

    plt.show()