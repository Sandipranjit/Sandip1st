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

    def drive(self, hours: float):
        self.distance += self.current_speed * hours
