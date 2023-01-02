from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.cat import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):

        # subscription = Gym.find_object(self, subscription_id, self.subscriptions)
        # customer = Gym.find_object(self, subscription_id, self.customers)
        # trainer = Gym.find_object(self, subscription_id, self.trainers)
        # plan = Gym.find_object(self, subscription_id, self.plans)
        # equipment = Gym.find_object(self, subscription_id, self.equipment)

        subscription = self.__get_object_by_id(self.subscriptions, subscription_id)
        c = subscription.customer_id
        customer = self.__get_object_by_id(self.customers, c)
        t = subscription.trainer_id
        trainer = self.__get_object_by_id(self.trainers, t)
        p = subscription.exercise_id
        plan = self.__get_object_by_id(self.plans, p)
        e = plan.equipment_id
        equipment = self.__get_object_by_id(self.equipment, e)

        result = f"{subscription.__repr__()}" + "\n"
        result += f"{customer.__repr__()}" + "\n"
        result += f"{trainer.__repr__()}" + "\n"
        result += f"{equipment.__repr__()}" + "\n"
        result += f"{plan.__repr__()}" + "\n"
        return result.strip()

        # result = str(subscription) + '\n'
        # result += str(customer) + '\n'
        # result += str(trainer) + '\n'
        # result += str(equipment) + '\n'
        # result += str(plan) + '\n'
        # return result


    def __get_object_by_id(self, objects, id):
        for obj in objects:
            if obj.id == id:
                return obj