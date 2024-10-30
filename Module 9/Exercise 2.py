class Car:
    def __init__(self, reg_num: str, max_speed: int):
        self.reg_num = reg_num
        self.max_speed = max_speed
        self.current_speed = 0
        self.distance = 0

    def accelerate(self, change_in_speed: int):
        self.current_speed += change_in_speed
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0

car = Car("ABC-123", 142)
print(f"This car's registration number is: '{car.reg_num}'. \nIt has maximum speed of {car.max_speed} km/h. "
          f"\nIt's current speed and distance are {car.current_speed} km/h and {car.distance} km respectively.")

car.accelerate(30)
print(f"Your car's initial speed is {car.current_speed} km/h.")
car.accelerate(70)
print(f"Now, your car's current speed is {car.current_speed} km/h.")
car.accelerate(50)
print(f"Your car's current speed is {car.current_speed} km/h.")
car.accelerate(-200)
print(f"Your car's final speed is {car.current_speed} km/h.")