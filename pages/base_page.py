import conftest


# Vai ser usado para as próximas páginas que eu for usar
class BasePage:
    def __init__(self):
        self.driver = conftest.driver

    # Métodos genérios para utilização
    def encontrar_elemento(self, locator):
        return self.driver.find_element(*locator)

    def encontrar_elementos(self, locator):
        return self.driver.find_elements(*locator)

    def escrever(self, locator, text):
        self.encontrar_elemento(locator).send_keys(text)

    def clicar(self, locator):
        self.encontrar_elemento(locator).click()

    def verificar_se_elemento_existe(self, locator):
        assert self.encontrar_elemento(locator).is_displayed(), f"O elemento '{locator}' não foi encontrado na tela."

    def pegar_texto_elemento(self, locator):
        return self.encontrar_elemento(locator).text

    # Métodos da página inicial antes do login
    def texto_elemento_lateral_esquerdo(self, locator):
        return self.texto_elemento_lateral_esquerdo(locator).text


