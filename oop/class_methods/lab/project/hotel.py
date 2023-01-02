class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for room in self.rooms:
            if room.number == room_number:
                result = room.take_room(people)
                if not result:
                    self.guests += people

    def free_room(self, room_number):
        for room in self.rooms:
            if room.number == room_number:
                self.guests -= room.guests
                room.free_room()

    def status(self):
        result = f"Hotel {self.name} has {self.guests} total guests" + "\n"
        result += f"Free rooms: {', '.join([str(room.number) for room in self.rooms if not room.is_taken])}" + "\n"
        result += f"Taken rooms: {', '.join([str(room.number) for room in self.rooms if room.is_taken])}"
        return result


# class Hotel:
#
#     def __init__(self, name):
#         self.name = name
#         self.rooms = []
#         self.guests = 0
#
#     @classmethod
#     def from_stars(cls, stars_count):
#         return cls(f"{stars_count} stars Hotel")
#
#     def add_room(self, room):
#         self.rooms.append(room)
#
#     def take_room(self, room_number, people):
#         for room in self.rooms:
#             if room.number == room_number:
#                 if not room.is_taken:
#                     if room.capacity >= people:
#                         self.guests += people
#                         room.guests += people
#                         room.is_taken = True
#
#     def free_room(self, room_number):
#         for room in self.rooms:
#             if room.number == room_number:
#                 if room.is_taken:
#                     self.guests -= room.guests
#                     room.guests = 0
#                     room.is_taken = False
#
#     def status(self):
#         result = ""
#         result += f"Hotel {self.name} has {self.guests} total guests" + "\n"
#         t = [x for x in self.rooms if not x.is_taken]
#         ttt = [x for x in self.rooms if x.is_taken]
#         result += f"Free rooms: {', '.join(str(x.number) for x in t)}" + "\n"
#         result += f"Taken rooms: {', '.join(str(x.number) for x in ttt)}"
#         return result

