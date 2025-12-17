import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

class ImportaCompras:
    """
    Classe responsável pela infraestrutura da automação.
    Gerencia a configuração do WebDriver, define diretórios de saída e 
    ajusta parâmetros do navegador para garantir a estabilidade da execução.
    """
    def __init__(self, headless=True):
        """
        Inicializa o bot configurando o ambiente do Chrome.
        Define resolução padrão, desativa pop-ups de segurança e 
        configura esperas explícitas para evitar falhas de carregamento.
        """
        if not os.path.exists("comprovantes"):
            os.makedirs("comprovantes")

        chrome_options = Options()
        if headless:
            chrome_options.add_argument("--headless=new")
        
        # Configurações para garantir que os elementos não mudem de posição e evitar bloqueios
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_argument("--disable-password-leak-detection")
        
        # Preferências para desativar gerenciadores de senhas e notificações nativas
        prefs = {
            "credentials_enable_service": False, 
            "profile.password_manager_enabled": False,
            "profile.default_content_setting_values.notifications": 2,
            "autofill.profile_enabled": False
        }
        chrome_options.add_experimental_option("prefs", prefs)

        # Instalação automática do driver compatível com a versão do navegador
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.wait = WebDriverWait(self.driver, 20)
        self.resultados_log = []

    def fechar(self):
        """Encerra a sessão do navegador e libera recursos do sistema."""
        self.driver.quit()