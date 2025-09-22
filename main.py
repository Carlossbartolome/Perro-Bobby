# Clase Perro
class Perro:
    def __init__(self, color, nombre, raza):
        self.__color = color
        self.__nombre = nombre
        self.__raza = raza

    # Getters
    def get_color(self):
        return self.__color

    def get_nombre(self):
        return self.__nombre

    def get_raza(self):
        return self.__raza

    # Setters
    def set_color(self, color):
        self.__color = color

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_raza(self, raza):
        self.__raza = raza

    def menear(self):
        print(f"{self.__nombre} está meneando la cola.")

    def ladrar(self):
        print(f"{self.__nombre} está ladrando: ¡Guau guau!")

    def comer(self):
        print(f"{self.__nombre} está comiendo.")

