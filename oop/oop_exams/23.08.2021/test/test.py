import unittest

from project.library import Library


class LibraryTest(unittest.TestCase):

    def test_initialization(self):
        library = Library("L")
        self.assertEqual("L", library.name)
        self.assertEqual({}, library.books_by_authors)
        self.assertEqual({}, library.readers)

    def test_name_error(self):
        library = Library("L")
        with self.assertRaises(ValueError) as ex:
            library.name = ""
        self.assertEqual("Name cannot be empty string!", str(ex.exception))

    def test_name_success(self):
        library = Library("L")
        library.name = "LLL"
        self.assertEqual("LLL", library.name)

    def test_add_book_author_not_in(self):
        library = Library("L")
        library.books_by_authors = {"Deli": ["Wis"]}
        library.add_book("Kaloyan", "G")
        self.assertEqual({"Deli": ["Wis"], "Kaloyan": ["G"]}, library.books_by_authors)

    def test_add_book_author_in(self):
        library = Library("L")
        library.books_by_authors = {"Deli": ["Wis"]}
        library.add_book("Deli", "G")
        self.assertEqual({"Deli": ["Wis", "G"]}, library.books_by_authors)

    def test_add_reader(self):
        library = Library("L")
        library.readers = {"Deli": ["Wis"]}
        library.add_reader("Kaloyan")
        self.assertEqual({"Deli": ["Wis"], "Kaloyan": []}, library.readers)

    def test_add_reader_in_already(self):
        library = Library("L")
        library.readers = {"Deli": ["Wis"]}
        result = library.add_reader("Deli")
        self.assertEqual(f"Deli is already registered in the L library.", result)

    def test_rent_book_reader_not(self):
        library = Library("L")
        library.readers = {"Deli": ["Wis"]}
        result = library.rent_book("Kaloyan", "Go", "Titanic")
        self.assertEqual(f"Kaloyan is not registered in the L Library.", result)

    def test_rent_book_author_not_in(self):
        library = Library("L")
        library.readers = {"Deli": []}
        library.books_by_authors = {"Go": ["UOO"]}
        result = library.rent_book("Deli", "PPP", "Titanic")
        self.assertEqual(f"L Library does not have any PPP's books.", result)

    def test_rent_book_not_in(self):
        library = Library("L")
        library.readers = {"Deli": ["Wis"]}
        library.books_by_authors = {"Go": ["UOO"]}
        result = library.rent_book("Deli", "Go", "Titanic")
        self.assertEqual(f"""L Library does not have Go's "Titanic".""", result)

    def test_rent_book_success(self):
        library = Library("L")
        library.readers = {"Deli": []}
        library.books_by_authors = {"Go": ["UOO", "Titanic"]}
        library.rent_book("Deli", "Go", "Titanic")
        self.assertEqual({"Deli": [{"Go": "Titanic"}]}, library.readers)

    def test_rent_book_success_delete_from_books_authors(self):
        library = Library("L")
        library.readers = {"Deli": []}
        library.books_by_authors = {"Go": ["UOO", "Titanic"]}
        library.rent_book("Deli", "Go", "Titanic")
        self.assertEqual({"Go": ["UOO"]}, library.books_by_authors)


if __name__ == '__main__':
    unittest.main()

