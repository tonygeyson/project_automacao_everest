import time
import conftest
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class VerPaginaInicial(BasePage):
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

    def ver_pagina_inicial(self):
        # Valida de se os produtos estão na página
        mensagem_produto_1 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[@class='inventory_item_name '][contains(.,'Sauce Labs Backpack')]"))).text
        assert mensagem_produto_1 == "Sauce Labs Backpack"
        print("Produto número 1 está cadastrado!")

        mensagem_produto_2 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[@class='inventory_item_name '][contains(.,'Sauce Labs Bike Light')]"))).text
        assert mensagem_produto_2 == "Sauce Labs Bike Light"
        print("Produto número 2 está cadastrado!")

        mensagem_produto_3 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[@class='inventory_item_name '][contains(.,'Sauce Labs Bolt T-Shirt')]"))).text
        assert mensagem_produto_3 == "Sauce Labs Bolt T-Shirt"
        print("Produto número 3 está cadastrado!")

        mensagem_produto_4 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[@class='inventory_item_name '][contains(.,'Sauce Labs Fleece Jacket')]"))).text
        assert mensagem_produto_4 == "Sauce Labs Fleece Jacket"
        print("Produto número 4 está cadastrado!")

        mensagem_produto_5 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[@class='inventory_item_name '][contains(.,'Sauce Labs Onesie')]"))).text
        assert mensagem_produto_5 == "Sauce Labs Onesie"
        print("Produto número 5 está cadastrado!")

        mensagem_produto_6 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH,
                 "//div[@class='inventory_item_name '][contains(.,'Test.allTheThings() T-Shirt (Red)')]"))).text
        assert mensagem_produto_6 == "Test.allTheThings() T-Shirt (Red)"
        print("Produto número 6 está cadastrado!")
        time.sleep(2)

        # -------------------------------------------------------------------------------------------- #
        # -------------------------------------------------------------------------------------------- #

        # Faz o processo de saída da página
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(@id,'react-burger-menu-btn')]"))).click()

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "*[data-test=\"logout-sidebar-link\"]"))).click()
        time.sleep(1)

        # Certifica que o elemento foi encontrado.
        mensagem_elemento_existe_sucesso = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//h4[contains(.,'Accepted usernames are:')]"))).text
        assert mensagem_elemento_existe_sucesso == "Accepted usernames are:"
        print("Usuário saiu da página.")

