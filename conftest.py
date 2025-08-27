import pytest
from selenium import webdriver
driver: webdriver.Remote

@pytest.fixture()
def setup_teardown():
    #setup
    global driver

    # driver = webdriver.Safari()
    driver = webdriver.Chrome()
    # driver = webdriver.ChromiumEdge()
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://front.serverest.dev/login")

    # Exectuta o teste
    yield

    # teardown fecha o teste
    driver.quit()

