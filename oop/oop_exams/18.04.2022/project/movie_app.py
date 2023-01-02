from project.movie_specification.movie import Movie
from project.movie_specification.action import Action
from project.movie_specification.fantasy import Fantasy
from project.movie_specification.thriller import Thriller
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def register_user(self, username: str, age: int):
        users = [d for d in self.users_collection if d.username == username]
        if users:
            raise Exception("User already exists!")

        new_user = User(username, age)
        self.users_collection.append(new_user)
        return f"{username} registered successfully."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        user = MovieApp.find_object(self, username, self.users_collection)
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        found_movie = [m for m in user.movies_owned if m == movie]
        if not found_movie:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        if user == movie.owner:
            for key, value in kwargs.items():
                if key == "title":
                    movie.title = value
                elif key == "year":
                    movie.year = value
                elif key == "age_restriction":
                    movie.age_restriction = value
        #     for attr, new_value in kwargs.items():
        #         setattr(movie, attr, new_value)
            return f"{username} successfully edited {movie.title} movie."

    def upload_movie(self, username: str, movie: Movie):
        user = MovieApp.find_object(self, username, self.users_collection)
        if user not in self.users_collection:
            raise Exception("This user does not exist!")
        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")
        if user == movie.owner:
            self.movies_collection.append(movie)
            user.movies_owned.append(movie)
            return f"{username} successfully added {movie.title} movie."
        if user.username != movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        # elif not username == movie.owner.username:
        #     raise Exception(f'{username} is not the owner of the movie {movie.title}!')

    def delete_movie(self, username: str, movie: Movie):
        user = MovieApp.find_object(self, username, self.users_collection)
        if user != movie.owner:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        self.movies_collection.remove(movie)
        user.movies_owned.remove(movie)
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        user = MovieApp.find_object(self, username, self.users_collection)
        if user.username == movie.owner.username:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")
        # if username == movie.owner.username:
        #     raise Exception(f'{username} is the owner of the movie {movie.title}!')
        if movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        movie.likes += 1
        user.movies_liked.append(movie)
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        user = MovieApp.find_object(self, username, self.users_collection)
        if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        movie.likes -= 1
        user.movies_liked.remove(movie)
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if not self.movies_collection:
            return f"No movies found."

        new_list = sorted(self.movies_collection, key=lambda x: (-x.year, x.title))
        result = ""
        for u in new_list:
            result += f"{u.details()}" + "\n"
        return result.strip()

    def __str__(self):
        result = ""
        if self.users_collection:
            result += f"All users: {', '.join([d.username for d in self.users_collection])}" + "\n"
        else:
            result += f"All users: No users." + "\n"

        if self.movies_collection:
            result += f"All movies: {', '.join([d.title for d in self.movies_collection])}" + "\n"
        else:
            result += f"All movies: No movies."
        return result.strip()

    def find_object(self, username, list_with_objects):
        for obj in list_with_objects:
            if obj.username == username:
                return obj
