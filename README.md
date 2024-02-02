# Car Class Project

## Introduction

This project is a simple Python program that demonstrates the use of classes and inheritance to model electric and gas cars. The project consists of three classes: `Car`, `ElectricCar`, and `GasCar`. Each class represents a different type of car with specific attributes and methods.

## Classes

### `Car`

The base class representing a generic car with attributes such as name, model, and year.

#### Methods:

- `__init__(self, name, model, year)`: Initializes a Car instance with the provided name, model, and year.
- `display_info(self)`: Displays basic information about the car.

### `ElectricCar`

A derived class from `Car`, representing an electric car. It includes an additional attribute for battery capacity.

#### Methods:

- `__init__(self, name, model, year, battery_capacity)`: Initializes an ElectricCar instance with the provided name, model, year, and battery capacity.
- `display_info(self)`: Displays information about the electric car, including battery capacity.

### `GasCar`

Another derived class from `Car`, representing a gas car. It includes an additional attribute for fuel efficiency.

#### Methods:

- `__init__(self, name, model, year, fuel_efficiency)`: Initializes a GasCar instance with the provided name, model, year, and fuel efficiency.
- `display_info(self)`: Displays information about the gas car, including fuel efficiency.


