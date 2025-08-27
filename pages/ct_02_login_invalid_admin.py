import pytest
import conftest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.login_page import LoginPageSenhaErrada
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
@pytest.mark.smoke
class TestLoginInvalido:
    def test_login_invalido(self):
        # Entra no sistema
        self.driver = conftest.driver
        login_page = LoginPageSenhaErrada()
        login_page.fazer_login("geysonsilva@teste.com", "Senhaerrada")

        # Verifica mensagem de erro
        mensagem_erro = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//h3[@data-test='error'][contains(.,'Epic sadface: Username and "
                                                  "password do not match any user in this service')]"))
        ).text
        mensagem_esperada = "Epic sadface: Username and password do not match any user in this service"
        assert mensagem_erro == mensagem_esperada, "Mensagem de erro de login inválido não corresponde ao esperado"
        print("Login inválido.")