class Car:
    total_cars = 0  # Class variable to keep track of the number of cars
    def __init__(self, brand, model):
        self.__brand = brand # private attribute (should not be accessed directly outside the class)
        self.model = model
        Car.total_cars += 1
        # self.__class__.total_cars += 1  # Increment the class variable for each instance created
    def get_brand(self):
        return self.__brand + " !"
    def set_brand(self, brand):
        self.brand = brand
        
    def full_name(self):
        return f"{self.__brand} {self.model}"

    def fuel_type(self):
        return "Gasoline"
    @staticmethod
    def general():
        return "This is a car class"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    def fuel_type(self):
        return "Electricity"
    
my_Car = Car("Toyota", "Corolla")  # Create an instance of the Car class
Car("Honda", "Civic")  # Create another instance of the Car class

# print(my_Car.general())  # Access the brand attribute
print(Car.general())  # Access the model attribute
print(Car.total_cars)  # Access the class variable to get the total number of cars created