class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    def accelerate(self, increment):
        self.speed += increment

    def brake(self, decrement):
        self.speed -= decrement

    def get_speed(self):
        return self.speed

# Creating objects of the Car class
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Accord", 2019)

# Accelerating car1
car1.accelerate(20)
print(f"Car1 speed: {car1.get_speed()} mph")

# Accelerating car2
car2.accelerate(30)
print(f"Car2 speed: {car2.get_speed()} mph")

# Braking car1
car1.brake(10)
print(f"Car1 speed after braking: {car1.get_speed()} mph")