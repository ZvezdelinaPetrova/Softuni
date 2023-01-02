from project.user import Song


class Album:
    def __init__(self, name, *args):
        self.name = name
        self.published = False
        self.songs = list(args)

    def add_song(self, song):
        if self.published:
            return f"Cannot add songs. Album is published."
        if song.single:
            return f"Cannot add {song.name}. It's a single"

        for s in self.songs:
            if s.name == song.name:
                return f"Song is already in the album."

        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name):
        if self.published:
            return f"Cannot remove songs. Album is published."

        for song in self.songs:
            if song.name == song_name:
                self.songs.remove(song)
                return f"Removed song {song.name} from album {self.name}."

        return f"Song is not in the album."

    def details(self):
        result = ""
        result += f"Album {self.name}" + "\n"
        for values in self.songs:
            result += f"== {values.get_info()}" + "\n"
        return result

    def publish(self):

        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."
