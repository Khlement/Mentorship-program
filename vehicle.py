
class Vehicle:
    def __init__(self, make: str, model: str, year: int, rental_rate: int):

        assert year >= 0, f"Invalid input for year"
        assert rental_rate >= 0, f"Invalid input. The rental rate cannot be negative"

        self.make = make
        self.model = model
        self.year = year
        self.rental_rate = rental_rate
        self.available = True

class Car(Vehicle):
    def __init__(self, make: str, model: str, year: int, rental_rate: int, number_of_doors: int, seats: int):
        super().__init__(make, model, year, rental_rate)
        self.number_of_doors = number_of_doors
        self.seats = seats

class Truck(Vehicle):
    def __init__(self, make: str, model: str, year: int, rental_rate: int, bed_size: str, towing_capacity: int):
        super().__init__(make, model, year, rental_rate)
        self.bed_size = bed_size
        self.towing_capacity = towing_capacity