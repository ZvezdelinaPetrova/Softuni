import unittest

# from oop.testing.exercise.vehicle.project.vehicle import Vehicle

from project.cat import Vehicle


class TestMammal(unittest.TestCase):
    def test_initialization(self):
        vehicle = Vehicle(50, 20)
        self.assertEqual(50, vehicle.fuel)
        self.assertEqual(50, vehicle.capacity)
        self.assertEqual(20, vehicle.horse_power)
        self.assertEqual(1.25, vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_drive(self):
        vehicle = Vehicle(50, 20)
        vehicle.drive(5)
        # needed = 6.25
        expected = 43.75
        actual = vehicle.fuel
        self.assertEqual(expected, actual)

    def test_drive_error(self):
        vehicle = Vehicle(50, 20)
        with self.assertRaises(Exception) as ex:
            vehicle.drive(50)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refuel_error(self):
        vehicle = Vehicle(50, 20)
        with self.assertRaises(Exception) as ex:
            vehicle.refuel(50)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_success(self):
        vehicle = Vehicle(50, 20)
        vehicle.capacity = 60
        vehicle.refuel(5)
        expected = 55
        actual = vehicle.fuel
        self.assertEqual(expected, actual)

    def test_str_function(self):
        vehicle = Vehicle(50, 20)
        vehicle.__str__()
        expected = f"The vehicle has 20 horse power with 50 fuel left and " \
                   f"1.25 fuel consumption"
        actual = vehicle.__str__()
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()