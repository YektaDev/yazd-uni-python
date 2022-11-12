class Car():
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed
        self.xloc = 0
        self.yloc = 0
        self.fuel = 0
        self.fuelrate = 0.2

    def set_speed(self, speed):
        self.speed = speed

    def move_forward(self, step):
        needed_fuel = step * self.fuelrate
        if self.fuel >= needed_fuel:
            self.yloc += step
            self.fuel -= needed_fuel
        else:
            print('Not enough fuel to move!')

    def move_backward(self, step):
        needed_fuel = step * self.fuelrate
        if self.fuel >= needed_fuel:
            self.yloc -= step
            self.fuel -= needed_fuel
            if self.yloc < 0:
                self.yloc = 0
        else:
            print('Not enough fuel to move!')

    def refuel(self):
        self.fuel = 100


car1 = Car('red', 120)
car2 = Car('Black', 160)
print(car1)

print(car1.xloc, car1.yloc, car1.speed, car1.fuel)
car1.move_forward(10)
print(car1.xloc, car1.yloc, car1.speed, car1.fuel)

car1.refuel()
car1.move_forward(30)
print(car1.xloc, car1.yloc, car1.speed, car1.fuel)
car1.move_backward(30)
print(car1.xloc, car1.yloc, car1.speed, car1.fuel)
car1.move_forward(100)
print(car1.xloc, car1.yloc, car1.speed, car1.fuel)
