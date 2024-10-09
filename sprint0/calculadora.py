#importamos los metodos del archivo operaciones
from operaciones import suma, resta, multiplicacion, division

#Creamos un metodo que hará de calculadora
def calcular():
    while True:
        #introducimos los dos números que usaremos comprobando que estos sean válidos
        try:
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))
        except ValueError:
            print("Por favor, introduce un número válido.")
            continue

        #Preguntamos al usuario que operación desea realizar
        print("\n¿Qué operación deseas realizar?")
        print("1: Suma")
        print("2: Resta")
        print("3: Multiplicación")
        print("4: División")
        operacion = input("Introduce el número de la operación: ") #Leemos la elección del usuario

        if operacion == '1':
            print(f"Resultado de la suma: {suma(num1, num2)}\n") #Hacemos la suma llamando al metodo
        elif operacion == '2':
            print(f"Resultado de la resta: {resta(num1, num2)}\n")  #Hacemos la resta llamando al metodo
        elif operacion == '3':
            print(f"Resultado de la multiplicación: {multiplicacion(num1, num2)}\n") #Hacemos la multiplicación llamando al metodo
        elif operacion == '4':
            try:
                print(f"Resultado de la división: {division(num1, num2)}\n") #Hacemos la división llamando al metodo
            except ValueError as e:
                print(e) #En caso de que el segundo número sea 0 nos dará el aviso
        else:
            print("Operación no válida. Inténtalo de nuevo.\n") #Si ha escogido una opción fuera del rango daremos un aviso al usuario
            continue

        #Preguntamos al usuario si desea seguir utilizando la calculadora
        continuar = input("¿Quieres realizar otra operación? (s/n): ").lower()
        if continuar != 's': #En caso de que la respuesta no sea "s" se terminará el programa
            print("Fin del programa.")
            break


if __name__ == "__main__":
    calcular()