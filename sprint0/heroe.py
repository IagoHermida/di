class Heroe:
    #Creamos los atributos de la clase
    def __init__(self, nombre):
        self.nombre = nombre
        self.ataque = 10
        self.defensa = 5
        self.salud = 100
        self.salud_maxima = 100
        self.defensa_aumentada = False

    #Creamos el metodo atacar
    def atacar(self, enemigo):
        print(f"Héroe ataca a {enemigo.nombre}.")
        #Asignamos a dano el valor entre el ataque del heroe menos la defensa del enemigo
        dano = self.ataque - enemigo.defensa
        if dano > 0: #Si el daño es mayor que 0 actualizamos la salud del enemigo
            enemigo.salud -= dano
            print(f"El enemigo {enemigo.nombre} ha recibido {dano} puntos de daño.")
        else: #Si daño no es mayor que 0 el enemigo habrá bloqueado el ataque
            print(f"El enemigo ha bloqueado el ataque.")

    #Creo el metodo curarse
    def curarse(self):
        curacion = 20 #Le asigno un valor de curacion de 20
        self.salud += curacion #Añadimos el valor de curación a la salud total del heroe
        if self.salud > self.salud_maxima: #En caso de que la salud sea mayor que la salud máxima se quedará en esta ya que no puede superarla
            self.salud = self.salud_maxima
        print(f"Héroe se ha curado. Salud actual: {self.salud}")

    #Creamos el método defenderse
    def defenderse(self):
        self.defensa += 5 #Se añaden 5 puntos a la defensa del heroe
        self.defensa_aumentada = True #Marcamos que la defensa ha sido aumentada para después restablecerla a la defensa original
        print(f"Héroe se defiende. Defensa aumentada temporalmente a {self.defensa}.")

    #Ceramos el metodo reset_defensa
    def reset_defensa(self):
        if self.defensa_aumentada: #Comprobamos si defensa_aumentada tiene el valor true
            self.defensa -= 5 #Restablecemos la defensa a su valor inicial
            self.defensa_aumentada = False #Marcamos que la defensa ya no está aumentada
            print(f"La defensa de {self.nombre} vuelve a la normalidad.")

    #Creamos el metodo esta_vivo que simplemente devolverá si la salud es mayor (true) o no (false) que 0
    def esta_vivo(self):
        return self.salud > 0