from heroe import Heroe
from mazmorra import Mazmorra

def main():
    #Pedimos al usuario que introduzca el nombre de su heroe y posteriormente creamos el personaje con dicho nombre
    nombre_heroe = input("Introduce el nombre de tu héroe: ")
    heroe = Heroe(nombre_heroe)
    #iniciamos la clase mazmorra con nuestro heroe e invocamos el metodo jugar
    mazmorra = Mazmorra(heroe)
    mazmorra.jugar()

#Ejecutamos el main
if __name__ == "__main__":
    main()