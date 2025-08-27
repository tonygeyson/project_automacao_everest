import time
import conftest
import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class TestLoginValido:
    def test_login_valido(self):
        self.driver = conftest.driver
        login_page = LoginPage()
        home_page = HomePage()
        login_page.fazer_login("geysonsilva@teste.com","Abcd1234")

        # Verifica se o login foi realizado
        home_page.verificar_login_com_sucesso()

        # Faz o processo de sair da Página
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".my-2"))).click()

        # Certifica que o elemento foi encontrado.
        mensagem_elemento_existe_sucesso = self.driver.find_element(By.XPATH,
        "//h1[@class='font-robot'][contains(.,'Login')]").text
        assert mensagem_elemento_existe_sucesso == "Login"
        print("Usuário saiu da página.")

