# Para prevenir warnings de Pylance...
class dir_memoria:
    pass


matriz = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
]  # n_filas = 4 /// n_columnas = 4

caracteres_bien = ["a", "b", "c"]
caracteres_mal = ["a"]


def puzzle_print(dir_matriz: "dir_memoria", F: int, C: int) -> None:
    """Imprime el contenido de la matriz"""

    f = 0  # Iterador del índice de cada fila
    n = 0  # Iterador de cada elemento de la matriz

    while f < F:
        c = 0  # Iterador del índice de cada fila
        while c < C:
            indice = (f * C) + c  # Incluir en RISC-V '* 4 bytes'
            print(dir_matriz[indice], end="")
            if c + 1 != C:
                print(";", end="")

            c += 1

            # Avanzamos al siguiente elemento
            n += 1

        f += 1
        print("\n")


def search_puzzle(
    direccion_matriz,
    n_filas,
    n_columnas,
    direccion_caracteres,
    coordenada_fila,
    coordenada_columna,
) -> bool:
    """Esta función determina si una palabra se puede insertar en la sopa de letras de forma horizontal
    a partir de una determinada coordenada de forma completa."""

    longitud_matriz = len(direccion_matriz)

    if (
        coordenada_fila < n_filas
    ):  # doble if o and según sea mejor para usar el ensamblador
        if coordenada_columna < n_columnas - 1:
            print("la coordena de la columna es válida")
            inicio = (n_columnas * coordenada_fila) + (coordenada_columna + 1)
        else:
            return 0
    else:
        return 0

    longitud_palabra = len(direccion_caracteres)
    posicion = inicio

    contador = 0
    print(
        f"posicion {posicion - (coordenada_fila * n_columnas)}, longitud_palabra: {longitud_palabra}"
    )
    while posicion < (coordenada_fila) * n_columnas:
        print(f"contador while: {contador}")
        if direccion_matriz[posicion] != chr(182):
            print(f"no hay {chr(182)} en {posicion}")
            posicion += 1
        else:
            return 0
        contador += 1

    if posicion == (coordenada_fila + 1) * n_columnas:
        print("los caracteres caben de forma exacta")
        return 1
    else:
        return 0


def insert_puzzle(
    direccion_matriz,
    n_filas,
    n_columnas,
    direccion_caracteres,
    coordenada_fila,
    coordenada_columna,
):
    """Esta  función  inserta  una  palabra  en  una  sopa  de  letras  de  forma  horizontal  a  partir  de  una
    determinada coordenada."""

    palabra_cabe = search_puzzle(
        direccion_matriz,
        n_filas,
        n_columnas,
        direccion_caracteres,
        coordenada_fila,
        coordenada_columna,
    )
    if palabra_cabe == 0:
        print("la palabra no cabe")
        return 0

    elif palabra_cabe == 1:
        print("la palabra cabe")
        longitud_matriz = len(direccion_matriz)
        inicio = (n_columnas * coordenada_fila) + (coordenada_columna)
        posicion = inicio
        i = 0
        while i < longitud_matriz:
            direccion_matriz[posicion] = direccion_caracteres[i]
            posicion += 1
            i += 1
        return direccion_matriz


F, C = 6, 5
matriz = [0] * (F * C)

def fill_puzzle(
    dir_matriz: "dir_memoria", F: int, C: int, dir_V: "dir_memoria", n_chars: int
) -> bool:
    """Esta función crea una sopa de letras a partir de una lista de coordenadas formada
    por un vector V que almacenará las coordenadas de la matriz donde hay que insertar el símbolo ¶.
    """

    V = [0, 4, 1, 1, 3, 1, 3, 2]
    global matriz 
    i = 0
    while i < n_chars:
        indice_colocacion = V[i] * C + V[i + 1]
        # print(indice_colocacion, (V[i], V[i + 1]))
        if indice_colocacion <= F * C:
            matriz[indice_colocacion] = chr(182)
        else:
            # Index out of Bounds
            return 0

        # Saltar al siguiente par de coordenadas
        i += 2

    # Todas las coordenadas estaban dentro de la matriz
    return 1


def main():
    print(
        search_puzzle(
            direccion_matriz=matriz,
            n_filas=4,
            n_columnas=4,
            direccion_caracteres=caracteres_bien,
            coordenada_fila=0,
            coordenada_columna=0,
        )
    )
    print(
        insert_puzzle(
            direccion_matriz=matriz,
            n_filas=4,
            n_columnas=4,
            direccion_caracteres=caracteres_bien,
            coordenada_fila=0,
            coordenada_columna=0,
        )
    )
    print("---")
    print(fill_puzzle("memoria", F, C, "memoria", 8))
    puzzle_print(matriz, F, C)

main()
