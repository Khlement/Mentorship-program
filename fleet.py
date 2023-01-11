class Fleet:
    def __init__(self, name: str):
        self.name = name
        self.vehicles = []

    def addVehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def removeVehicle(self, vehicle):
        self.vehicles.remove(vehicle)

    def listVehicles(self):
        print(self.vehicles)

    def rentVehicle(self, vehicle):
        if vehicle.available:
            vehicle.available = False
        else:
            print("Vehicle currently out for rent.")

    def returnVehicle(self, vehicle):
        if not vehicle.available:
            vehicle.available = True
        else:
            print("This vehicle is not rented.")

    def calculateRevenue(self):
        revenue = 0
        for vehicle in self.vehicles:
            if not vehicle.available:
                revenue += vehicle.rental_rate
        return revenue
