

matriz = [1,2,3,4,
          5,6,7,8,
          9,10,11,12,
          13,14,15,16] #n_filas = 4 /// n_columnas = 4

caracteres_bien = ["a","b","c"]
caracteres_mal = ["a"]
def search_puzzle(direccion_matriz, n_filas, n_columnas, direccion_caracteres, coordenada_fila, coordenada_columna):
    longitud_matriz = len(direccion_matriz)

    if coordenada_fila < n_filas: # doble if o and según sea mejor para usar el ensamblador
        if coordenada_columna  < n_columnas -1 :
            print("la coordena de la columna es válida")
            inicio = (n_columnas * coordenada_fila) + (coordenada_columna +1)
        else:
            return 0
    else:
        return 0

    longitud_palabra = len(direccion_caracteres)
    posicion = inicio

    contador = 0
    print(f"posicion {posicion - (coordenada_fila * n_columnas)}, longitud_palabra: {longitud_palabra}")
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


def insert_puzzle(direccion_matriz, n_filas, n_columnas, direccion_caracteres, coordenada_fila, coordenada_columna):
    palabra_cabe = search_puzzle(direccion_matriz, n_filas, n_columnas, direccion_caracteres, coordenada_fila, coordenada_columna)
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


def fill_puzzle(direccion_matriz, n_filas,n_columnas, direccion_char, n_chars):
    V = [0, 4, 1, 1, 3, 1, 3, 2]
    direccion_matriz = [0]*(n_filas* n_columnas)
    i = 0
    while i < n_chars:
        colocacion = 

    print(direccion_matriz)



def main():
    print(search_puzzle(direccion_matriz= matriz, n_filas = 4, n_columnas = 4, direccion_caracteres= caracteres_bien, coordenada_fila=0, coordenada_columna= 0))
    print(insert_puzzle(direccion_matriz= matriz, n_filas = 4, n_columnas = 4, direccion_caracteres= caracteres_bien, coordenada_fila=0, coordenada_columna= 0))
main()