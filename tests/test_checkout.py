import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# Fixture que prepara el driver, hace login y añade un item al carrito
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
    driver.find_element(By.CLASS_NAME, "btn_inventory").click()
    yield driver
    driver.quit()

# Prueba del flujo de compra completo
def test_compra_exitosa(driver):
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.find_element(By.ID, "checkout").click()
    
    driver.find_element(By.ID, "first-name").send_keys("Juan")
    driver.find_element(By.ID, "last-name").send_keys("Perez")
    driver.find_element(By.ID, "postal-code").send_keys("10101")
    driver.find_element(By.ID, "continue").click()

    finish_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "finish"))
    )
    finish_button.click()
    
    mensaje_final = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))
    )
    assert mensaje_final.text == "Thank you for your order!"

# Prueba negativa de checkout sin nombre
def test_checkout_sin_nombre(driver):
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.find_element(By.ID, "checkout").click()
    
    # Rellena el formulario SIN el nombre
    driver.find_element(By.ID, "last-name").send_keys("Perez")
    driver.find_element(By.ID, "postal-code").send_keys("10101")
    driver.find_element(By.ID, "continue").click()

    # Verificación del mensaje de error
    mensaje_error = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
    assert "First Name is required" in mensaje_error

# Prueba de límite para cancelar el checkout
def test_cancelar_checkout(driver):
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.find_element(By.ID, "checkout").click()

    # Cancela el checkout
    driver.find_element(By.ID, "cancel").click()

    # Verificación: Debemos volver a la página del carrito
    url_actual = driver.current_url
    assert "cart.html" in url_actual