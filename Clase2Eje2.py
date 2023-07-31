
class Flower:     # Esta clase representa una flor.

    
    name: str   # El nombre de la flor.
    color: str  # El color de la flor.
    height: int  # La altura de la flor en centímetros.
    number_of_petals: int    # El número de pétalos de la flor.

    # Se inicializa la flor con el nombre, color, altura y número de pétalos dados.
    def __init__(self, name: str, color: str, height: int, number_of_petals: int):
        self.name = name
        self.color = color
        self.height = height
        self.number_of_petals = number_of_petals

    def get_name(self) -> str:  # Devuelve el nombre de la flor.
        return self.name
    
    def get_color(self) -> str: # Devuelve el color de la flor.
        return self.color

    def get_height(self) -> int:    # Devuelve la altura de la flor en centímetros.
        return self.height

    def get_number_of_petals(self) -> int:   # Devuelve el número de pétalos de la flor.
        return self.number_of_petals

# Se crear una instancia con la clase Flower con información de una flor específica.
rose = Flower(name="Rosa", color="rojo", height=50, number_of_petals=20)

# Se imprime información sobre la flor.
print("Nombre de la flor:", rose.get_name())
print("Color de la flor:", rose.get_color())
print("Altura de la flor (cm):", rose.get_height())
print("Número de pétalos:", rose.get_number_of_petals())
