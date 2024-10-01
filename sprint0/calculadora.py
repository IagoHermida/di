from operaciones import suma, resta, multiplicacion, division


def calcular():
    while True:
        try:
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))
        except ValueError:
            print("Por favor, introduce un número válido.")
            continue

        print("\n¿Qué operación deseas realizar?")
        print("1: Suma")
        print("2: Resta")
        print("3: Multiplicación")
        print("4: División")
        operacion = input("Introduce el número de la operación: ")

        if operacion == '1':
            print(f"Resultado de la suma: {suma(num1, num2)}\n")
        elif operacion == '2':
            print(f"Resultado de la resta: {resta(num1, num2)}\n")
        elif operacion == '3':
            print(f"Resultado de la multiplicación: {multiplicacion(num1, num2)}\n")
        elif operacion == '4':
            try:
                print(f"Resultado de la división: {division(num1, num2)}\n")
            except ValueError as e:
                print(e)
        else:
            print("Operación no válida. Inténtalo de nuevo.\n")
            continue

        continuar = input("¿Quieres realizar otra operación? (s/n): ").lower()
        if continuar != 's':
            print("Fin del programa.")
            break


if __name__ == "__main__":
    calcular()