from selenium.webdriver.common.by import By

# Prueba para añadir un item al carrito
def test_anadir_producto_al_carrito(driver_logueado):
    # Añade el primer producto al carrito
    driver_logueado.find_element(By.CLASS_NAME, "btn_inventory").click()
    
    # Verifica que el ícono del carrito ahora muestre "1"
    icono_carrito = driver_logueado.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert icono_carrito == "1"

# Prueba para quitar un item del carrito
def test_quitar_producto_del_carrito(driver_logueado):
    # Primero, añade un producto para poder quitarlo
    driver_logueado.find_element(By.CLASS_NAME, "btn_inventory").click()

    # Ahora, quita el producto
    driver_logueado.find_element(By.CLASS_NAME, "btn_inventory").click()

    # Verifica que el ícono del carrito desaparece
    elementos_carrito = driver_logueado.find_elements(By.CLASS_NAME, "shopping_cart_badge")
    assert len(elementos_carrito) == 0

# Se puede completar una compra con carrito vacío (BUG)
def test_checkout_carrito_vacio(driver_logueado):
    # Va al carrito y al checkout
    driver_logueado.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver_logueado.find_element(By.ID, "checkout").click()

    # Rellena el formulario y continúa
    driver_logueado.find_element(By.ID, "first-name").send_keys("Test")
    driver_logueado.find_element(By.ID, "last-name").send_keys("User")
    driver_logueado.find_element(By.ID, "postal-code").send_keys("12345")
    driver_logueado.find_element(By.ID, "continue").click()

    # Intenta finalizar la compra en la segunda página
    driver_logueado.find_element(By.ID, "finish").click()

    # Verificación: La prueba ahora confirma el bug, esperando llegar a la página final.
    url_actual = driver_logueado.current_url
    assert "checkout-complete.html" in url_actual