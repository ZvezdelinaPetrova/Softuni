# from project.product import Product
from oop.inheritance.exercise.project5.project.product import Product


class Food(Product):
    def __init__(self, name):
        super().__init__(name, 15)

