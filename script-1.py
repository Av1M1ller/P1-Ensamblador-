# 40 min

# Para prevenir warnings de Pylance...
class dir_memoria:
    pass

def puzzle_print(dir_matriz: "dir_memoria", F: int, C: int) -> None:

    f = 0  # Iterador del índice de cada fila
    n = 0 # Iterador de cada elemento de la matriz
    
    while f < F:
        c = 0  # Iterador del índice de cada fila
        while c < C:
            indice = (f * C) + c # Incluir en RISC-V '* 4 bytes'
            print(dir_matriz[indice], end="")
            if c + 1 != C:
                print(";", end="")

            c += 1

            # Avanzamos al siguiente elemento
            n += 1

        f += 1
        print("\n")


def search_puzzle(
    dir_matriz: "dir_memoria", F: int, C: int, dir_cadena: "dir_memoria", f: int, c: int
) -> bool:
    pass


matriz = ["H", "O", "L", "A", chr(182), "", chr(182), "M", "E", "S"]
F, C = 2, 5

puzzle_print(matriz, F, C)
