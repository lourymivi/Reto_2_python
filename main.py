class JuegoReparastetumoto:
    def __init__(self):
        self.finales ="¡Felicidades! Has reparado tu moto y te has convertido en un buen mecanico.",
        "Ya puedes volver al camino a casa. Fin del juego." "Fin del juego."
        self.actual = 0

    def iniciar_juego(self):
        print("\n¡Bienvenido a REPARA TU MOTO!")
        print("\nLas decisiones que tomes durante el juego te llevaran a arreglar o dañar tu moto.")

        while self.actual != -1:
            self.mostrar_nombre()
            self.mostrar_situacion()
            self.tomar_decision()

    def mostrar_nombre(self):
        nombre = input("Ingresa tu nombre: ") .lower()

    def mostrar_situacion(self):
        print("\Empecemos!\n\n" + nombre + ", vas en tu moto hacia tu casa pero en el camino se te rompe la cadena debes hacer algo antes que caiga la noche. Tienes dos opciones:\n" )
        print("1.Buscar el kit de herramientas.\n2. Pedir ayuda")
        print("¿Qué quieres hacer?")

    def tomar_decision(self):
        decision = input("Escribe tu eleccion, seleccionando el numero ") .lower()
        
        # Aquí puedes agregar lógica para manejar diferentes decisiones y eventos en la historia.
        # Puedes usar estructuras condicionales para determinar qué sucede a continuación.

        if "1" in decision:
            self.actual = 1  # Cambia el estado a 1 para representar la exploración de la cueva.
        
        else:
            print("Perdiste. Esta solo. Nadie te puede ayudar.")
             
        def mostrar_continuacion(self):
            print (nombre + ", en el kit encontraras varias herramientas debes elegir una de ellas para reparar la averia\n")
            print ("1ra: DESTORNILLADOR \n2da: DESPINADOR \n3ra: PRENSA")
        
        

        if self.actual == len(self.finales):
            print("¡Felicidades! Has alcanzado uno de los finales:")
            print(self.finales[self.actual - 1])
            self.actual = -1
        elif self.actual == -1:
            print("Fin del juego.")
        else:
            print("Continuemos la aventura...")

if __name__ == "__main__":
    juego = JuegoReparastetumoto()
    juego.iniciar_juego()
