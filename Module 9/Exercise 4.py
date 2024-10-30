import random
class Car:
    def __init__(self, reg_num: str, max_speed: int):
        self.reg_num = reg_num
        self.max_speed = max_speed
        self.current_speed = 0
        self.distance = 0

    def accelerate(self, change_in_speed):
        #self.current_speed = min(max(self.current_speed + change_in_speed, 0), self.max_speed)
        self.current_speed += change_in_speed
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours: float):
        self.distance += self.current_speed * hours

if __name__ == "__main__":      #main program
    car = Car('ABC-123', 142)       #Creating new car
    print(f"This car's registration number is: '{car.reg_num}'. \nIt has maximum speed of {car.max_speed} km/h. "
          f"\nIt's current speed and distance are {car.current_speed} km/h and {car.distance} km respectively.")

    #Accelerating the car
    car.accelerate(30)
    print(f"Your car's initial speed is {car.current_speed} km/h.")
    car.accelerate(70)
    print(f"Now, your car's current speed is {car.current_speed} km/h.")
    car.accelerate(50)
    print(f"Your car's current speed is {car.current_speed} km/h.")
    car.accelerate(-200)
    print(f"Your car's final speed is {car.current_speed} km/h.")

    car.accelerate(60)
    car.drive(1.5)
    print(f"Your car's current distance is {car.distance} km.")

    cars = []       #Creating list of cars for the race
    for i in range(10):
        cars.append(Car("ABC-" + str (i+1), random.randint(100,200)))

    max_distance = 0        #Distance set to Zero as per question
    winner = None
    while max_distance < 10_000:
        for car in cars:
            car.accelerate(random.randint(-10,15))
            car.drive(1)

            if car.distance > max_distance:
                max_distance = car.distance
                winner = car

    print("-" * 80)

    print(f"{'Registration':<10} | {'Max Speed (km/h)':10} |"
          f" {'Current Speed (km/h)':<20} | {'Travelled Distance (km)':<22}")

    print("-" * 80)

    for car in cars:
        print(f"    {car.reg_num:<8} |     {car.max_speed:<3} km/h     |"
              f"     {car.current_speed:<3} km/h         |        {car.distance:<3} km")

        print("-" * 80)

    print(f"\nWinner of the race is Car: '{winner.reg_num}' with distance of {winner.distance} km. Congratulations!")



