# from oop.encapsulation.exercise.project1.project.worker import Worker

from project.pizza import Worker



class Caretaker(Worker):
    def __init__(self, name, age, salary):
        super().__init__(name, age, salary)