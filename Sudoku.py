import time

def es_valido(tablero, fila, columna, num):
    """
    Comprueba si es válido colocar 'num' en la posición (fila, columna).
    """
    # Comprobar la fila
    if num in tablero[fila]:
        return False
    
    # Comprobar la columna
    if num in [tablero[i][columna] for i in range(9)]:
        return False
    
    # Comprobar el subcuadrante 3x3
    inicio_fila, inicio_columna = 3 * (fila // 3), 3 * (columna // 3)
    for i in range(inicio_fila, inicio_fila + 3):
        for j in range(inicio_columna, inicio_columna + 3):
            if tablero[i][j] == num:
                return False
    
    return True

def resolver_sudoku(tablero):
    """
    Resuelve el Sudoku usando backtracking.
    """
    # Buscar una celda vacía (marcada como 0)
    for fila in range(9):
        for columna in range(9):
            if tablero[fila][columna] == 0:
                # Intentar con números del 1 al 9
                for num in range(1, 10):
                    if es_valido(tablero, fila, columna, num):
                        tablero[fila][columna] = num
                        
                        # Recursión: intentar resolver el resto del tablero
                        if resolver_sudoku(tablero):
                            return True
                        
                        # Si no funciona, retrocede
                        tablero[fila][columna] = 0
                
                # Si no se puede colocar ningún número, no hay solución
                return False
    return True

def imprimir_tablero(tablero):
    """
    Imprime el tablero de Sudoku con divisiones características.
    """
    for i, fila in enumerate(tablero):
        if i % 3 == 0 and i != 0:
            print("-" * 21)  # Línea divisoria entre bloques 3x3
        for j, num in enumerate(fila):
            if j % 3 == 0 and j != 0:
                print("| ", end="")  # Línea divisoria entre columnas de bloques 3x3
            print(f"{num if num != 0 else '.'} ", end="")
        print()  # Nueva línea al final de cada fila

# Tablero inicial
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


print("Tablero inicial:")
imprimir_tablero(tablero_inicial)

# Medir tiempo de ejecución
inicio = time.time()
if resolver_sudoku(tablero_inicial):
    fin = time.time()
    print("\nTablero resuelto:")
    imprimir_tablero(tablero_inicial)
    print(f"\nTiempo de ejecución: {fin - inicio:.6f} segundos")
else:
    print("\nNo hay solución para este tablero.")
