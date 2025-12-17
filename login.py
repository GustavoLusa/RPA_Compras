from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def realizar_login(bot, url, user, password):
    """
    Realiza a autenticação no portal informada, preenchendo os campos 
    de usuário e senha e executando o clique de acesso via JavaScript.
    """
    bot.driver.get(url)
    bot.wait.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys(user)
    bot.driver.find_element(By.ID, "password").send_keys(password)
    
    btn_login = bot.driver.find_element(By.ID, "login-button")
    bot.driver.execute_script("arguments[0].click();", btn_login)