import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.ct_03_verificar_pagina_inicial import VerPaginaInicial

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.admin_vincular_gestor
class TestVerProdutosCadastrados:
    def test_ver_pagina_inicial(self):
        login_page = LoginPage()
        home_page = HomePage()
        login_page.fazer_login("geysonsilva@teste.com","Abcd1234")
        ver_pagina_inicial_page = VerPaginaInicial()

        # Verifica se o login foi realizado
        home_page.verificar_login_com_sucesso()

        # Chama o método para verificar a página inicial da Everest
        ver_pagina_inicial_page.ver_pagina_inicial()
