import random

class Car:
    def __init__(self, reg_num: str, max_speed: int):
        self.reg_num = reg_num
        self.max_speed = max_speed
        self.current_speed = 0
        self.travel_distance = 0

    def accelerate(self, change_in_speed):
        self.current_speed += change_in_speed
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours: float):
        self.travel_distance += self.current_speed * hours

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            car.accelerate(random.randint(-10,15))
            car.drive(1.)

    def print_status(self):
        print(self.name + ":")
        print("\nRegistration | Speed (km/h) | Distance (km) ")
        print("-" * 43)
        for car in self.cars:
            print(f"    {car.reg_num:6s}   | {car.current_speed:3d} km/h     |  {car.travel_distance} km")
            print("-" * 43)

    def race_finished(self):
        for car in self.cars:
            if car.travel_distance >= self.distance:
                return True
            return False

cars = []
for i in range(10):
    cars.append(Car("ABC-" + str(i + 1), random.randint(100,200)))

race1 = Race("\nGrand Demolition Derby", 8000., cars)
hours = 0
while not race1.race_finished():
    race1.hour_passes()
    hours += 1

    if hours % 10 == 0:
        print(f"\nResults of the race after {hours} hours: ")
        race1.print_status()

print(f"\nFinal results, after {hours} hours: ")
race1.print_status()

