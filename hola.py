def busqueda_binaria(lista, objetivo):
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2

        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1


def menu():
    continuar = "si"

    while continuar == "si":
        # Lista ordenada
        lista = [1, 3, 5, 7, 9, 11, 13, 15]

        print("\nLista:", lista)
        numero = int(input("Ingresa el número que deseas buscar: "))

        resultado = busqueda_binaria(lista, numero)

        if resultado != -1:
            print(f"El número {numero} está en la posición {resultado}")
        else:
            print("El número no se encontró")

        continuar = input("¿Deseas buscar otro número? (si/no): ").lower()


# Ejecutar programa
menu()
