import random

class Tesoro:
    #Definimos los posibles beneficios de encontrar el tesoro en un array
    def __init__(self):
        self.beneficios = ["aumento de ataque", "aumento de defensa", "restauración de salud"]

    #Creamos el metodo encontrar tesoro
    def encontrar_tesoro(self, heroe):
        beneficio = random.choice(self.beneficios) #El beneficio se seleccionará de forma aleatoria usando random.choice
        print(f"Héroe ha encontrado un tesoro: {beneficio}.")
        #Dependiendo de qué baneficio haya tocado le daremos una u otra ventaja al heroe
        if beneficio == "aumento de ataque":
            heroe.ataque += 5 #Sumamos 5 puntos al ataque del heroe
            print(f"El ataque de {heroe.nombre} aumenta a {heroe.ataque}.")
        elif beneficio == "aumento de defensa":
            heroe.defensa += 5 #Sumamos 5 puntos a la defensa del heroe
            print(f"La defensa de {heroe.nombre} aumenta a {heroe.defensa}.")
        elif beneficio == "restauración de salud":
            heroe.salud = heroe.salud_maxima #Restauramos la salud de heroe
            print(f"La salud de {heroe.nombre} ha sido restaurada a {heroe.salud_maxima}.")