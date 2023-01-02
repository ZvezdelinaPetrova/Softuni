class Shop:

    def __init__(self, name, type, capacity):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = {}  # name of an item and its quantity

    def add_item(self, item_name):
        result = 0
        for key, value in self.items.items():
            result += value
        if result + 1 <= self.capacity:
            self.capacity -= 1
            if item_name not in self.items:
                self.items[item_name] = 1
            else:
                self.items[item_name] += 1
            return f"{item_name} added to the shop"

        return f"Not enough capacity in the shop"

    def remove_item(self, item_name, amount):
        if item_name in self.items:
            quantity = self.items[item_name]
            if quantity - amount > 0:
                self.items[item_name] -= amount
                return f"{amount} {item_name} removed from the shop"
            elif quantity - amount == 0:
                self.items.pop(item_name)
                # del self.items[item_name]
                return f"{amount} {item_name} removed from the shop"
        return f"Cannot remove {amount} {item_name}"

    @classmethod
    def small_shop(cls, name, type):
        return cls(name, type, 10)

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"


fresh_shop = Shop("Fresh Shop", "Fruit and Veg", 50)
small_shop = Shop.small_shop("Fashion Boutique", "Clothes")
print(fresh_shop)
print(small_shop)

print(fresh_shop.add_item("Bananas"))
print(fresh_shop.remove_item("Tomatoes", 2))

print(small_shop.add_item("Jeans"))
print(small_shop.add_item("Jeans"))
print(small_shop.remove_item("Jeans", 2))
print(small_shop.items)
