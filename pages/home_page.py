import conftest
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):

    def __init__(self):
        self.driver = conftest.driver

        # Verificar se o título da página inicial, existe na página
        self.titulo_pagina = (By.XPATH, "//a[@data-testid='home'][contains(.,'Home')]")

    def verificar_login_com_sucesso(self):
        self.verificar_se_elemento_existe(self.titulo_pagina)
