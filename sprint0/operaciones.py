def suma(n1, n2):
    return n1 + n2

def resta(n1, n2):
    return n1 - n2

def multiplicacion(n1, n2):
    return n1 * n2

def division(n1, n2):
    if n2 == 0:
        raise ValueError("No se puede dividir por cero.")
    return n1 / n2

if __name__ == "__main__":
    print(suma(3, 5))
    print(resta(10, 4))
    print(multiplicacion(2, 6))
    try:
        print(division(10, 0))
    except ValueError as e:
        print(e)
    print(division(10,5))