# 1 - Bibliotecas (libraries)
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

# Set Chrome preferences to disable password warnings
prefs = {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False,
    "profile.password_manager_leak_detection": False  # Optional: disables breach warnings
}

options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", prefs)
options.add_argument("--incognito")


# 2 - Classe (Opcional)

class TestProdutos():

    # 2.1 - Atributos (dentro da classe)
    url = "https://www.saucedemo.com"                     # url do site alvo

    # 2.2 - Funcoes e methodos (dentro da classe)
    def setup_method(self, method):                        # metodo de inicializacao dos testes
        self.driver = webdriver.Chrome(options=options)                     # instanciar o objeto do selenium webdriver como chrome
        self.driver.implicitly_wait(10)                    # define o tempo de espera padrao por elemento em 10 segundos
   # a espera vale para todo script

    def teardown_method(self, method):                     # metodo de finalizacao dos testes
        self.driver.quit()                                 # encerra / destroi o objeto do selenium webdriver da memoria

    def test_selecionar_produto(self):                                                     # metodo de teste
        self.driver.get(self.url)                                                          # abre o navegador
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")            # escreve no campo user_name
        self.driver.find_element(By.NAME, "password").send_keys("secret_sauce")            # escreve no campo password  
        self.driver.find_element(By.CSS_SELECTOR, "input.submit-button.btn_action").click() # click botao login

        # transicao de pagina
        
        assert self.driver.find_element(By.CSS_SELECTOR, ".title").text == "Products"      # confirma se esta escrito Products no elemento
        assert self.driver.find_element(By.ID, "item_4_title_link").text == "Sauce Labs Backpack"  # confirma se e a mochila
        # confirma o preco da mochila
        assert self.driver.find_element(By.CSS_SELECTOR, ".inventory_item:nth-child(1) .inventory_item_price").text == "$29.99"

