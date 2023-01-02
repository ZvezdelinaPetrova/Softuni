import unittest

from project.plantation import Plantation


class PlantationTest(unittest.TestCase):

    def test_initialization(self):
        plantation = Plantation(50)
        self.assertEqual(50, plantation.size)
        self.assertEqual({}, plantation.plants)
        self.assertEqual([], plantation.workers)

    def test_size_error(self):
        plantation = Plantation(50)
        with self.assertRaises(ValueError) as ex:
            plantation.size = -3
        self.assertEqual("Size must be positive number!", str(ex.exception))

    def test_if_make_success(self):
        plantation = Plantation(50)
        plantation.size = 3
        self.assertEqual(3, plantation.size)

    def test_worker_error(self):
        plantation = Plantation(50)
        plantation.workers.append("Deli")
        with self.assertRaises(ValueError) as ex:
            plantation.hire_worker("Deli")
        self.assertEqual("Worker already hired!", str(ex.exception))

    def test_worker_success(self):
        plantation = Plantation(50)
        expected = plantation.hire_worker("Deli")
        self.assertEqual(f"Deli successfully hired.", expected)
        self.assertEqual(["Deli"], plantation.workers)

    def test_len_success(self):
        plantation = Plantation(50)
        result = plantation.__len__()
        self.assertEqual(0, result)

    def test_len_success_2(self):
        plantation = Plantation(50)
        plantation.workers = ["Deli", "Kaloyan"]
        plantation.plants = {"Deli": "t", "Kaloyan": "v"}
        result = plantation.__len__()
        self.assertEqual(2, result)

    def test_planting_error(self):
        plantation = Plantation(50)
        plantation.workers.append("Deli")
        with self.assertRaises(ValueError) as ex:
            plantation.planting("Kaloyan", "Rosa")
        self.assertEqual(f"Worker with name Kaloyan is not hired!", str(ex.exception))

    def test_planting_error_2(self):
        plantation = Plantation(0)
        plantation.workers.append("Deli")
        with self.assertRaises(ValueError) as ex:
            plantation.planting("Deli", "Rosa")
        self.assertEqual("The plantation is full!", str(ex.exception))

    def test_planting_success(self):
        plantation = Plantation(50)
        plantation.workers.append("Deli")
        plantation.plants = {"Deli": ["t"]}
        result = plantation.planting("Deli", "Rosa")
        self.assertEqual(f"Deli planted Rosa.", result)
        self.assertEqual({"Deli": ["t", "Rosa"]}, plantation.plants)

    def test_planting_success_2(self):
        plantation = Plantation(50)
        plantation.workers.append("Deli")
        result = plantation.planting("Deli", "Rosa")
        self.assertEqual(f"Deli planted it's first Rosa.", result)
        self.assertEqual({"Deli": ["Rosa"]}, plantation.plants)

    def test_str_success(self):
        plantation = Plantation(50)
        plantation.workers.append("Deli")
        plantation.plants = {"Deli": ["t"]}
        expected = f"Plantation size: 50" + "\n"
        expected += f"Deli" + "\n"
        expected += f"Deli planted: t"
        self.assertEqual(expected, plantation.__str__())

    def test_repr_success(self):
        plantation = Plantation(50)
        plantation.workers.append("Deli")
        plantation.plants = {"Deli": ["t"]}
        expected = ""
        expected += f"Size: {plantation.size}" + "\n"
        expected += f"Workers: Deli"
        self.assertEqual(expected, plantation.__repr__())


if __name__ == '__main__':
    unittest.main()

