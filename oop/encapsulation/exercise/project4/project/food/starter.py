# from oop.encapsulation.exercise.project4.project.food.food import Food

from project.car.food import Food


class Starter(Food):
    def __init__(self, name, price, grams):
        super().__init__(name, price, grams)