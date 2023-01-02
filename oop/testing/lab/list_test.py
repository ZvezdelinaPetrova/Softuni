import unittest

from oop.testing.lab.extended_list import IntegerList


class Integers(unittest.TestCase):

    def test_initialization(self):
        list_num = IntegerList(5, 10, 15)
        self.assertEqual([5, 10, 15], list_num._IntegerList__data)

    def test_init(self):
        list_num = IntegerList("s", "d")
        self.assertEqual([], list_num._IntegerList__data)

    def test_add_element_in_list_error_error(self):
        list_num = IntegerList(5, 10, 15)
        with self.assertRaises(ValueError) as ex:
            list_num.add("text")
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_add_element_in_list(self):
        list_num = IntegerList(5, 10, 15)
        expected = list_num.add(7)
        self.assertEqual([5, 10, 15, 7], expected)

    def test_add_remove_index_error(self):
        list_num = IntegerList(5, 10, 15)
        with self.assertRaises(IndexError) as ex:
            list_num.remove_index(3)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_remove_index(self):
        list_num = IntegerList(5, 10, 15)
        expected = list_num.remove_index(0)
        self.assertEqual(5, expected)
        self.assertEqual([10, 15], list_num._IntegerList__data)

    def test_get_index_error(self):
        list_num = IntegerList(5, 10, 15)
        with self.assertRaises(IndexError) as ex:
            list_num.get(3)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_index(self):
        list_num = IntegerList(5, 10, 15)
        expected = list_num.get(0)
        self.assertEqual(5, expected)
        self.assertEqual([5, 10, 15], list_num._IntegerList__data)

    def test_insert_error_index(self):
        list_num = IntegerList(5, 10, 15)
        with self.assertRaises(IndexError) as ex:
            list_num.insert(3, 9)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_error_int(self):
        list_num = IntegerList(5, 10, 15)
        with self.assertRaises(ValueError) as ex:
            list_num.insert(0, "t")
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_insert(self):
        list_num = IntegerList(5, 10, 15)
        list_num.insert(0, 9)
        expected = list_num._IntegerList__data
        self.assertEqual([9, 5, 10, 15], expected)

    def test_get_biggest(self):
        list_num = IntegerList(5, 10, 15)
        expected = list_num.get_biggest()
        self.assertEqual(15, expected)

    def test_get_element_return_index(self):
        list_num = IntegerList(5, 10, 15)
        expected = list_num.get_index(5)
        self.assertEqual(0, expected)


if __name__ == '__main__':
    unittest.main()


# import unittest
#
# # from project.main import IntegerList
#
#
# class TestIntegerList(unittest.TestCase):
#     def test_initialization(self):
#         obj = IntegerList(1, 2, 3)
#         self.assertEqual([1, 2, 3], obj._IntegerList__data)
#
#     def test_initialization_letters(self):
#         obj = IntegerList("d")
#         self.assertEqual([], obj._IntegerList__data)
#
#     # def test_get(self):
#     #     obj = IntegerList(1, 2, 3)
#     #     obj.get_data()
#     #     self.assertEqual([1, 2, 3], obj._IntegerList__data)
#
#     def test_add_error(self):
#         obj = IntegerList(1, 2, 3)
#         with self.assertRaises(ValueError) as ex:
#             obj.add("d")
#         self.assertEqual("Element is not Integer", str(ex.exception))
#
#     def test_add_success(self):
#         obj = IntegerList(1, 2, 3)
#         obj.add(4)
#         self.assertEqual([1, 2, 3, 4], obj._IntegerList__data)
#
#     def test_remove_index(self):
#         obj = IntegerList(1, 2, 3)
#         with self.assertRaises(IndexError) as ex:
#             obj.remove_index(4)
#         self.assertEqual("Index is out of range", str(ex.exception))
#
#     def test_remove_success(self):
#         obj = IntegerList(1, 2, 3)
#         obj.remove_index(1)
#         self.assertEqual([1, 3], obj._IntegerList__data)
#
#     def test_get_index_error(self):
#         obj = IntegerList(1, 2, 3)
#         with self.assertRaises(IndexError) as ex:
#             obj.get(4)
#         self.assertEqual("Index is out of range", str(ex.exception))
#
#     def test_get_success(self):
#         obj = IntegerList(1, 2, 3)
#         el = obj.get(1)
#         self.assertEqual(2, el)
#
#     def test_insert_index_error(self):
#         obj = IntegerList(1, 2, 3)
#         with self.assertRaises(IndexError) as ex:
#             obj.insert(4, 4)
#         self.assertEqual("Index is out of range", str(ex.exception))
#
#     def test_insert_el_error(self):
#         obj = IntegerList(1, 2, 3)
#         with self.assertRaises(ValueError) as ex:
#             obj.insert(2, "d")
#         self.assertEqual("Element is not Integer", str(ex.exception))
#
#     def test_insert_success(self):
#         obj = IntegerList(1, 2, 3)
#         obj.insert(1, 5)
#         self.assertEqual([1, 5, 2, 3], obj._IntegerList__data)
#
#     def test_get_biggest(self):
#         obj = IntegerList(1, 2, 3)
#         el = obj.get_biggest()
#         self.assertEqual(3, el)
#
#     def test_get_index(self):
#         obj = IntegerList(1, 2, 3)
#         index = obj.get_index(3)
#         self.assertEqual(2, index)
#
#
# if __name__ == '__main__':
#     unittest.main()