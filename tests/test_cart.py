import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Fixture para configurar y limpiar el driver para cada prueba
@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    # Login previo para las pruebas del carrito
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    yield driver
    # Limpieza
    driver.quit()

# Prueba para añadir un item al carrito
def test_anadir_producto_al_carrito(driver):
    # Añade el primer producto al carrito
    driver.find_element(By.CLASS_NAME, "btn_inventory").click()
    
    # Verifica que el ícono del carrito ahora muestre "1"
    icono_carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert icono_carrito == "1"