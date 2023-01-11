from fleet import Fleet 
from vehicle import Car, Vehicle, Truck, Motorcycle

Car1 = Car('Toyota', 'Camry', 2019, 100, 4, 4)
Car2 = Car('Honda', 'Civic', 2018, 87, 4, 4 )
fleet1 = Fleet('group1')
fleet1.addVehicle(Car1)
fleet1.addVehicle(Car2)
fleet1.rentVehicle(Car1)
fleet1.rentVehicle(Car2)
revenue= fleet1.calculateRevenue()
print(revenue)




