import conftest
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.username_field = (By.ID, "email")
        self.password_field = (By.ID, "password")
        self.login_button = (By.CSS_SELECTOR, ".btn-primary")
        self.driver.implicitly_wait(10)

    def fazer_login(self, usuario, senha):
        self.escrever(self.username_field, usuario)
        self.escrever(self.password_field, senha)
        self.clicar(self.login_button)
        self.driver.implicitly_wait(10)

class LoginPageSenhaErrada(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.username_field = (By.ID, "email")
        self.password_field = (By.ID, "password")
        self.login_button = (By.CSS_SELECTOR, ".btn-primary")
        self.driver.implicitly_wait(10)

    def fazer_login(self, usuario, senha):
        self.escrever(self.username_field, usuario)
        self.escrever(self.password_field, senha)
        self.clicar(self.login_button)

