# RPA de Compras - Teste Técnico
Este projeto é uma automação (RPA) desenvolvida em **Python** utilizando **Selenium** para realizar o fluxo de compra no site *SauceDemo*.

## 🚀Funcionalidades
**Login**: Autenticação no portal.
**Importação de Dados**: Lista os produtos com base em um arquivo `.csv`.
**Busca automática**: Localização da planilha (Pasta Local ou Downloads).
**Captura de Evidências**: Captura de screenshots para comprovação.
**Relatórios**: Geração de logs em CSV detalhando o sucesso ou erro de cada produto.

## 🛠️Decisões Técnicas
**Padrão**: Código dividido em módulos específicos para facilitar a manutenção e entendimento.
**Configuração do navegador**: Configurações do Chrome para desativar alertas de "Mude sua senha" e notificações nativas.
**Waits Explícitos**: Implementação de `WebDriverWait` em vez de pausas fixas.

## 📦Como Configurar e Executar
**Requisitos:**
**Python 3.12.0**: [Download Versão 3.12.0 x64](https://www.python.org/ftp/python/3.12.0/python-3.12 0-amd64.exe)
**Google Chrome** instalado. 
**Configuração e execução:**
   ```PowerShell
# Criação do ambiente virtual
python -m venv venv
# Instalação das bibliotecas necessárias
pip install -r requirements.txt
# Liberação de execução de scripts (caso o Windows bloqueie)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
# Ativação do ambiente
.\venv\Scripts\activate
#Excutando
python main.py

## 📂Organização de Arquivos 
planilhasCompras/: Pasta recomendada para colocar o arquivo produtos_compra.csv.
Comprovantes/: Armazena automaticamente os prints de sucesso/erro.
relatorios/: Armazena os arquivos CSV gerados após cada execução.