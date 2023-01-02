from project.movie import Movie

import unittest


class MovieTest(unittest.TestCase):

    def test_initialization(self):
        movie = Movie("Avatar", 2000, 10)
        self.assertEqual("Avatar", movie.name)
        self.assertEqual(2000, movie.year)
        self.assertEqual(10, movie.rating)
        self.assertEqual([], movie.actors)

    def test_name_error(self):
        movie = Movie("Avatar", 2000, 10)
        with self.assertRaises(ValueError) as ex:
            movie.name = ""
        self.assertEqual("Name cannot be an empty string!", str(ex.exception))

    def test_if_name_success(self):
        movie = Movie("Avatar", 2000, 10)
        movie.name = "Titanic"
        self.assertEqual("Titanic", movie.name)

    def test_year_error(self):
        movie = Movie("Avatar", 2000, 10)
        with self.assertRaises(ValueError) as ex:
            movie.year = 1600
        self.assertEqual("Year is not valid!", str(ex.exception))

    def test_worker_success(self):
        movie = Movie("Avatar", 2000, 10)
        movie.year = 2003
        self.assertEqual(2003, movie.year)

    def test_add_actors_success(self):
        movie = Movie("Avatar", 2000, 10)
        movie.actors = ["Deli"]
        movie.add_actor("Kaloyan")
        self.assertEqual(["Deli", "Kaloyan"], movie.actors)

    def test_add_actors_error(self):
        movie = Movie("Avatar", 2000, 10)
        movie.actors = ["Deli"]
        result = movie.add_actor("Deli")
        self.assertEqual(f"Deli is already added in the list of actors!", result)

    def test_gt(self):
        movie = Movie("Avatar", 2000, 10)
        movie2 = Movie("Titanic", 1999, 11)
        result = movie.__gt__(movie2)
        self.assertEqual(f'"{movie2.name}" is better than "{movie.name}"', result)

    def test_gt_2(self):
        movie = Movie("Avatar", 2000, 15)
        movie2 = Movie("Titanic", 1999, 11)
        result = movie.__gt__(movie2)
        self.assertEqual(f'"{movie.name}" is better than "{movie2.name}"', result)

    def test_repr_success(self):
        movie = Movie("Avatar", 2000, 15)
        movie.actors = ["Deli"]
        expected = ""
        expected += f"Name: {movie.name}" + "\n"
        expected += f"Year of Release: {movie.year}" + "\n"
        expected += f"Rating: {movie.rating:.2f}" + "\n"
        expected += f"Cast: {', '.join(movie.actors)}"
        self.assertEqual(expected, movie.__repr__())


if __name__ == '__main__':
    unittest.main()


