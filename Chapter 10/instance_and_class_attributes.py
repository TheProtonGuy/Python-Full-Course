class Car:

    # class attribute
    number_of_doors = 4

    def __init__(self, brand, model, year):
        # instance attributes 
        self.brand = brand
        self.model = model
        self.year = year

    def details(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}")

first_car = Car("Toyota", "Camry", 2025)
first_car.details()
print(first_car.number_of_doors)

print('\n\n')

second_car = Car("Ford", "Explorer", 2015)
second_car.details()
print(second_car.number_of_doors)