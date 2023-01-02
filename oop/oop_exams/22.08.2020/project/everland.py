from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        expenses = sum([x.expenses for x in self.rooms])
        room_cost = sum([x.room_cost for x in self.rooms])
        result = expenses + room_cost
        return f"Monthly consumption: {result:.2f}$."

        # total_amount_room_expenses = 0
        # for room in self.rooms:
        #     each_room_expense = room.expenses + room.room_cost
        #     total_amount_room_expenses += each_room_expense
        # return f"Monthly consumption: {total_amount_room_expenses:.2f}$."

    def pay(self):
        result = ""
        for room in self.rooms:
            each_room_expense = room.expenses + room.room_cost
            if each_room_expense > room.budget:
                result += f"{room.family_name} does not have enough budget and must leave the hotel." + "\n"
                self.rooms.remove(room)
            else:
                room.budget -= each_room_expense
                result += f"{room.family_name} paid {each_room_expense:.2f}$ and have {room.budget:.2f}$ left." + "\n"
        return result.strip()

    def status(self):
        result = ""
        people = sum([x.members_count for x in self.rooms])
        result += f"Total population: {people}" + "\n"
        for room in self.rooms:
            result += f"{room.family_name} with {room.members_count} " \
                      f"members. Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$" + "\n"
            if room.members_count > 2:
                for x in range(len(room.children)):
                    result += f"--- Child {x + 1} monthly cost: {room.children[x].cost * 30:.2f}$" + "\n"

            if room.appliances:
                result += f"--- Appliances monthly cost: {room.calculate_expenses(room.appliances):.2f}$" + "\n"

        return result.strip()

