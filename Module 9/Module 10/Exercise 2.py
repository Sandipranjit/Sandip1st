from elevator import Elevator

class Building:
    def __init__(self, bottom_floor, top_floor, elevator_num):
        self.property = []
        for i in range(elevator_num):
            self.property.append(Elevator(bottom_floor, top_floor))

    def run_elevator(self, elevator_num, destination_floor):
        if elevator_num < 1 or elevator_num >len(self.property):
            print(f"Elevator {elevator_num} does not exist.")
            return
        print(f"Elevator number '{elevator_num}' is being used.")
        self.property[elevator_num - 1].go_to_floor(destination_floor)

building1 = Building(1,7,4)

building1.run_elevator(1,1)

building1.run_elevator(2,5)

building1.run_elevator(4,3)

