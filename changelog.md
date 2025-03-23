## Implementación del Power-Up par de cañones

Para implementar el power-up del par de cañones, se han realizado las siguientes modificaciones:

*   **Creación de la clase `PairCannons` (`src/powerups/PairCannons.py`):** Define el comportamiento del power-up y lo desencadena cuando la paleta toma el power-up

*   **Creación de la clase `Cannon` (`src/Cannon.py`):** Define un cañón que puede disparar bolas de cañón en el juego Breakout. Esta clase es parte de la implementacion del power-up PairCannon

*   **Creación de la clase `CannonBall` (`src/CannonBall.py`):** Define una bola de cañon en el juego. Hereda de la clase Ball, por lo que tiene todas las propiedades y metodos de este. Esta clase es utilizada por la clase Cannon para disparar bolas de cañon cuando se activa el power-up correspondiente

*   **Modificación de la clase `PlayState` (`src/states/PlayState.py`):**
    *   Se ha añadido la lógica para generar el power-up aleatoriamente al romper un ladrillo. **(Lineas 134 a 141)**
    *   Se ha añadido la lógica para activar el power-up al colisionar con la paleta, generando dos cañones junto a la paleta uno en cada lado
    *   Se ha añadido el mecanismo para poder dispara los cañones al presionar la tecla F. **(Lineas 276 a 280)**

*   **Modificación del archivo `settings.py`:** 
    *   Se han añadido las configuraciones necesarias para el power-up, como la carga de la textura de los cañones junto con su frame
    *   Se ha añadido una nueva tecla de accion para disparar los cañones "F" 

*   **Modificación del archivo `Paddle.py`:** 
    *   Se han añadido las logica necesarias para el power-up, como el par de cañones que se activan si se toma el power-up correspondiente
    *   Se ha añadido un nuevo metodo fire para dispara los cañones

## Implementación del Power-Up bolas pegajosas

Para implementar el power-up de bolas pegajosas, se han realizado las siguientes modificaciones:

*   **Creación de la clase `AttachedBall` (`src/powerups/AttachedBall.py`):** Define el comportamiento del power-up y lo desencadena cuando la paleta toma el power-up

*   **Modificación de la clase `PlayState` (`src/states/PlayState.py`):**
    *   Se ha añadido la lógica para generar el power-up aleatoriamente al romper un ladrillo. **(lineas 125 a 132)**
    *   Se ha añadido la lógica para activar el power-up al colisionar con la paleta, haciendo que, si la o las bolas colisionan con la paleta esta se adieren a la paleta. **(lineas 62 a 82)**
    *   Se ha añadido el mecanismo para poder lanzar la bola al presionar la tecla enter. **(Lineas 259 a 274)**
    *   Se ha añadido un timer para definir cuanto tiempo debe estar activo el power-up. **(Lineas 72 a 79)**

