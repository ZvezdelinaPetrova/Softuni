# from oop.inheritance.lab.project5.project.cat import Cat

from project.cat import Cat

class Kitten(Cat):
    def __init__(self, name, age):
        super().__init__(name, age, "Female")

    def make_sound(self):
        return f"Meow"