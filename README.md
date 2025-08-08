# Proyecto de Pruebas Automatizadas con Selenium

Este es un proyecto de práctica que desarrolla una suite de pruebas automatizadas para la página web de demostración `saucedemo.com`. Se utilizan Selenium y Pytest para verificar los flujos de trabajo críticos de la aplicación.

## Características Probadas

El proyecto cubre las siguientes historias de usuario con múltiples casos de prueba:

* **Flujo de Inicio de Sesión:**
    *  Prueba de login exitoso (camino feliz).
    *  Prueba de login con credenciales incorrectas (prueba negativa).
    *  Prueba de login con un usuario bloqueado (prueba de límite).

* **Flujo del Carrito de Compras:**
    * Prueba para añadir un producto al carrito (camino feliz).
    * Prueba para eliminar un producto del carrito (prueba negativa).
    * Prueba para intentar finalizar la compra con un carrito vacío (prueba de límite, identifica un bug).

* **Flujo de Compra (Checkout):**
    *  Prueba de un proceso de compra exitoso de principio a fin (camino feliz).
    *  Prueba de checkout con campos de formulario vacíos (prueba negativa).
    *  Prueba de la funcionalidad de cancelar el checkout (prueba de límite).

* **Calidad y Reportes:**
    * **Reportes en HTML:** Generación automática de reportes de resultados con `pytest-html`.
    * **Capturas de Pantalla:** Captura automática de una imagen al finalizar cada prueba para evidencia visual.
    * **Código Refactorizado:** Uso de `conftest.py` para centralizar `fixtures`, haciendo las pruebas más limpias y mantenibles.

## Requisitos

* Python 3.x

## Instalación y Uso

1.  **Clona el repositorio:**
    ```bash
    git clone [https://github.com/tu-usuario/selenium-swaglabs-tests.git](https://github.com/tu-usuario/selenium-swaglabs-tests.git)
    cd selenium-swaglabs-tests
    ```

2.  **Crea y activa un entorno virtual:**
    * En Windows:
        ```powershell
        python -m venv venv
        .\venv\Scripts\activate
        ```
    * En macOS / Linux:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3.  **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Ejecuta las pruebas:**
    * Para correr todas las pruebas desde la terminal:
        ```bash
        python -m pytest
        ```
    * Para generar el reporte en HTML:
        ```bash
        python -m pytest --html=reporte_pruebas.html
        ```
    * Las capturas de pantalla se guardarán automáticamente en la carpeta `screenshots/`.
