from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable
from project.table.table import Table
import os

class Bakery:
    def __init__(self, name):
        self.name = name
        self.food_menu = []  # every type of food in the bakery's menu
        self.drinks_menu = []  # every type of drinks in the bakery's menu
        self.tables_repository = []  # every table at the bakery
        self.total_income = 0  # total income from all the COMPLETED bills

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError(f"Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):
        if food_type != "Bread" and food_type != "Cake":
            return
        for x in self.food_menu:
            if x.name == name:
                raise Exception(f"{food_type} {name} is already in the menu!")
        if food_type == "Bread":
            new_food = Bread(name, price)
            self.food_menu.append(new_food)
            return f"Added {name} ({food_type}) to the food menu"
        if food_type == "Cake":
            new_food = Cake(name, price)
            self.food_menu.append(new_food)
            return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand:str):
        if drink_type != "Tea" and drink_type != "Water":
            return
        for x in self.drinks_menu:
            if x.name == name:
                raise Exception(f"{drink_type} {name} is already in the menu!")
        if drink_type == "Tea":
            new_drink = Tea(name, portion, brand)
            self.drinks_menu.append(new_drink)
            return f"Added {name} ({drink_type}) to the drink menu"
        if drink_type == "Water":
            new_drink = Water(name, portion, brand)
            self.drinks_menu.append(new_drink)
            return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        if table_type != "InsideTable" and table_type != "OutsideTable":
            return

        for x in self.tables_repository:
            if x.table_number == table_number:
                raise Exception(f"Table {table_number} is already in the bakery!")

        if table_type == "InsideTable":
            new_table = InsideTable(table_number, capacity)
            self.tables_repository.append(new_table)
            return f"Added table number {table_number} in the bakery"

        if table_type == "OutsideTable":
            new_table = OutsideTable(table_number, capacity)
            self.tables_repository.append(new_table)
            return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        for x in self.tables_repository:
            if not x.is_reserved and (x.capacity >= number_of_people):
                x.reserve(number_of_people)
                x.is_reserved = True
                return f"Table {x.table_number} has been reserved for {number_of_people} people"
        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *food_names):
        table = Bakery.find_object(table_number, self.tables_repository)
        if not table:
            return f"Could not find table {table_number}"
        food_could_be_ordered = []
        ordered_food_by_name = []

        for x in food_names:
            for item in self.food_menu:
                if item.name == x:
                    food_could_be_ordered.append(item)
                    ordered_food_by_name.append(item.name)
                    table.food_orders.append(item)
                    break
        not_ordered = [f for f in food_names if f not in ordered_food_by_name]

        result = ""
        result += f"Table {table_number} ordered:" + "\n"

        for x in table.food_orders:
            result += f" - {x.name}: {x.portion:.2f}g - {x.price:.2f}lv" + "\n"

        result += f"{self.name} does not have in the menu:" + "\n"

        for x in not_ordered:
            result += f"{x}" + "\n"
        return result.strip()

    def order_drink(self, table_number: int, *drink_names):
        table = Bakery.find_object(table_number, self.tables_repository)
        if not table:
            return f"Could not find table {table_number}"

        drinks_could_be_ordered = []
        ordered_drinks_by_name = []

        for item in drink_names:
            for drink in self.drinks_menu:
                if item == drink.name:
                    drinks_could_be_ordered.append(drink)
                    ordered_drinks_by_name.append(drink.name)
                    table.drink_orders.append(drink)
                    break
        not_ordered_drinks = [d for d in drink_names if d not in ordered_drinks_by_name]

        result = ""
        result += f"Table {table_number} ordered:" + "\n"

        for x in table.drink_orders:
            result += f"- {x.name} {x.brand} - {x.portion:2f}ml - {x.price:2f}lv" + "\n"

        result += f"{self.name} does not have in the menu:" + "\n"

        for x in not_ordered_drinks:
            result += f"{x}" + "\n"
        return result.strip()

    def leave_table(self, table_number: int):
        table_to_leave = [t for t in self.tables_repository if t.table_number == table_number]
        if not table_to_leave:
            return
        if table_to_leave:
            bill = table_to_leave[0].get_bill()
            self.total_income += bill
            table_to_leave[0].clear()

            result = f"Table: {table_number}" + "\n"
            result += f"Bill: {bill:.2f}"
            return result

    def get_free_tables_info(self):
        result = ""
        for x in self.tables_repository:
            if not x.is_reserved:
                result += f"{x.free_table_info()}" + "\n"
        return result.strip()

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"

    @staticmethod
    def find_object(provided_number, list_with_objects):
        for obj in list_with_objects:
            if obj.table_number == provided_number:
                return obj


