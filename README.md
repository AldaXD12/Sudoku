### **README.md**

# Sudoku Solver

Este proyecto contiene un programa que resuelve tableros de Sudoku utilizando un algoritmo voraz con backtracking. El programa busca una solución válida para un tablero dado y muestra el resultado con el formato típico de Sudoku.


## **Requisitos**
- Python 3.x instalado en tu computadora.  
  Si no lo tienes instalado, descárgalo desde [https://www.python.org/](https://www.python.org/).



## **Instrucciones para Ejecutar el Programa**

1. **Clonar el Repositorio**
   Si tienes Git instalado, clona este repositorio:
   ```bash
   git clone https://github.com/TuUsuario/sudoku-solver.git
   cd sudoku-solver
   ```

   Alternativamente, descarga el archivo ZIP desde el repositorio de GitHub y descomprímelo.

2. **Preparar el Tablero de Sudoku**
   - El tablero inicial se encuentra en el archivo `sudoku_solver.py`.
   - Busca la variable `tablero_inicial` y ajusta los valores según el tablero que quieras resolver. Usa `0` para representar celdas vacías:
     ```python
     tablero_inicial = [
         [5, 3, 0, 0, 7, 0, 0, 0, 0],
         [6, 0, 0, 1, 9, 5, 0, 0, 0],
         [0, 9, 8, 0, 0, 0, 0, 6, 0],
         [8, 0, 0, 0, 6, 0, 0, 0, 3],
         [4, 0, 0, 8, 0, 3, 0, 0, 1],
         [7, 0, 0, 0, 2, 0, 0, 0, 6],
         [0, 6, 0, 0, 0, 0, 2, 8, 0],
         [0, 0, 0, 4, 1, 9, 0, 0, 5],
         [0, 0, 0, 0, 8, 0, 0, 7, 9]
     ]
     ```

3. **Ejecutar el Programa**
   - Abre una terminal o consola en la carpeta donde se encuentra el archivo `sudoku_solver.py`.
   - Ejecuta el programa con el siguiente comando:
     ```bash
     python sudoku_solver.py
     ```
     o, si tu sistema usa `python3`:
     ```bash
     python3 sudoku_solver.py
     ```

---

## **Salida Esperada**

1. **Tablero Inicial:**  
   El programa muestra el tablero con divisiones características entre bloques 3x3. Las celdas vacías se representan con `.`.

2. **Tablero Resuelto:**  
   Si el tablero tiene solución, se imprime el tablero completo con las divisiones.

3. **Tiempo de Ejecución:**  
   Se muestra el tiempo total que tardó en encontrar la solución.

Ejemplo de salida:

```
Tablero inicial:
5 3 . | . 7 . | . . . 
6 . . | 1 9 5 | . . . 
. 9 8 | . . . | . 6 . 
---------------------
8 . . | . 6 . | . . 3 
4 . . | 8 . 3 | . . 1 
7 . . | . 2 . | . . 6 
---------------------
. 6 . | . . . | 2 8 . 
. . . | 4 1 9 | . . 5 
. . . | . 8 . | . 7 9 

Tablero resuelto:
5 3 4 | 6 7 8 | 9 1 2 
6 7 2 | 1 9 5 | 3 4 8 
1 9 8 | 3 4 2 | 5 6 7 
---------------------
8 5 9 | 7 6 1 | 4 2 3 
4 2 6 | 8 5 3 | 7 9 1 
7 1 3 | 9 2 4 | 8 5 6 
---------------------
9 6 1 | 5 3 7 | 2 8 4 
2 8 7 | 4 1 9 | 6 3 5 
3 4 5 | 2 8 6 | 1 7 9 

Tiempo de ejecución: 0.001234 segundos
```

---

## **Notas**
- Si el tablero no tiene solución, el programa mostrará un mensaje indicando que no hay soluciones posibles.
- El algoritmo está diseñado para resolver tableros estándar de 9x9.

---

## **Contribuciones**
Si encuentras errores o quieres mejorar el programa, por favor crea un **issue** o envía un **pull request** en el repositorio.

---

## **Licencia**
Este proyecto está bajo la licencia MIT. Puedes usarlo, modificarlo y distribuirlo libremente.
```