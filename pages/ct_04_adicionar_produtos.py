import time
import conftest
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AdicionarProdutos(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.username_field = (By.ID, "username")
        self.password_field = (By.ID, "password")
        self.login_button = (By.CSS_SELECTOR, "[data-qa='login-submit']")
        self.driver.implicitly_wait(10)

    def fazer_login(self, usuario, senha):
        self.escrever(self.username_field, usuario)
        self.escrever(self.password_field, senha)
        self.clicar(self.login_button)
        self.driver.implicitly_wait(10)

    def adicionar_produtos(self):
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
        time.sleep(1)

        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"shopping-cart-link\"]").click()
        time.sleep(1)

        # VERIFICA SE O PRODUTO ESTÁ NO CARRINHO
        self.driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge'][contains(.,'1')]")
        mensagem_produto_adicionado_ao_carrinho = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[@class='shopping_cart_badge'][contains(.,'1')]"))).text
        assert mensagem_produto_adicionado_ao_carrinho == "1"
        print("Produto adicionado ao carrinho.")


        # VERIFICA SE O PRODUTO ESTÁ NA PÁGINA
        mensagem_produto_na_pagina = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[@class='inventory_item_name'][contains(.,'Sauce Labs Backpack')]"))).text
        assert mensagem_produto_na_pagina == "Sauce Labs Backpack"
        print("Produto esta na página.")

        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"continue-shopping\"]").click()
        time.sleep(1)

