from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.bakery import Bakery
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable
from project.table.table import Table


i = InsideTable(40, 20)
c = Cake("Chese", 2.50)
d = Tea("Te", 100, "BlackTea")
print(i.table_number)
i.reserve(10)
print(i.is_reserved)
i.order_food(c)
i.order_food(d)
print(i.get_bill())
i.clear()
print(i.free_table_info())
print(i.get_bill())

b = Bakery("Moe")
b.food_menu = [c]
print(b.food_menu[0].name)
b.add_food("Cake", "Chese", 1.2)
print(len(b.food_menu))