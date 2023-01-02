import unittest

from project.factory.factory import Factory
from project.factory.paint_factory import PaintFactory


class PlantationTest(unittest.TestCase):

    def test_initialization(self):
        factory = PaintFactory("Fac", 10)
        self.assertEqual("Fac", factory.name)
        self.assertEqual(10, factory.capacity)
        self.assertEqual({}, factory.ingredients)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], factory.valid_ingredients)
        self.assertEqual({}, factory.products)

    def test_add_ingredient_error(self):
        factory = PaintFactory("Fac", 2)
        with self.assertRaises(ValueError) as ex:
            factory.add_ingredient("white", 4)
        self.assertEqual("Not enough space in factory", str(ex.exception))

    def test_add_ingredient_success(self):
        factory = PaintFactory("Fac", 10)
        factory.ingredients = {}
        factory.add_ingredient("white", 4)
        self.assertEqual({"white": 4}, factory.ingredients)

    def test_add_ingredient_error_2(self):
        factory = PaintFactory("Fac", 10)
        with self.assertRaises(TypeError) as ex:
            factory.add_ingredient("b", 4)
        self.assertEqual(f"Ingredient of type b not allowed in PaintFactory", str(ex.exception))

    def test_remove_ingredient_error(self):
        factory = PaintFactory("Fac", 10)
        factory.ingredients = {"v": 1}
        with self.assertRaises(KeyError) as ex:
            factory.remove_ingredient("b", 4)
        self.assertEqual(f"No such ingredient in the factory", str(ex.exception))

    def test_remove_ingredient_error_quantity(self):
        factory = PaintFactory("Fac", 5)
        factory.ingredients = {"v": 1}
        with self.assertRaises(ValueError) as ex:
            factory.remove_ingredient("v", 8)
        self.assertEqual(f'Ingredients quantity cannot be less than zero', str(ex.exception))

    def test_remove_ingredient_success(self):
        factory = PaintFactory("Fac", 10)
        factory.ingredients = {"v": 5}
        factory.remove_ingredient("v", 2)
        self.assertEqual({"v": 3}, factory.ingredients)

    def test_can_add_success(self):
        factory = PaintFactory("Fac", 10)
        factory.ingredients = {"v": 5}
        result = factory.can_add(2)
        self.assertTrue(True, result)

    def test_can_add_false(self):
        factory = PaintFactory("Fac", 10)
        factory.ingredients = {"v": 10}
        result = factory.can_add(2)
        self.assertFalse(False, result)

    def test_repr_success(self):
        factory = PaintFactory("Fac", 10)
        factory.ingredients = {"v": 5}
        expected = ""
        expected += f"Factory name: Fac with capacity 10." + "\n"
        expected += f"v: 5" + "\n"
        self.assertEqual(expected, factory.__repr__())


if __name__ == '__main__':
    unittest.main()

