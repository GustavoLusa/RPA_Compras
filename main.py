import pandas as pd
import os
from automacao import ImportaCompras
from login import realizar_login
from adicionaProdutos import adiciona_e_check, gerar_relatorio
from tiraPrint import capturar_comprovante

"""
PROJETO: Automação de Compras RPA
CRIADOR: Gustavo Lusa Owsiany
SOLICITANTE: Sicredi Soma
DATA: 16/12/2025
OBJETIVO: Automatizar a compra de produtos no portal SauceDemo a partir de um arquivo .csv.
"""

if __name__ == "__main__":
    """
    Ponto de entrada do sistema. Gerencia a localização do arquivo de entrada 
    e orquestra as chamadas de login, processamento e finalização.
    """
    caminhos_possiveis = [
        r"planilhasCompras/produtos_compra.csv",
        os.path.join(os.path.expanduser("~"), "Downloads", "produtos_compra.csv"),
        "produtos_compra.csv"
    ]
    caminho_csv = next((p for p in caminhos_possiveis if os.path.exists(p)), None)
    
    #Se deseja ver o bot trabalhando setar headless=False
    bot = ImportaCompras(headless=False)
    
    try:
        if caminho_csv:
            print(f"📂 Lendo arquivo: {caminho_csv}")
            dados = pd.read_csv(caminho_csv)
            
            realizar_login(bot, "https://www.saucedemo.com/", "standard_user", "secret_sauce")
            
            dados_comprador = {'nome': 'Comprador', 'sobrenome': 'Teste', 'cep': '12345678'}
            adiciona_e_check(bot, dados["Produto"].tolist(), dados_comprador)
            
            capturar_comprovante(bot, "Comprovante")
            print("✅ Processo de compra concluído!")
        else:
            print("❌ Arquivo produtos_compra.csv não encontrado nos locais padrão.")
            
    except Exception as e:
        print(f"❌ Erro na execução: {e}")
        
    finally:

        # Garante que o relatório seja salvo e o navegador fechado, mesmo em caso de erro
        gerar_relatorio(bot)
        bot.fechar()