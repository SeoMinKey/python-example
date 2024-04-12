class car:
    def __init__(self, name, gas_mileage, gas_liter):
        self.name = name
        self.gas_mileage = gas_mileage
        self.gas_liter = gas_liter

    def driving(self):
        km = self.gas_mileage * self.gas_liter
        self.gas_liter = 0
        print(f"Driving({self.name}): {km}km")
        return km
    
    def refueling(self, gas_refuel):
        self.gas_liter = gas_refuel
        print(f"Gas refuel({self.name}): {self.gas_liter}L")
        return self.gas_liter

a = car("aaa", 3, 18)
a.driving()
a.driving()
a.refueling(13)
a.driving()