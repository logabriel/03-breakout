# Breakout Game with Golden Coin Power-Up

Este proyecto es una implementación del clásico juego Breakout en Python utilizando Pygame y el framework Gale. Se ha añadido un nuevo power-up: la Moneda Dorada.

## Características

*   Implementación del juego Breakout con Gale.
*   Power-up de la Moneda Dorada que duplica la puntuación durante un tiempo limitado.
*   Textos flotantes para indicar la activación del power-up.
*   Efectos de sonido al recoger el power-up.

## Estructura de Carpetas

El proyecto sigue la siguiente estructura:
0
*   `assets/`: Contiene los recursos del juego (sonidos, fuentes, gráficos).
*   `src/`: Contiene el código fuente del juego.
    *   `powerups/`: Implementación de los power-ups.
        *   `GoldCoin.py`: Lógica del power-up de la Moneda Dorada.
        *   `PowerUp.py`: Clase base para los power-ups.
        *   `__init__.py`: Inicializa el paquete `powerups`.
    *   `states/`: Implementación de los estados del juego.
        *   `PlayState.py`: Lógica del estado de juego principal.
    *   `utilities/`: Clases de utilidad.
        *   `timer.py`: Implementación de la clase Timer para manejar la duración del power-up.
        *   `floating_text.py`: Clase para mostrar textos flotantes en la pantalla.
    *   `Breakout.py`: Clase principal del juego.
    *   `main.py`: Punto de entrada del juego.
*   `settings.py`: Contiene la configuración del juego (dimensiones de la ventana, rutas de los recursos, etc.).

## Implementación del Power-Up de la Moneda Dorada

Para implementar el power-up de la Moneda Dorada, se han realizado las siguientes modificaciones:

*   **Creación de la clase `GoldCoin` (`src/powerups/GoldCoin.py`):** Define el comportamiento del power-up, incluyendo la activación del multiplicador de puntuación, la visualización del texto flotante y la reproducción del sonido.
*   **Modificación de la clase `PlayState` (`src/states/PlayState.py`):**
    *   Se ha añadido la lógica para generar el power-up aleatoriamente al romper un ladrillo.
    *   Se ha añadido la lógica para detectar la colisión entre el power-up y la paleta.
    *   Se ha añadido la lógica para activar el power-up al colisionar con la paleta, aplicando el multiplicador de puntuación y mostrando el texto flotante.
    *   Se ha añadido la lógica para actualizar y dibujar los power-ups en la pantalla.
*   **Creación de la clase `Timer` (`src/utilities/timer.py`):** Implementa un temporizador para manejar la duración del efecto del power-up.
*   **Creación de la clase `FloatingText` (`src/utilities/floating_text.py`):** Implementa una clase para mostrar textos flotantes en la pantalla.
*   **Modificación del archivo `settings.py`:** Se han añadido las configuraciones necesarias para el power-up, como la probabilidad de aparición, los sonidos y las fuentes.

## Uso

Para ejecutar el juego, sigue estos pasos:

1.  Asegúrate de tener Python 3 instalado.
2.  Crea y activa un entorno virtual (recomendado):
    ```
    python3 -m venv myenv
    source myenv/bin/activate
    ```
3.  Instala las dependencias:
    ```
    pip install -r requirements.txt
    ```
4.  Ejecuta el archivo `main.py`:
    ```
    python main.py
    ```

## Créditos

*   Este proyecto se basa en el framework Gale.
*   Los recursos del juego (sonidos, fuentes, gráficos) son de dominio público.

