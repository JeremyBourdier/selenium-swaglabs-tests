import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Fixture que prepara el driver, hace login y añade un item al carrito
@pytest.fixture
def driver_con_producto(driver_logueado):
    driver_logueado.find_element(By.CLASS_NAME, "btn_inventory").click()
    return driver_logueado

# Prueba del flujo de compra completo
def test_compra_exitosa(driver_con_producto):
    driver_con_producto.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver_con_producto.find_element(By.ID, "checkout").click()
    
    # Rellena el formulario
    driver_con_producto.find_element(By.ID, "first-name").send_keys("Juan")
    driver_con_producto.find_element(By.ID, "last-name").send_keys("Perez")
    driver_con_producto.find_element(By.ID, "postal-code").send_keys("10101")
    driver_con_producto.find_element(By.ID, "continue").click()

    finish_button = WebDriverWait(driver_con_producto, 10).until(
        EC.element_to_be_clickable((By.ID, "finish"))
    )
    finish_button.click()
    
    mensaje_final = WebDriverWait(driver_con_producto, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))
    )
    assert mensaje_final.text == "Thank you for your order!"

# Prueba negativa de checkout sin nombre
def test_checkout_sin_nombre(driver_con_producto):
    driver_con_producto.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver_con_producto.find_element(By.ID, "checkout").click()
    
    # Rellena el formulario SIN el nombre
    driver_con_producto.find_element(By.ID, "last-name").send_keys("Perez")
    driver_con_producto.find_element(By.ID, "postal-code").send_keys("10101")
    driver_con_producto.find_element(By.ID, "continue").click()

    # Verificación del mensaje de error
    mensaje_error = driver_con_producto.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
    assert "First Name is required" in mensaje_error

# Prueba de límite para cancelar el checkout
def test_cancelar_checkout(driver_con_producto):
    driver_con_producto.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver_con_producto.find_element(By.ID, "checkout").click()

    # Cancela el checkout
    driver_con_producto.find_element(By.ID, "cancel").click()

    # Debemos volver a la página del carrito
    url_actual = driver_con_producto.current_url
    assert "cart.html" in url_actual