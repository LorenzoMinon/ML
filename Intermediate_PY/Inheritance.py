# Parent class
class Animal:
    def __init__(self, name): # Constructor method, that is called when an object is created from the class and it allows the class to initialize the attributes of a class.
        self.name = name

    def speak(self): # Method that prints a generic message, self means that the method is bound to the object itself.
        print(f"{self.name} makes a sound.")

# Child class inheriting from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name) # Super method is used to call the constructor of the parent class and initialize the parent class attributes.
        self.breed = breed

    def speak(self):
        print(f"{self.name} barks.")

    def fetch(self):
        print(f"{self.name} fetches a ball.")

# Child class inheriting from Animal
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def speak(self):
        print(f"{self.name} meows.")

    def scratch(self):
        print(f"{self.name} scratches the furniture.")

Tito = Cat("Tito", "Naranja como gardfield")
print(Tito.name, "El color de tito es: ", Tito.color)

# Creating instances of the classes
animal = Animal("Generic Animal")
dog = Dog("Buddy", "Labrador")
cat = Cat("Whiskers", "Gray")

# Calling methods on the instances
animal.speak()  # Output: Generic Animal makes a sound.
dog.speak()     # Output: Buddy barks.
dog.fetch()     # Output: Buddy fetches a ball.
cat.speak()     # Output: Whiskers meows.
cat.scratch()   # Output: Whiskers scratches the furniture.