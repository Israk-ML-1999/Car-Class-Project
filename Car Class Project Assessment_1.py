class Car:
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.name} {self.model}"


class ElectricCar(Car):
    def __init__(self, name, model, year, battery_capacity):
        super().__init__(name, model, year)
        self.battery_capacity = battery_capacity

    def display_info(self):
        car_info = super().display_info()
        return f"{car_info}\nBattery Capacity: {self.battery_capacity} kWh"


class GasCar(Car):
    def __init__(self, name, model, year, fuel_efficiency):
        super().__init__(name, model, year)
        self.fuel_efficiency = fuel_efficiency

    def display_info(self):
        car_info = super().display_info()
        return f"{car_info}\nFuel Efficiency: {self.fuel_efficiency} MPG"


def main():
    car_type = input("Enter car type (Electric/Gas): ").capitalize()
    name = input("Enter Name: ")
    model = input("Enter model: ")
    year = int(input("Enter year: "))

    if car_type == "Electric":
        battery_capacity = float(input("Enter battery capacity (kWh): "))
        electric_car = ElectricCar(name, model, year, battery_capacity)
        print("\nCar Information:")
        print(electric_car.display_info())
    elif car_type == "Gas":
        fuel_efficiency = float(input("Enter fuel efficiency (MPG): "))
        gas_car = GasCar(name, model, year, fuel_efficiency)
        print("\nCar Information:")
        print(gas_car.display_info())
    else:
        print("Invalid car type plase selict GAs or elitricr than run the code ")


if __name__ == "__main__":
    main()
