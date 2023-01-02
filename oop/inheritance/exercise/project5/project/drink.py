# from project.product import Product
from oop.inheritance.exercise.project5.project.product import Product


class Drink(Product):
    def __init__(self, name):
        super().__init__(name, 10)

