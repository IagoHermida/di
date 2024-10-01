def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    return a / b

if __name__ == "__main__":
    print(suma(3, 5))
    print(resta(10, 4))
    print(multiplicacion(2, 6))
    try:
        print(division(10, 0))
    except ValueError as e:
        print(e)
    print(division(10,5))