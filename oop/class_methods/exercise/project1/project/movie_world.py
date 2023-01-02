# from oop.class_methods.exercise.project1.project.customer import Customer
# from oop.class_methods.exercise.project1.project.dvd import DVD

from project.customer import Customer
from project.equipment import DVD

class MovieWorld:

    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer):
        if len(self.customers) + 1 <= MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) + 1 <= MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        customer = self.__get_object_by_id(self.customers, customer_id)
        dvd = self.__get_object_by_id(self.dvds, dvd_id)

        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"
        if dvd.is_rented:
            return f"DVD is already rented"
        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        customer.rented_dvds.append(dvd)
        dvd.is_rented = True
        return f"{customer.name} has successfully rented {dvd.name}"

    def __get_object_by_id(self, objects, id):
        for obj in objects:
            if obj.id == id:
                return obj

    def return_dvd(self, customer_id, dvd_id):
        customer = self.__get_object_by_id(self.customers, customer_id)
        dvd = self.__get_object_by_id(self.dvds, dvd_id)

        if dvd in customer.rented_dvds:
            customer.rented_dvds.remove(dvd)
            dvd.is_rented = False
            return f"{customer.name} has successfully returned {dvd.name}"
        return f"{customer.name} does not have that DVD"

    def __repr__(self):
        result = ""

        for customer in self.customers:
            result += f"{customer.__repr__()}" + "\n"

        for dvd in self.dvds:
            result += f"{dvd.__repr__()}" + "\n"

        return result.strip()

