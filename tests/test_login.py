import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Fixture para configurar y limpiar el driver
@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    # Limpieza
    driver.quit()

# Camino Feliz
def test_login_exitoso(driver):
    driver.get("https://www.saucedemo.com/")
    # Acciones
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    # Verificación
    titulo_productos = driver.find_element(By.CLASS_NAME, "title").text
    assert titulo_productos == "Products"

# Prueba Negativa
def test_login_fallido(driver):
    driver.get("https://www.saucedemo.com/")
    # Acciones con contraseña incorrecta
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("bad_password")
    driver.find_element(By.ID, "login-button").click()
    # Mensaje de error
    mensaje_error = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
    assert "Username and password do not match" in mensaje_error

# Prueba de Límite Usuario Bloqueado
def test_login_usuario_bloqueado(driver):
    driver.get("https://www.saucedemo.com/")
    # Acciones con usuario bloqueado
    driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    # Mensaje de error específico para este caso
    mensaje_error = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
    assert "Sorry, this user has been locked out" in mensaje_error