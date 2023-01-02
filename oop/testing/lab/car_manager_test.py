import unittest

from oop.testing.lab.car_manager import Car


class CarTest(unittest.TestCase):

    def test_initialization(self):
        car = Car("t", "Opel", 2, 40)
        self.assertEqual("t", car.make)
        self.assertEqual("Opel", car.model)
        self.assertEqual(2, car.fuel_consumption)
        self.assertEqual(40, car.fuel_capacity)
        self.assertEqual(0, car.fuel_amount)

    def test_fuel_consumption_error(self):
        car = Car("t", "Opel", 2, 40)
        with self.assertRaises(Exception) as ex:
            car.fuel_consumption = -4
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_consumption(self):
        car = Car("t", "Opel", 2, 40)
        car.fuel_consumption = 4
        expected = car.fuel_consumption
        self.assertEqual(4, expected)

    def test_fuel_capacity_error(self):
        car = Car("t", "Opel", 2, 40)
        with self.assertRaises(Exception) as ex:
            car.fuel_capacity = -4
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity(self):
        car = Car("t", "Opel", 2, 40)
        car.fuel_capacity = 4
        expected = car.fuel_capacity
        self.assertEqual(4, expected)

    def test_fuel_amount_error(self):
        car = Car("t", "Opel", 2, 40)
        with self.assertRaises(Exception) as ex:
            car.fuel_amount = -4
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_fuel_amount(self):
        car = Car("t", "Opel", 2, 40)
        car.fuel_amount = 4
        expected = car.fuel_amount
        self.assertEqual(4, expected)

    def test_fuel_error(self):
        car = Car("t", "Opel", 2, 40)
        with self.assertRaises(Exception) as ex:
            car.refuel(-4)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_model_error(self):
        car = Car("t", "Opel", 2, 40)
        with self.assertRaises(Exception) as ex:
            car.model = ""
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_model(self):
        car = Car("t", "Opel", 2, 40)
        car.model = "V"
        self.assertEqual("V", car.model)

    def test_make_error(self):
        car = Car("t", "Opel", 2, 40)
        with self.assertRaises(Exception) as ex:
            car.make = ""
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_make(self):
        car = Car("t", "Opel", 2, 40)
        car.make = "V"
        self.assertEqual("V", car.make)

    def test_refuel_error_re(self):
        car = Car("t", "Opel", 2, 40)
        with self.assertRaises(Exception) as ex:
            car.refuel(-4)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel(self):
        car = Car("t", "Opel", 2, 40)
        car.fuel_amount = 0
        car.refuel(10)
        self.assertEqual(10, car.fuel_amount)

    def test_refuel_with_capacity(self):
        car = Car("t", "Opel", 2, 5)
        car.refuel(10)
        car.fuel_amount = 5
        self.assertEqual(5, car.fuel_amount)

    def test_drive_error(self):
        car = Car("t", "Opel", 5, 30)
        car.fuel_amount = 15
        with self.assertRaises(Exception) as ex:
            car.drive(400)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive(self):
        car = Car("t", "Opel", 2, 300)
        car.fuel_amount = 900
        car.drive(400)
        self.assertEqual(892, car.fuel_amount)


if __name__ == '__main__':
    unittest.main()