# Importação de Classe
import time
# importaçao dos arquivos
import sistema_Colonia as sc
import regras as rds
import regressao_linear as rl

                            # ==================
                            # PAINEL DE ENTRADA
                            # ==================
nome = input(f"""
Olá Seja bem Vindo Ao Sistema De Colonia Da Nave!🚀
\nInsira seu Nome De Usuario Para Acessar O painel de Controle:

""").upper()
print(f"""
======================================================
            SEJA BEM VINDO TRIPULANTE: {nome}
======================================================
""")
# =============================================
# Inicialização do sistema e Laço de Repetição
# =============================================

while True:

    try:
        opcao = int(input("""
    Oque Deseja Iniciar Primeiro?
    
0- Sair ❌
1- Verificar Status Do Sistema 🤖
2- Mostrar Grafico 📈
3- Mostrar Sistemas De Nave 🔧
Escolha: 
"""))

    except:
        print("opçao invalida")
        continue

    match opcao:

        case 1:
            print("Iniciando Verificaçao Do Sistema...")
            print("analizando Dados...")
            time.sleep(0.5)
            colonia = sc.sistema_colonia()
            print()
            regras = rds.regras_Do_sistema(colonia)
            print(regras)
            input("\nPressione ENTER para Voltar Ao menu...")
        case 2:
        # =========================
        # REGRESSÃO LINEAR
        # =========================
            print("\nIniciando previsão de energia...")
            time.sleep(1.5)

            rl.regressao_linear()

            input("\nPressione ENTER para Voltar Ao menu...")
        case 3:
         print("hello world")
        case 0:
            print("Encerrando sistema...")
            break

        case _:
            print("Opção inválida!")
            break