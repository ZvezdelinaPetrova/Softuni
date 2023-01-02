import unittest

from project.bookstore import Bookstore


class BookstoreTest(unittest.TestCase):

    def test_initialization(self):
        store = Bookstore(5)
        self.assertEqual(5, store.books_limit)
        self.assertEqual({}, store.availability_in_store_by_book_titles)
        self.assertEqual(0, store._Bookstore__total_sold_books)

    def test_book_limit_error(self):
        store = Bookstore(5)
        with self.assertRaises(ValueError) as ex:
            store.books_limit = -3
        self.assertEqual(f"Books limit of -3 is not valid", str(ex.exception))

    def test_book_limit_error_0(self):
        store = Bookstore(5)
        with self.assertRaises(ValueError) as ex:
            store.books_limit = 0
        self.assertEqual(f"Books limit of 0 is not valid", str(ex.exception))

    def test_book_limit_success(self):
        store = Bookstore(5)
        store.books_limit = 5
        self.assertEqual(5, store.books_limit)

    def test_len_book_values(self):
        store = Bookstore(5)
        store.availability_in_store_by_book_titles = {"Titanic": 4}
        result = store.__len__()
        self.assertEqual({"Titanic": 4}, store.availability_in_store_by_book_titles)
        self.assertEqual(4, result)

    def test_book_limit_reached(self):
        store = Bookstore(5)
        store.books_limit = 5
        store.availability_in_store_by_book_titles = {"Titanic": 4}
        with self.assertRaises(Exception) as ex:
            store.receive_book("Titanic", 5)
        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))

    def test_receive_numbers(self):
        store = Bookstore(30)
        store.availability_in_store_by_book_titles = {"Titanic": 2}
        store.receive_book("The Beach", 5)
        self.assertEqual({"Titanic": 2, "The Beach": 5}, store.availability_in_store_by_book_titles)

    def test_receive_numbers_book_there(self):
        store = Bookstore(30)
        store.availability_in_store_by_book_titles = {"Titanic": 2}
        result = store.receive_book("Titanic", 5)
        self.assertEqual({"Titanic": 7}, store.availability_in_store_by_book_titles)
        self.assertEqual(f"7 copies of Titanic are available in the bookstore.", result)

    def test_sell_book_error(self):
        store = Bookstore(5)
        store.availability_in_store_by_book_titles = {"Titanic": 4}
        with self.assertRaises(Exception) as ex:
            store.sell_book("Exam", 1)
        self.assertEqual(f"Book Exam doesn't exist!", str(ex.exception))

    def test_sell_book_error_ahhhh(self):
        store = Bookstore(5)
        store.availability_in_store_by_book_titles = {}
        with self.assertRaises(Exception) as ex:
            store.sell_book("Exam", 1)
        self.assertEqual(f"Book Exam doesn't exist!", str(ex.exception))

    def test_sell_book_error_2(self):
        store = Bookstore(5)
        store.availability_in_store_by_book_titles = {"Titanic": 4}
        with self.assertRaises(Exception) as ex:
            store.sell_book("Titanic", 7)
            store.availability_in_store_by_book_titles = {"Titanic": 4}
        self.assertEqual(f"Titanic has not enough copies to sell. Left: 4", str(ex.exception))

    def test_sell_book_success(self):
        store = Bookstore(30)
        store.availability_in_store_by_book_titles = {"Titanic": 5}
        result = store.sell_book("Titanic", 2)
        self.assertEqual({"Titanic": 3}, store.availability_in_store_by_book_titles)
        self.assertEqual(2, store._Bookstore__total_sold_books)
        self.assertEqual(f"Sold 2 copies of Titanic", result)

    def test_str_success(self):
        store = Bookstore(30)
        store.availability_in_store_by_book_titles = {"Titanic": 5}
        store._Bookstore__total_sold_books = 2
        expected = f"Total sold books: 2" + "\n"
        expected += f"Current availability: 5" + "\n"
        expected += f" - Titanic: 5 copies"
        self.assertEqual(expected, store.__str__())

if __name__ == '__main__':
    unittest.main()


