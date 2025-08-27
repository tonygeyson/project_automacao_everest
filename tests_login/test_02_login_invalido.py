import pytest
import conftest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.login_page import LoginPageSenhaErrada
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class TestLoginInvalido:
    def test_login_invalido(self):
        self.driver = conftest.driver
        login_page = LoginPageSenhaErrada()
        login_page.fazer_login("geyson_silva@teste.com","senha_errada")

        # Certifica que o elemento foi encontrado.
        mensagem_elemento_existe_sucesso = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(.,'Email e/ou senha inválidos')]"))).text
        assert mensagem_elemento_existe_sucesso == "Email e/ou senha inválidos"
        print("Login inválido.")