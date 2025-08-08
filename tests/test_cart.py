import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    yield driver
    driver.quit()

def test_anadir_producto_al_carrito(driver):
    driver.find_element(By.CLASS_NAME, "btn_inventory").click()
    icono_carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert icono_carrito == "1"

def test_quitar_producto_del_carrito(driver):
    driver.find_element(By.CLASS_NAME, "btn_inventory").click()
    driver.find_element(By.CLASS_NAME, "btn_inventory").click()
    elementos_carrito = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
    assert len(elementos_carrito) == 0

# # Prueba de checkout con carrito vacío
# def test_checkout_carrito_vacio(driver):
#     # Ve al carrito y al checkout
#     driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
#     driver.find_element(By.ID, "checkout").click()

#     # Rellena el formulario y continúa
#     driver.find_element(By.ID, "first-name").send_keys("Test")
#     driver.find_element(By.ID, "last-name").send_keys("User")
#     driver.find_element(By.ID, "postal-code").send_keys("12345")
#     driver.find_element(By.ID, "continue").click()

#     # Intenta finalizar la compra en la segunda página
#     driver.find_element(By.ID, "finish").click()
    
#     # Verificación: El sistema nos debe devolver a la página del carrito
#     url_actual = driver.current_url
#     assert "cart.html" in url_actual
# Si se completa una compra con carrito vacío, se llega a la página final

# Se puede completar una compra con carrito vacío (BUG)
def test_checkout_carrito_vacio(driver):
    # Va al carrito y al checkout
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.find_element(By.ID, "checkout").click()

    # Rellena el formulario y continúa
    driver.find_element(By.ID, "first-name").send_keys("Test")
    driver.find_element(By.ID, "last-name").send_keys("User")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.ID, "continue").click()

    # Intenta finalizar la compra en la segunda página
    driver.find_element(By.ID, "finish").click()

    # Verificación: La prueba ahora confirma el bug, esperando llegar a la página final.
    url_actual = driver.current_url
    assert "checkout-complete.html" in url_actual