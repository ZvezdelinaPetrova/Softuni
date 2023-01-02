import unittest

from oop.testing.lab.test_worker import Worker



class WorkerTests(unittest.TestCase):

    def test_initialization(self):
        worker = Worker("Deli", 200, 100)
        self.assertEqual("Deli", worker.name)
        self.assertEqual(200, worker.salary)
        self.assertEqual(100, worker.energy)
        self.assertEqual(0, worker.money)

    def test_rest_method_check(self):
        worker = Worker("Deli", 200, 100)
        worker.rest()
        self.assertEqual(101, worker.energy)

    def test_if_work_with_energy_below_zero(self):
        worker = Worker("Deli", 200, 0)

        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_if_work_with_negative_energy(self):
        worker = Worker("Deli", 200, -5)

        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_rest_increase_salary(self):
        worker = Worker("Deli", 200, 100)
        worker.work()
        self.assertEqual(200, worker.money)
        self.assertEqual(99, worker.energy)

    def test_worker_str_get_info(self):
        worker = Worker("Deli", 200, 100)
        worker.get_info()
        expected = f'Deli has saved 0 money.'
        self.assertEqual(expected, worker.get_info())


if __name__ == '__main__':
    unittest.main()

