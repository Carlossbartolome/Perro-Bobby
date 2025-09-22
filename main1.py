from main import Perro

# Ejemplos de instancias de la clase Perro
if __name__ == "__main__":
    bobby = Perro("marrón", "Bobby", "Labrador")
    luna = Perro("negro", "Luna", "Pastor Alemán")
    max = Perro("blanco", "Max", "Poodle")

    bobby.menear()
    luna.ladrar()
    max.comer()
    print(f"Nombre: {max.get_nombre()}, Color: {max.get_color()}, Raza: {max.get_raza()}")
    rocky.ladrar()
    rocky.menear()
    print(f"Nombre: {rocky.get_nombre()}, Color: {rocky.get_color()}, Raza: {rocky.get_raza()}")
