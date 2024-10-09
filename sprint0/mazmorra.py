from heroe import Heroe
from monstruo import Monstruo
from tesoro import Tesoro
import random


class Mazmorra:
    #Iniciamos al heroe, 3 monstruos como ejemplo y el tesoro
    def __init__(self, heroe):
        self.heroe = heroe
        self.monstruos = [
            Monstruo("Monstruo 1", 8, 3, 30),
            Monstruo("Monstruo 2", 10, 4, 40),
            Monstruo("Monstruo 3", 12, 5, 50)
        ]
        self.tesoro = Tesoro()

    #Creamos el metodo jugar
    def jugar(self):
        print("Héroe entra en la mazmorra.")
        for monstruo in self.monstruos: #Creamos un bucle que recorra los monstruos
            print(f"Te has encontrado con un {monstruo.nombre}.")
            self.enfrentar_enemigo(monstruo) #Hacmos que el heroe se enfrente al monstruo

            if not self.heroe.esta_vivo():  #Comprobamos que el heroe siga vivo, si no es así se termina el juego
                print("Héroe ha sido derrotado en la mazmorra.")
                return
            #En el caso de que el heroe siga vivo y haya ganado al monstruo conseguirá un tesoro
            self.buscar_tesoro()
        #Cuando gana a todos los monstruos mostramos un texto en pantalla que lo indique
        print(f"¡{self.heroe.nombre} ha derrotado a todos los monstruos y ha conquistado la mazmorra!")

    #Creamos el metodo enfrentar enemigo
    def enfrentar_enemigo(self, enemigo):
        #Mientras enemigo y heroe están vivos preguntamos si se quiere atacar, defender o curarse
        while enemigo.esta_vivo() and self.heroe.esta_vivo():
            print("\n¿Qué deseas hacer?")
            print("1. Atacar")
            print("2. Defender")
            print("3. Curarse")
            opcion = input("Elige una opción: ")

            if opcion == "1":
                self.heroe.atacar(enemigo) #El heroe ataca al enemigo
                if enemigo.esta_vivo(): #Si el enemigo sigue vivo este atacará al heroe
                    enemigo.atacar(self.heroe)
                self.heroe.reset_defensa()
            elif opcion == "2":
                self.heroe.defenderse() #El heroe se defiende del enemigo
                enemigo.atacar(self.heroe) #El enemigo ataca al heroe
            elif opcion == "3":
                self.heroe.curarse() #El heroe cura su salud
                enemigo.atacar(self.heroe) #El enemigo ataca al heroe
            else:
                print("Opción no válida.") #En caso de haber escogido una opción erronea se mostrará con este mensaje

    #Creamos el metodo buscar tesoro
    def buscar_tesoro(self):
        print("Buscando tesoro...")
        self.tesoro.encontrar_tesoro(self.heroe) #Invocamos el metodo encontrar tesoro de la clase tesoro