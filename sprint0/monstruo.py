class Monstruo:
    #Definimos los atributos de la clase
    def __init__(self, nombre, ataque, defensa, salud):
        self.nombre = nombre
        self.ataque = ataque
        self.defensa = defensa
        self.salud = salud

    #Creamos el metodo atacar
    def atacar(self, heroe):
        print(f"El monstruo {self.nombre} ataca a {heroe.nombre}.")
        dano = self.ataque - heroe.defensa #Calculamos el daño del ataque restando el ataque del monstruo menos la defensa del heroe
        if dano > 0: #Si el daño es mayor que cero se le resta vida al heroe
            heroe.salud -= dano
            print(f"El héroe {heroe.nombre} ha recibido {dano} puntos de daño.")
        else: #Si el daño no es mayor que cero el heroe habrá bloqueado el ataque
            print(f"El héroe ha bloqueado el ataque.")

    #Creamos el metodo esta_vivo que devolverá true si la salud del monstruo es mayor que cero y false si no lo es
    def esta_vivo(self):
        return self.salud > 0