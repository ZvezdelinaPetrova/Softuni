import unittest

from project.plantation import Plantation
# from oop.project.project.plantation import Plantation


class TestPlantation(unittest.TestCase):
    def test_initialization(self):
        plantation = Plantation(20)
        self.assertEqual(20, plantation.size)
        self.assertEqual({}, plantation.plants)
        self.assertEqual([], plantation.workers)

    def test_size_error(self):
        plantation = Plantation(0)
        with self.assertRaises(ValueError) as ex:
            plantation.size = -4
        self.assertEqual("Size must be positive number!", str(ex.exception))

    def test_size_setter(self):
        plantation = Plantation(10)
        plantation.size = 10
        self.assertEqual(10, plantation.size)

    def test_hire_worker_error(self):
        plantation = Plantation(20)
        plantation.workers.append("Deli")
        with self.assertRaises(ValueError) as ex:
            plantation.hire_worker("Deli")
        self.assertEqual("Worker already hired!", str(ex.exception))

    def test_hire_worker_success(self):
        plantation = Plantation(20)
        plantation.workers.append("Deli")
        expected = plantation.hire_worker("Ari")
        self.assertEqual(f"Ari successfully hired.", expected)
        self.assertEqual(["Deli", "Ari"], plantation.workers)

    def test_planting_error(self):
        plantation = Plantation(20)
        plantation.workers.append("Deli")
        with self.assertRaises(ValueError) as ex:
            plantation.planting("Ari", "Rosa")
        self.assertEqual(f"Worker with name Ari is not hired!", str(ex.exception))

    def test_len_planting_no_more(self):
        plantation = Plantation(0)
        plantation.workers.append("Deli")
        with self.assertRaises(ValueError) as ex:
            plantation.planting("Deli", "Rosa")
        self.assertEqual("The plantation is full!", str(ex.exception))

    def test_len_not_addition(self):
        self.pl = Plantation(1)
        self.pl.hire_worker('Martin')
        self.pl.hire_worker('Alexandra')
        self.pl.plants['Martin'] = ['Tomatoes']
        self.pl.plants['Alexandra'] = ['plant']
        self.assertEqual(self.pl.__len__(), 2)

    def test_planting_worker_in_list(self):
        plantation = Plantation(20)
        plantation.workers.append("Deli")
        plantation.plants = {"Deli": ["Rosa"]}
        expected = plantation.planting("Deli", "Rosa2")
        self.assertEqual(f"Deli planted Rosa2.", expected)
        self.assertEqual({'Deli': ['Rosa', 'Rosa2']}, plantation.plants)

    def test_planting_not_in_list(self):
        plantation = Plantation(20)
        plantation.workers.append("Ari")
        plantation.plants = {}
        expected = plantation.planting("Ari", "Rosa2")
        self.assertEqual(f"Ari planted it's first Rosa2.", expected)
        self.assertEqual({'Ari': ['Rosa2']}, plantation.plants)


    def test_repr_method(self):
        plantation = Plantation(20)
        plantation.workers.append("Deli")
        plantation.plants = {"flower": 1}
        expected = f'Size: 20\nWorkers: Deli'
        actual = plantation.__repr__()
        self.assertEqual(expected, actual)

    def test_str_method(self):
        plantation = Plantation(20)
        plantation.workers.append("Deli")
        plantation.workers.append("Ari")
        plantation.plants = {'Deli': ['Rosa'], 'Ari': ['Rosa2']}
        result = f"Plantation size: 20" + "\n"
        result += "Deli, Ari" + "\n"
        result += "Deli planted: Rosa" + "\n"
        result += "Ari planted: Rosa2"
        result.strip()
        actual = plantation.__str__()
        self.assertEqual(result, actual)

    def test_len(self):
        plantation = Plantation(20)
        plantation.workers.append("Deli")
        plantation.plants = {"Deli": ["flower1", "flower2"]}
        plantation.__len__()
        self.assertEqual(2, plantation.__len__())


if __name__ == '__main__':
    unittest.main()

