import os
from datetime import datetime

def capturar_comprovante(bot, prefixo):
    """
    Captura um screenshot da tela final para servir como comprovante do processo.
    Utiliza um identificador de tempo para garantir nomes únicos e evitar sobreposição.
    """
    timestamp = datetime.now().strftime("%H%M%S")
    nome_arquivo = f"{prefixo}_{timestamp}.png"
    
    caminho = os.path.join("comprovantes", nome_arquivo)
    bot.driver.save_screenshot(caminho)
    print(f"📸 Comprovante salvo: {caminho}")