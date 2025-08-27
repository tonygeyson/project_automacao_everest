import pytest
import conftest
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
@pytest.mark.smoke
class TestLoginValido:
    def test_login_valido(self):
         # Entra no sistema
        driver = conftest.driver
        login_page = LoginPage()
        login_page.fazer_login("geysonsilva@teste.com", "Abcd1234")

        # Certifica que o usuário está logado no Everest
        logged_in_element = driver.find_element(By.XPATH, "//button[@data-testid='entrar'][contains(.,'Entrar')]")
        assert logged_in_element.is_displayed(), "Falha ao verificar se o usuário está logado."
