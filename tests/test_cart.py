import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Fixture para limpiar y configurar el driver
@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    yield driver
    driver.quit()

# Prueba para añadir un item al carrito
def test_anadir_producto_al_carrito(driver):
    driver.find_element(By.CLASS_NAME, "btn_inventory").click()
    icono_carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert icono_carrito == "1"

# Prueba para quitar un item del carrito
def test_quitar_producto_del_carrito(driver):
    driver.find_element(By.CLASS_NAME, "btn_inventory").click()
    driver.find_element(By.CLASS_NAME, "btn_inventory").click()
    elementos_carrito = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
    assert len(elementos_carrito) == 0

# Prueba de checkout con carrito vacío
def test_checkout_carrito_vacio(driver):
    # Ve al carrito directamente
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Intenta hacer checkout y llenar el formulario
    driver.find_element(By.ID, "checkout").click()
    driver.find_element(By.ID, "first-name").send_keys("Test")
    driver.find_element(By.ID, "last-name").send_keys("User")
    driver.find_element(By.ID, "postal-code").send_keys("12345")

    # Intenta continuar
    driver.find_element(By.ID, "continue").click()

    # Nos debemos quedar en la misma página
    url_actual = driver.current_url
    assert "checkout-step-one.html" in url_actual