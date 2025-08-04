# 1- Bibliotecas / imports
import time
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given(u'que acesso o site Sauce Demo')
def step_impl(context):
    # setup / inicializacao
    context.driver = webdriver.Chrome()                 # instanciar o objeto do selenium webdriver especializado para o chrome
    context.driver.maximize_window()                    # maximizar a janela do navegador
    context.driver.implicitly_wait(10)                   # esperar ate 10 segundos por qualquer elemento
    # passo em si
    context.driver.get("https://www.saucedemo.com")     # abrir o navegador no endereco do site alvo

# Preencher com usuario e senha
@when(u'preencho os campos de login com usuario {usuario} e senha {senha}')
def step_impl(context, usuario, senha):
    context.driver.find_element(By.ID, "user-name").send_keys(usuario)      # preencher o usuario
    context.driver.find_element(By.ID, "password").send_keys(senha)         # preencher a senha
    context.driver.find_element(By.ID, "login-button").click()              # clicar no botao login

# Preencher com usuario em branco e senha
@when(u'preencho os campos de login com usuario  e senha {senha}')
def step_impl(context, senha):
    # nao preenche o usuario
    context.driver.find_element(By.ID, "password").send_keys(senha)         # preencher a senha
    context.driver.find_element(By.ID, "login-button").click()              # clicar no botao login

# Preencher com usuario, mas deixar a senha em branco
@when(u'preencho os campos de login com usuario {usuario} e senha ')
def step_impl(context, usuario):
    context.driver.find_element(By.ID, "user-name").send_keys(usuario)      # preencher o usuario
    # nao preencho a senha
    context.driver.find_element(By.ID, "login-button").click()              # clicar no botao login

# Clica no botao de login sem ter preenchido o usuario e a senha
@when(u'preencho os campos de login com usuario  e senha ')
def step_impl(context):
    # nao preencho o usuario
    # nao preencho a senha
    context.driver.find_element(By.ID, "login-button").click()              # clicar no botao login

# Preencher com usuario e senha atraves da decisao (IF)
@when(u'digito os campos de login com usuario {usuario} e senha {senha} com IF')
def step_impl(context, usuario, senha):
    if usuario != '<branco>':
        context.driver.find_element(By.ID, "user-name").send_keys(usuario)      # preencher o usuario
        # se o usuario estiver em <branco> nao ha acao de preenchimento
    if senha != '<branco>':
        context.driver.find_element(By.ID, "password").send_keys(senha)         # preencher a senha
        # se a senha estiver em <branco> nao ha acao de preenchimento

    context.driver.find_element(By.ID, "login-button").click()              # clicar no botao login

@then(u'sou direcionado para pagina Home')
def step_impl(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".title").text == "Products"
    time.sleep(2) # espera por dois segundos - remover depois = alfinete

    # teardown / encerramento
    context.driver.quit()

@then(u'exibe a mensagem de erro no login')
def step_impl(context):
    # validar a mensagem de error
    assert context.driver.find_element(By.CSS_SELECTOR, "h3").text == "Epic sadface: Username and password do not match any user in this service"

    # teardown / encerramento
    context.driver.quit()

# Verifica a mensagem para o Scenario Outline
@then(u'exibe a {mensagem} de erro no login')
def step_impl(context, mensagem):
    # validar a mensagem de error
    assert context.driver.find_element(By.CSS_SELECTOR, "h3").text == mensagem

    # teardown / encerramento
    context.driver.quit()
