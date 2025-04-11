class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
my_car = Car( "Toyota", "Corolla")  # Create an instance of the Car class
print(my_car.brand)  # Access the brand attribute
print(my_car.model)  # Access the model attribute
