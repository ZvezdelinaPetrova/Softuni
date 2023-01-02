import unittest

from project.mammal import Mammal


class TestMammal(unittest.TestCase):
    def test_initialization(self):
        mammal = Mammal("Deli", "female", "boo")
        self.assertEqual("Deli", mammal.name)
        self.assertEqual("female", mammal.type)
        self.assertEqual("boo", mammal.sound)
        self.assertEqual("animals", mammal._Mammal__kingdom)

    def test_make_sound(self):
        mammal = Mammal("Deli", "female", "boo")
        expected = mammal.make_sound()
        self.assertEqual(expected, f"Deli makes boo")

    def test_get_kingdom(self):
        mammal = Mammal("Deli", "female", "boo")
        mammal._Mammal__kingdom = "test"
        expected = mammal.get_kingdom()
        self.assertEqual(expected, f"test")

    def test_info(self):
        mammal = Mammal("Deli", "female", "boo")
        expected = mammal.info()
        self.assertEqual(expected, f"Deli is of type female")


if __name__ == '__main__':
    unittest.main()