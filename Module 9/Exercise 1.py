class Car:
    def __init__(self, reg_num: str, max_speed: int, current_speed, distance):
        self.reg_num = reg_num
        self.max_speed = max_speed
        self.current_speed = 0
        self.distance = 0

car = Car("ABC-123", 142, 0, 0)
print(f"This car's registration number is: '{car.reg_num}'. \nIt has maximum speed of {car.max_speed} km/h. "
          f"\nIt's current speed and distance are {car.current_speed} km/h and {car.distance} km respectively.")