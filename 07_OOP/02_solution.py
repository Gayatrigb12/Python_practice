class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def full_name(self):
        return f"{self.brand} {self.model}"
    
my_car = Car( "Toyota", "Corolla")  # Create an instance of the Car class
print(my_car.brand)  # Access the brand attribute
print(my_car.model)  # Access the model attribute

print(my_car.full_name())  # Access the full_name method