import pandas as pd
import os
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def adiciona_e_check(bot, lista_produtos, dados_comprador):
    """
    Percorre a lista de produtos fornecida, localiza os itens no site via XPath 
    dinâmico e os adiciona ao carrinho. Após a seleção, realiza o fluxo completo 
    de checkout utilizando os dados do comprador.
    """
    for nome in lista_produtos:
        try:
            xpath = f"//div[text()='{nome}']/ancestor::div[@class='inventory_item']//button"
            btn = bot.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            bot.driver.execute_script("arguments[0].click();", btn)
            registrar_log(bot, nome, "sucesso")
        except Exception as e:
            registrar_log(bot, nome, "erro", str(e))

    # Navegação para o checkout e preenchimento de informações de entrega
    bot.driver.execute_script("arguments[0].click();", bot.driver.find_element(By.CLASS_NAME, "shopping_cart_link"))
    bot.wait.until(EC.presence_of_element_located((By.ID, "checkout"))).click()

    bot.wait.until(EC.visibility_of_element_located((By.ID, "first-name"))).send_keys(dados_comprador['nome'])
    bot.driver.find_element(By.ID, "last-name").send_keys(dados_comprador['sobrenome'])
    bot.driver.find_element(By.ID, "postal-code").send_keys(dados_comprador['cep'])
    
    bot.driver.execute_script("arguments[0].click();", bot.driver.find_element(By.ID, "continue"))
    
    # Finalização do pedido com scroll para garantir a visibilidade do botão
    btn_finish = bot.wait.until(EC.presence_of_element_located((By.ID, "finish")))
    bot.driver.execute_script("arguments[0].scrollIntoView(true);", btn_finish)
    bot.driver.execute_script("arguments[0].click();", btn_finish)

def registrar_log(bot, produto, status, erro=""):
    """Armazena internamente os eventos de cada tentativa de compra para o relatório."""
    bot.resultados_log.append({
        "produto": produto, 
        "status": status, 
        "motivo_erro": erro, 
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

def gerar_relatorio(bot):
    """
    Compila os logs da execução e gera um arquivo .csv na pasta 'relatorios'.
    Utiliza timestamp no nome do arquivo para manter um histórico único por execução.
    """
    pasta_relatorios = "relatorios"
    if not os.path.exists(pasta_relatorios):
        os.makedirs(pasta_relatorios)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    nome_arquivo = f"relatorio_compras_{timestamp}.csv"
    caminho_completo = os.path.join(pasta_relatorios, nome_arquivo)

    df = pd.DataFrame(bot.resultados_log)
    df.to_csv(caminho_completo, index=False)
    print(f"📊 Relatório salvo em: {caminho_completo}")