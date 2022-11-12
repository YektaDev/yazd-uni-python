class Car():
    def __init__(self, color, model, year, fuelrate):
        self.color = color
        self.model = model
        self.year = year
        self.fuelrate = fuelrate
        self.fuel = 0

    def __str__(self):
        return f'{self.__class__.__name__}\nColor: {self.color}\nModel: {self.model}\nYear: {self.year}\nFuel Rate: {self.fuelrate}\nFuel: {self.fuel}'

    def refuel(self):
        self.fuel = 30


c1 = Car('White', 'Toyota', 2014, 0.07)
print(c1)

c1.refuel()
print(c1)


class Taxi(Car):
    def __init__(self, color, model, year, fuelrate, capacity, airport_flag):
        super().__init__(color, model, year, fuelrate)
        self.capacity = capacity
        self.airport_flag = airport_flag

    def __str__(self):
        return f'{super().__str__()}\nCapacity: {self.capacity}\nAirport: {self.airport_flag}'

    def refuel(self):
        self.fuel = 50


t1 = Taxi('Yellow', 'Pride', 1397, 0.08, 4, False)
print(t1)
t1.refuel()
print(t1)
