# from oop.inheritance.lab.project1.project.food import Food

from project.car import Food


class Fruit(Food):
    def __init__(self, name, expiration_date):
        self.name = name
        super().__init__(expiration_date)



