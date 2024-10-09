#Suma de los numeros n1 y n2 que recibe el metodo
def suma(n1, n2):
    return n1 + n2

#Resta de los numeros n1 y n2 que recibe el metodo
def resta(n1, n2):
    return n1 - n2

#Multiplicación de los numeros n1 y n2 que recibe el metodo
def multiplicacion(n1, n2):
    return n1 * n2

#División de los numeros n1 y n2 que recibe el metodo
#En caso de que n2 sea 0 dará un aviso de que no se puede dividir por 0
def division(n1, n2):
    if n2 == 0:
        raise ValueError("No se puede dividir por cero.")
    return n1 / n2

#Creamos un ejemplo con cada metodo para comprobar que estos funcionan
if __name__ == "__main__":
    print(suma(3, 5))
    print(resta(10, 4))
    print(multiplicacion(2, 6))
    try:
        print(division(10, 0))
    except ValueError as e:
        print(e)
    print(division(10,5))