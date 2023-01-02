class ImageArea:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        area = self.width * self.height
        return area

    def __eq__(self, other):  # equal
        if self.get_area() == other.get_area():
            return True
        return False

    def __ne__(self, other):  # not equal
        return self.get_area() != other.get_area()

    def __ge__(self, other):   # greater or equal
        return self.get_area() >= other.get_area()

    def __le__(self, other):  # less or equal
        return self.get_area() <= other.get_area()

    def __lt__(self, other):  # less than
        return self.get_area() < other.get_area()

    def __gt__(self, other):  # greater than
        return self.get_area() > other


a1 = ImageArea(7, 10)
a2 = ImageArea(35, 2)
a3 = ImageArea(8, 9)

print(a1 == a2)
print(a1 != a3)


a1 = ImageArea(7, 10)
a2 = ImageArea(35, 2)
a3 = ImageArea(8, 9)
print(a1 != a2)
print(a1 >= a3)

a1 = ImageArea(7, 10)
a2 = ImageArea(35, 2)
a3 = ImageArea(8, 9)
print(a1 <= a2)
print(a1 < a3)
