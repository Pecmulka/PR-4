class Vehicle:
    def start(self):
        return "Starting the vehicle"

    def stop(self):
        return "Stopping the vehicle"

class Car(Vehicle):
    def start(self):
        return "Starting the car engine"

class Bicycle(Vehicle):
    def start(self):
        return "Pedaling the bicycle"

vehicle = Vehicle()
print(vehicle.start())  # Starting the vehicle
print(vehicle.stop())   # Stopping the vehicle

car = Car()
print(car.start())      # Starting the car engine
print(car.stop())       # Stopping the vehicle (наследуется от Vehicle)

bike = Bicycle()
print(bike.start())     # Pedaling the bicycle
print(bike.stop())      # Stopping the vehicle (наследуется от Vehicle)