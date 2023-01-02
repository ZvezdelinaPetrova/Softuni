def start_playing(Guitar):
    return Guitar.play()


class Guitar:
    def play(self):
        return "Playing the guitar"


guitar = Guitar()

print(start_playing(guitar))
