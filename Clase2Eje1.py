class Image:
    def __init__(self, width, height, background_color):
        # Atributos de la imagen
        self.width = width
        self.height = height
        self.background_color = background_color
        self.canvas = [[background_color for _ in range(width)] for _ in range(height)]
        self.shapes = []
        self.text = []
        self.colors = ["black", "red", "green", "blue"]
        self.paint = False
        self.paint_color = None

    def draw_shape(self, shape, color, position):   # Método para dibujar una forma geométrica en la imagen.                                     
        pass

    def add_text(self, text, color, position):  # Método para agregar texto en la imagen.
        pass

    def paint_mode_on(self, color): # Método para activar el modo de pintura con el color proporcionado.
        pass

    def paint_mode_off(self):  # Método para desactivar el modo de pintura.
        pass

    def fill_area(self, color, position):  # Método para rellenar un área contigua con el color especificado a partir de la posición dada.
        pass

    def create_color(self, red, green, blue):  # Método para crear un nuevo color personalizado a partir de los valores RGB proporcionados.
        pass

    def clear_canvas(self):  # Método para borrar todo el contenido de la imagen, restaurando el fondo original.
        pass

# Ejemplo de uso:
width, height = 800, 600
background_color = "white"

image = Image(width, height, background_color)  #Para poder realizar muchas mas opciones con este ejemplo se necesita importar una libreria.
                                                
