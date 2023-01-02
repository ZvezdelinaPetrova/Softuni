import unittest

from project.main import Cat


class CatTests(unittest.TestCase):
    def test_initialization(self):
        kitten = Cat("Deli")
        self.assertEqual("Deli", kitten.name)
        self.assertEqual(False, kitten.fed)
        self.assertEqual(False, kitten.sleepy)
        self.assertEqual(0, kitten.size)

    def test_eat(self):
        kitten = Cat("Deli")
        kitten.eat()
        self.assertEqual(True, kitten.fed)
        self.assertEqual(True, kitten.sleepy)
        self.assertEqual(1, kitten.size)

    def test_if_def_true(self):
        kitten = Cat("Deli")
        kitten.fed = True
        with self.assertRaises(Exception) as ex:
            kitten.eat()
        self.assertEqual('Already fed.', str(ex.exception))

    def test_if_hungry(self):
        kitten = Cat("Deli")
        kitten.fed = False
        with self.assertRaises(Exception) as ex:
            kitten.sleep()
        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_sleep(self):
        kitten = Cat("Deli")
        kitten.fed = True
        kitten.sleepy = True
        kitten.sleep()
        self.assertEqual(False, kitten.sleepy)


if __name__ == '__main__':
    unittest.main()

#
# import unittest
#
# from nora.testing.cat import Cat
#
#
# class CatTests(unittest.TestCase):
#
#     def test_initialization(self):
#         cat = Cat("Deli")
#         self.assertEqual("Deli", cat.name)
#         self.assertFalse(cat.fed)
#         self.assertFalse(cat.sleepy)
#         self.assertEqual(0, cat.size)
#
#     def test_increased_after_eating(self):
#         cat = Cat("Deli")
#         cat.eat()
#         self.assertEqual(1, cat.size)
#         self.assertEqual(1, cat.size)
#
#     def test_fed_successfully(self):
#         cat = Cat("Deli")
#         cat.eat()
#         self.assertTrue(cat.fed)
#         self.assertTrue(cat.sleepy)
#
#     def test_already_fed(self):
#         cat = Cat("Deli")
#         self.assertFalse(cat.fed)
#         cat.eat()
#         self.assertTrue(cat.fed)
#         with self.assertRaises(Exception) as ex:
#             cat.eat()
#         self.assertEqual("Already fed.", str(ex.exception))
#
#     def test_sleep(self):
#         cat = Cat("Deli")
#         self.assertFalse(cat.fed)
#         with self.assertRaises(Exception) as ex:
#             cat.sleep()
#         self.assertEqual("Cannot sleep while hungry", str(ex.exception))
#
#     def test_sleepy(self):
#         cat = Cat("Deli")
#         self.assertFalse(cat.sleepy)
#         cat.eat()
#         self.assertTrue(cat.sleepy)
#         cat.sleep()
#         self.assertFalse(cat.sleepy)
#
#
# if __name__ == '__main__':
#     unittest.main()