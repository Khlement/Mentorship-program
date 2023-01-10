class Fleet:
    def __init__(self, name: str):
        self.name = name
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def remove_vehicle(self, vehicle):
        self.vehicles.remove(vehicle)

    def list_vehicles(self):
        for vehicle in self.vehicles:
            print(vehicle)

    def rent_vehicle(self, vehicle):
        if vehicle.available:
            vehicle.available = False
        else:
            print("Sorry, this vehicle is currently rented.")

    def return_vehicle(self, vehicle):
        if not vehicle.available:
            vehicle.available = True
        else:
            print("This vehicle is not currently rented.")

    def calculate_revenue(self):
        revenue = 0
        for vehicle in self.vehicles:
            if not vehicle.available:
                revenue += vehicle.rental_rate
        return revenue
