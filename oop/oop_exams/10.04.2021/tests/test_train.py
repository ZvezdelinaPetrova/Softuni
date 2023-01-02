import unittest

from project.train.train import Train


class TrainTest(unittest.TestCase):

    def test_initialization(self):
        train = Train("Fast", 100)
        self.assertEqual("Fast", train.name)
        self.assertEqual(100, train.capacity)
        self.assertEqual("Train is full", train.TRAIN_FULL)
        self.assertEqual("Passenger {} Exists", train.PASSENGER_EXISTS)
        self.assertEqual("Passenger Not Found", train.PASSENGER_NOT_FOUND)
        self.assertEqual("Added passenger {}", train.PASSENGER_ADD)
        self.assertEqual("Removed {}", train.PASSENGER_REMOVED)
        self.assertEqual(0, train.ZERO_CAPACITY)

    def test_add_passenger_error(self):
        train = Train("Fast", 100)
        train.capacity = 1
        train.passengers = ["Deli"]
        with self.assertRaises(ValueError) as ex:
            train.add("Kaloyan")
        self.assertEqual("Train is full", str(ex.exception))

    def test_add_passenger_error_name_added(self):
        train = Train("Fast", 100)
        train.capacity = 6
        train.passengers = ["Deli"]
        with self.assertRaises(ValueError) as ex:
            train.add("Deli")
        self.assertEqual("Passenger Deli Exists", str(ex.exception))

    def test_add_success(self):
        train = Train("Fast", 100)
        train.capacity = 6
        train.passengers = ["Deli"]
        result = train.add("Kaloyan")
        self.assertEqual("Added passenger Kaloyan", result)
        self.assertEqual(["Deli", "Kaloyan"], train.passengers)

    def test_remove_error(self):
        train = Train("Fast", 100)
        train.capacity = 6
        train.passengers = ["Deli"]
        with self.assertRaises(ValueError) as ex:
            train.remove("Kaloyan")
        self.assertEqual("Passenger Not Found", str(ex.exception))

    def test_remove_success(self):
        train = Train("Fast", 100)
        train.capacity = 6
        train.passengers = ["Deli"]
        result = train.remove("Deli")
        self.assertEqual("Removed Deli", result)
        self.assertEqual([], train.passengers)


if __name__ == '__main__':
    unittest.main()

