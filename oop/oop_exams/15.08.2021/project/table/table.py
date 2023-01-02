from abc import ABC, abstractmethod

from project.baked_food.baked_food import BakedFood
from project.drink.drink import Drink


class Table(ABC):
    @abstractmethod
    def __init__(self, table_number: int, capacity: int):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders = []  # contain every food order made from the table
        self.drink_orders = []  # contain every drink order made from the table
        self.number_of_people = 0  # the count of people who sit at the table
        self.is_reserved = False

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError(f"Capacity has to be greater than 0!")
        self.__capacity = value

    def reserve(self, number_of_people: int):
        if self.is_reserved or number_of_people > self.capacity:
            return
        self.is_reserved = True
        self.number_of_people = number_of_people

    def order_food(self, baked_food: BakedFood):
        self.food_orders.append(baked_food)

    def order_drink(self, drink: Drink):
        self.drink_orders.append(drink)

    def get_bill(self):
        total = ""
        for x in self.food_orders:
            total += x.price
        for y in self.drink_orders:
            total += y.price
        return total

    def clear(self):
        self.food_orders.clear()
        self.drink_orders.clear()
        self.number_of_people = 0
        self.is_reserved = False

    def free_table_info(self):
        result = ""
        if not self.is_reserved:
            result += f"Table: {self.table_number}" + "\n"
            result += f"Type: {self.__class__.__name__}" + "\n"
            result += f"Capacity: {self.capacity}"
        return result
