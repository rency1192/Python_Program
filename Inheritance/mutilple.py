class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        return f"{self.make} {self.model}"

class ElectricEngine:
    def __init__(self, battery_capacity):
        self.battery_capacity = battery_capacity

    def display_engine_info(self):
        return f"Electric Engine, Battery Capacity: {self.battery_capacity} kWh"

class GasolineEngine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type

    def display_engine_info(self):
        return f"Gasoline Engine, Fuel Type: {self.fuel_type}"

class HybridCar(Vehicle, ElectricEngine, GasolineEngine):
    def __init__(self, make, model, battery_capacity, fuel_type):
        Vehicle.__init__(self, make, model)
        ElectricEngine.__init__(self, battery_capacity)
        GasolineEngine.__init__(self, fuel_type)

    def display_info(self):
        vehicle_info = super().display_info()
        engine_info = f"{ElectricEngine.display_engine_info(self)} and {GasolineEngine.display_engine_info(self)}"
        return f"{vehicle_info} with {engine_info}"

# Example of Multiple Inheritance
hybrid_car = HybridCar("Toyota", "Prius", battery_capacity=30, fuel_type="Regular Gasoline")

# Display information
print(hybrid_car.display_info())
