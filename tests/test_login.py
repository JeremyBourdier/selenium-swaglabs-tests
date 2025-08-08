from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Camino Feliz
def test_login_exitoso():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.saucedemo.com/")

    # Acciones
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Verificación
    titulo_productos = driver.find_element(By.CLASS_NAME, "title").text
    assert titulo_productos == "Products"

    driver.quit()

# Prueba Negativa
def test_login_fallido():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.saucedemo.com/")

    # Acciones con contraseña incorrecta
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("Esta no es la contraseña")
    driver.find_element(By.ID, "login-button").click()

    # Mnsaje de error
    mensaje_error = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
    assert "Username and password do not match" in mensaje_error

    driver.quit()