import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.ct_04_adicionar_produtos import AdicionarProdutos

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.adicionar_produtos
class TestAdicionarProdutos:
    def test_adicionar_produtos(self):
        login_page = LoginPage()
        home_page = HomePage()
        login_page.fazer_login("standard_user","secret_sauce")
        adicionar_produtos_page = AdicionarProdutos()

        # Verifica se o login foi realizado
        home_page.verificar_login_com_sucesso()

        # Chama o método para adicionar produtos ao carrinho
        adicionar_produtos_page.adicionar_produtos()
