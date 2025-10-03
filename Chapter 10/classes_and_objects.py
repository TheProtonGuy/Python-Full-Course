class Car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def details(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}")
        self.brand = 'BMW'
        self.model = 'M4'
        self.year = 2024
        self.color = 'Black'

        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, color: {self.color}")

    def start_car(self):
        print(f"{self.brand} {self.model} is starting...")

    def stop_car(self):
        return f"{self.brand} {self.model} is stopping..."


first_car = Car("Toyota", "Camry", 2025)
first_car.details()
# first_car.start_car()
# print(first_car.stop_car())

# print('\n\n')

# second_car = Car("Ford", "Explorer", 2015)
# second_car.details()
# second_car.start_car()
# print(second_car.stop_car())