
class Vehicle:
    def __init__(self, make: str, model: str, year: int, rental_rate: int):

        assert year >= 0, f"Invalid input for year"
        assert rental_rate >= 0, f"Invalid input. The rental rate cannot be negative"

        self.make = make
        self.model = model
        self.year = year
        self.rental_rate = rental_rate
        self.available = True

    def __repr__(self):
        return f'{self.__class__.__name__}("{self.make}", "{self.model}", {self.year}, {self.rental_rate})'


class Car(Vehicle):
    def __init__(self, make: str, model: str, year: int, rental_rate: int, number_of_doors: int, seats: int):
        super().__init__(make, model, year, rental_rate)
        self.number_of_doors = number_of_doors
        self.seats = seats
    
    # Used to print of subclass Car instance as a string
    def __repr__(self):
        return f'{self.__class__.__name__}("{self.make}", "{self.model}", {self.year}, {self.rental_rate}, {self.number_of_doors}, {self.seats})'


class Truck(Vehicle):
    def __init__(self, make: str, model: str, year: int, rental_rate: int, bed_size: str, towing_capacity: int):
        super().__init__(make, model, year, rental_rate)
        self.bed_size = bed_size
        self.towing_capacity = towing_capacity

    # Used to print of subclass Truck instance as a string
    def __repr__(self):
        return f'{self.__class__.__name__}("{self.make}", "{self.model}", {self.year}, {self.rental_rate}, {self.bed_size}, {self.towing_capacity})'


class Motorcycle(Vehicle):
    def __init__(self, make: str, model: str, year: int, rental_rate: int, engine_size: float):
        super().__init__(make, model, year, rental_rate)
        self.engine_size = engine_size
    
    # Used to print of subclass Motorcycle instance as a string
    def __repr__(self):
        return f'{self.__class__.__name__}("{self.make}", "{self.model}", {self.year}, {self.rental_rate}, {self.engine_size})'