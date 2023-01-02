# from oop.inheritance.lab.project3.project.employee import Employee
# from oop.inheritance.lab.project3.project.person import Person

from project.cat import Employee
from project.car import Person


class Teacher(Person, Employee):
    def teach(self):
        return "teaching..."