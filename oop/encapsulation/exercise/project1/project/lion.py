# from oop.encapsulation.exercise.project1.project.animal import Animal

from project.car import Animal

class Lion(Animal):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender, 50)
