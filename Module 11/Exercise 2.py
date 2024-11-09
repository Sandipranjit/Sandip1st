import random
from car import Car

class ElectricCar(Car):
    def __init__(self, reg_num, max_speed, capacity):
        super().__init__(reg_num, max_speed)
        self.capacity = capacity

class GasolineCar(Car):
    def __init__(self, reg_num, max_speed, volume):
        super().__init__(reg_num, max_speed)
        self.volume = volume

e_car = ElectricCar("ABC-15", 180, 52.5)

g_car = GasolineCar("ACD-123", 165, 32.3)
list_of_cars = [e_car, g_car]

for car in list_of_cars:
    print("-" * 95 + "*")
    print("Initial information:")
    print(f" - Car: {car.reg_num} | Max speed: {car.max_speed} km/h | "
          f"Current speed: {car.current_speed} km/h | "
          f"Distance travelled: {car.distance} km |")

    car.accelerate(random.randint(10, 100))
    car.drive(3.)

    print("\nAfter driving:")
    print(f" - Car: {car.reg_num} | Max speed: {car.max_speed} km/h | "
          f"Current speed: {car.current_speed} km/h | "
          f"Distance travelled: {car.distance} km |")
    print("-" * 95 + "*")