class Dog:  # Esta clase representa un perro.
    def __init__(self, name, color, age, weight):
        # Atributos del perro.
        self.name = name
        self.color = color
        self.age = age
        self.weight = weight

    def bark(self, person): # Método para que el perro ladre cuando ve llegar a una persona.
        print(f"{self.name} barks when it sees {person} coming.")

    def wag_tail(self): # Método para que el perro mueva la cola cuando es acariciado en la cabeza.
        print(f"{self.name} wags its tail when petted on the head.")

    def poop(self): # Método para que el perro haga caca cuando le dan de comer muchas croquetas.
        print(f"{self.name} poops when given a lot of dog food.")

# Pedir datos del perro al usuario.
dog_name = input("Enter the dog's name: ")
dog_color = input("Enter the dog's color: ")
dog_age = int(input("Enter the dog's age: "))
dog_weight = float(input("Enter the dog's weight: "))

# Crear una instancia de la clase Perro con los datos proporcionados por el usuario.
user_dog = Dog(dog_name, dog_color, dog_age, dog_weight)

# Ejemplo de uso e interacción con el perro ingresado por el usuario.
print("\nInteracting with the dog!")
user_dog.bark("the neighbor")
user_dog.wag_tail()
user_dog.poop()
