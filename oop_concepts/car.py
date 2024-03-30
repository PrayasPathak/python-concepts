class Car:
    total_car = 0

    def __init__(self, brand, model):
        # Encapsulation
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    # Getters

    def get_brand(self):
        return self.__brand

    # Setter

    def set_brand(self, value):
        self.__brand = value

    def full_name(self):
        return f"{self.__brand} {self.__model}"

    def fuel_type(self):
        return "Petrol or Diesel"

    @staticmethod
    def general_description():
        return "Means of transportation"

    # Property
    @property
    def model(self):
        return self.__model


class Battery:
    def battery_info(self):
        print("This is battery")


class Engine:
    def engine_info(self):
        print("This is engine")


class ElectricCar(Car, Battery, Engine):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.__battery_size = battery_size

    def get_battery_size(self):
        return self.__battery_size

    def set_battery_size(self, value):
        self.__battery_size = value

    # Polymorphism
    def fuel_type(self):
        return "Electric Charge"


tata_safari = Car("Tata", "Safari")
print(tata_safari.full_name())


tesla = ElectricCar("Tesla", "Model S", "85KWh")
print(tesla)
# Accessing attributes
# print(f"Brand Name = {tesla.__brand}")
print(f"Brand Name = {tesla.get_brand()}")
# print(f"Battery Size = {tesla.__battery_size}")
print(tesla.full_name())

tesla.set_brand("Audi")
print(tesla.get_brand())

print(tesla.fuel_type())
print(tata_safari.fuel_type())

print(f"Total Number of cars = {Car.total_car}")
print(tesla.general_description())
print(Car.general_description())

print(tesla.model)

print(f"Is tesla an instance of Car? {isinstance(tesla, Car)}")
print(f"Is tesla an instance of ElectricCar? {isinstance(tesla, ElectricCar)}")

# Multiple Inheritance
tesla.battery_info()
tesla.engine_info()
