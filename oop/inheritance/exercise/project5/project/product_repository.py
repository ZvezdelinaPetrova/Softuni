# from project.product import Product
from oop.inheritance.exercise.project5.project.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name):
        for product in self.products:
            if product.name == product_name:
                return product_name
        return None

    def remove(self, product_name):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)

    def __repr__(self):
        result = ''
        for product in self.products:
            result += f"{product.name}: {product.quantity}" + "\n"

        return result.strip()