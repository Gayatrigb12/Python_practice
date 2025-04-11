class Car:
    def __init__(self, brand, model):
        self.__brand = brand # private attribute (should not be accessed directly outside the class)
        self.model = model
    def get_brand(self):
        return self.__brand + " !"
    def set_brand(self, brand):
        self.brand = brand
        
    def full_name(self):
        return f"{self.__brand} {self.model}"

    def fuel_type(self):
        return "Gasoline"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    def fuel_type(self):
        return "Electricity"

my_electric_car = ElectricCar("Tesla", "Model S", 100)  # Create an instance of the ElectricCar class
safari = Car("Tata", "safari")

print(safari.fuel_type())  # Access the fuel_type method    
print(my_electric_car.fuel_type())  # Access the fuel_type method