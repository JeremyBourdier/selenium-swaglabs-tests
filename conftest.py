import pytest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver(request):
    """Fixture base: abre, configura y cierra un navegador limpio."""
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    yield driver
    
    # Lógica para la captura de pantalla
    if not os.path.exists('screenshots'):
        os.makedirs('screenshots')

    # Obtiene el nombre de la prueba que acaba de ejecutarse
    test_name = request.node.name
    
    # Guarda la captura
    driver.save_screenshot(f"screenshots/{test_name}.png")
    # ----------------------------------------

    driver.quit()

@pytest.fixture
def driver_logueado(driver):
    """Fixture que usa el driver base y realiza el login."""
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    return driver

@pytest.fixture
def driver_con_producto(driver_logueado):
    """Fixture que usa el driver logueado y añade un producto."""
    driver_logueado.find_element(By.CLASS_NAME, "btn_inventory").click()
    return driver_logueado