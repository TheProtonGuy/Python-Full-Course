def car_info(brand, model):
    return f"{brand} {model}"

def start_car(brand, model):
    return f"{brand} {model} is starting..."

def stop_car(brand, model):
    return f"{brand} {model} is stopping..."

# Every time, we must pass brand & model again
print(car_info("Toyota", "Corolla"))
print(start_car("Toyota", "Corolla"))
print(stop_car("Toyota", "Corolla"))

# second car
print(car_info("Honda", "Civic"))
print(start_car("Honda", "Civic"))
print(stop_car("Honda", "Civic"))
