import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.ct_05_remover_produtos import RemoverProdutos

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.remover_produtos
class TestRemoverProdutos:
    def test_remover_produtos(self):
        login_page = LoginPage()
        home_page = HomePage()
        login_page.fazer_login("standard_user","secret_sauce")
        remover_produtos_page = RemoverProdutos()

        # Verifica se o login foi realizado
        home_page.verificar_login_com_sucesso()

        # Chama o método para remover produtos do carrinho
        remover_produtos_page.remover_produtos()
