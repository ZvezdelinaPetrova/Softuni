import unittest

from project.pet_shop import PetShop


class PetShopTest(unittest.TestCase):

    def test_initialization(self):
        shop = PetShop("Zoo")
        self.assertEqual("Zoo", shop.name)
        self.assertEqual({}, shop.food)
        self.assertEqual([], shop.pets)

    def test_add_food_error(self):
        shop = PetShop("Zoo")
        with self.assertRaises(ValueError) as ex:
            shop.add_food("Veg", -1)
        self.assertEqual(f'Quantity cannot be equal to or less than 0', str(ex.exception))

    def test_add_food_success_not_in(self):
        shop = PetShop("Zoo")
        result = shop.add_food("Veg", 5)
        self.assertEqual({"Veg": 5}, shop.food)
        self.assertEqual(f"Successfully added 5.00 grams of Veg.", result)

    def test_add_food_success_in(self):
        shop = PetShop("Zoo")
        shop.food = {"Veg": 2}
        result = shop.add_food("Veg", 5)
        self.assertEqual({"Veg": 7}, shop.food)
        self.assertEqual(f"Successfully added 5.00 grams of Veg.", result)

    def test_add_pet_not_in(self):
        shop = PetShop("Zoo")
        result = shop.add_pet("Ari")
        self.assertEqual(f"Successfully added Ari.", result)
        self.assertEqual(["Ari"], shop.pets)

    def test_add_pet_exception(self):
        shop = PetShop("Zoo")
        shop.pets = ["Ari"]
        with self.assertRaises(Exception) as ex:
            shop.add_pet("Ari")
        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))

    def test_feed_pet_exception_pet_name(self):
        shop = PetShop("Zoo")
        shop.pets = ["Ari"]
        with self.assertRaises(Exception) as ex:
            shop.feed_pet("ProPlan", "Jack")
        self.assertEqual(f"Please insert a valid pet name", str(ex.exception))

    def test_feed_pet_exception_food_name(self):
        shop = PetShop("Zoo")
        shop.food = {"G": 2}
        shop.pets = ["Ari"]
        result = shop.feed_pet("ProPlan", "Ari")
        self.assertEqual(f'You do not have ProPlan', result)

    def test_feed_pet_exception_adding_food(self):
        shop = PetShop("Zoo")
        shop.food = {"ProPlan": 2}
        shop.pets = ["Ari"]
        result = shop.feed_pet("ProPlan", "Ari")
        self.assertEqual({"ProPlan": 1002.00}, shop.food)
        self.assertEqual(f"Adding food...", result)

    def test_feed_pet_success(self):
        shop = PetShop("Zoo")
        shop.food = {"ProPlan": 150}
        shop.pets = ["Ari"]
        result = shop.feed_pet("ProPlan", "Ari")
        self.assertEqual({"ProPlan": 50}, shop.food)
        self.assertEqual(f"Ari was successfully fed", result)

    def test_repr_success(self):
        shop = PetShop("Zoo")
        shop.food = {"ProPlan": 150}
        shop.pets = ["Ari", "Jack"]
        expected = f"Shop {shop.name}:" + "\n"
        expected += f"Pets: Ari, Jack"
        self.assertEqual(expected, shop.__repr__())


if __name__ == '__main__':
    unittest.main()

