class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor #current floor set to bottom floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            print(f"Elevator is going up from floor '{self.current_floor}' to floor '{self.current_floor + 1}'.")
            self.current_floor += 1
            return True
        else:
            return False

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            print(f"Elevator is going down from floor '{self.current_floor}' to floor '{self.current_floor - 1}'.")
            self.current_floor -= 1
            return True
        else:
            return False

    def go_to_floor(self, floor_num):
        if floor_num < self.bottom_floor or floor_num > self.top_floor:
            print(f"Oops! No access to to floor '{floor_num}'.")
            return

        while self.current_floor != floor_num:
            if self.current_floor < floor_num:
                self.floor_up()
            else:
                self.floor_down()

def main():
    h = Elevator(1, 5)
    floor_num = int(input("Enter the floor number you want to go: "))
    print(f"Taking you to floor '{floor_num}' of your choice.")
    h.go_to_floor(floor_num)

    print(f"Let's return back to bottom floor.")
    h.go_to_floor(h.bottom_floor)

if __name__ == "__main__":
    main()
