class Zoo:

    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget >= price and len(self.animals) + 1 <= self.__animal_capacity:
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        if self.__budget < price and self.__animal_capacity > 0:
            return f"Not enough budget"

        return f"Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) + 1 <= self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                self.__workers_capacity += 1
                return f"{worker_name} fired successfully"

        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total = 0
        for w in self.workers:
            total += w.salary

        if self.__budget >= total:
            self.__budget -= total
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return f"You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_b = 0
        for a in self.animals:
            total_b += a.money_for_care

        if self.__budget >= total_b:
            self.__budget -= total_b
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return f"You have no budget to tend the animals. They are unhappy."

    def workers_status(self):
        result = ""
        if self.workers:
            result += f"You have {len(self.workers)} workers" + "\n"
            keepers = [el for el in self.workers if el.__class__.__name__ == "Keeper"]
            care = [el for el in self.workers if el.__class__.__name__ == "Caretaker"]
            vets = [el for el in self.workers if el.__class__.__name__ == "Vet"]

            result += f"----- {len(keepers)} Keepers:" + "\n"
            for k in keepers:
                result += f"{k.__repr__()}" + "\n"

            result += f"----- {len(care)} Caretakers:" + "\n"
            for k in care:
                result += f"{k.__repr__()}" + "\n"

            result += f"----- {len(vets)} Vets:" + "\n"
            for k in vets:
                result += f"{k.__repr__()}" + "\n"

        return result.strip()

    def animals_status(self):
        result = ""
        if self.animals:
            result += f"You have {len(self.animals)} animals" + "\n"
            lions_list = [el for el in self.animals if el.__class__.__name__ == "Lion"]
            tigers = [el for el in self.animals if el.__class__.__name__ == "Tiger"]
            cheetahs = [el for el in self.animals if el.__class__.__name__ == "Cheetah"]

            result += f"----- {len(lions_list)} Lions:" + "\n"
            for l in lions_list:
                result += f"{l.__repr__()}" + "\n"

            result += f"----- {len(tigers)} Tigers:" + "\n"
            for l in tigers:
                result += f"{l.__repr__()}" + "\n"

            result += f"----- {len(cheetahs)} Cheetahs:" + "\n"
            for l in cheetahs:
                result += f"{l.__repr__()}" + "\n"

        return result.strip()

    def profit(self, amount):
        self.__budget += amount

# class Zoo:
#     def __init__(self, name, budget, animal_capacity, workers_capacity):
#         self.name = name
#         self.__budget = budget
#         self.__animal_capacity = animal_capacity
#         self.__workers_capacity = workers_capacity
#         self.animals = []
#         self.workers = []
#
#     def add_animal(self, animal, price):
#         if price <= self.__budget:
#             if len(self.animals) + 1 <= self.__animal_capacity:
#                 self.animals.append(animal)
#                 self.__budget -= price
#                 return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
#
#         if price > self.__budget:
#             return f"Not enough budget"
#
#         if price <= self.__budget:
#             if len(self.animals) + 1 > self.__animal_capacity:
#                 return f"Not enough space for animal"
#
#     def hire_worker(self, worker):
#         if len(self.workers) + 1 > self.__workers_capacity:
#             return f"Not enough space for worker"
#         self.workers.append(worker)
#         return f"{worker.name} the {worker.__class__.__name__} hired successfully"
#
#     def fire_worker(self, worker_name):
#         for worker in self.workers:
#             if worker.name == worker_name:
#                 self.workers.remove(worker)
#                 return f"{worker_name} fired successfully"
#         return f"There is no {worker_name} in the zoo"
#
#     def pay_workers(self):
#         total = 0
#
#         for worker in self.workers:
#             total += worker.salary
#
#         if total > self.__budget:
#             return f"You have no budget to pay your workers. They are unhappy"
#
#         self.__budget -= total
#         return f"You payed your workers. They are happy. Budget left: {self.__budget}"
#
#     def tend_animals(self):
#         total_money_for_care = 0
#         for animal in self.animals:
#             total_money_for_care += animal.money_for_care
#         if total_money_for_care > self.__budget:
#             return f"You have no budget to tend the animals. They are unhappy."
#         self.__budget -= total_money_for_care
#         return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
#
#     def profit(self, amount):
#         self.__budget += amount
#
#     def animals_status(self):
#         result = f"You have {len(self.animals)} animals" + "\n"
#
#         total_lions = 0
#         lions = []
#         for animal in self.animals:
#             if animal.__class__.__name__ == "Lion":
#                 total_lions += 1
#                 lions.append(animal)
#
#         result += f"----- {total_lions} Lions:" + "\n"
#         for lion in lions:
#             result += lion.__repr__() + "\n"
#
#         total_tigers = 0
#         tigers = []
#         for animal in self.animals:
#             if animal.__class__.__name__ == "Tiger":
#                 total_tigers += 1
#                 tigers.append(animal)
#
#         result += f"----- {total_tigers} Tigers:" + "\n"
#         for tiger in tigers:
#             result += tiger.__repr__() + "\n"
#
#         total_cheetahs = 0
#         cheetahs = []
#         for animal in self.animals:
#             if animal.__class__.__name__ == "Cheetah":
#                 total_cheetahs += 1
#                 cheetahs.append(animal)
#
#         result += f"----- {total_cheetahs} Cheetahs:" + "\n"
#         for cheetah in cheetahs:
#             result += cheetah.__repr__() + "\n"
#
#         return result.strip()
#
#     def workers_status(self):
#         result = f"You have {len(self.workers)} workers" + "\n"
#
#         total_keepers = 0
#         keepers = []
#         for keeper in self.workers:
#             if keeper.__class__.__name__ == "Keeper":
#                 total_keepers += 1
#                 keepers.append(keeper)
#
#         result += f"----- {total_keepers} Keepers:" + "\n"
#         for keeper in keepers:
#             result += keeper.__repr__() + "\n"
#
#         total_caretakers = 0
#         caretakers = []
#         for worker in self.workers:
#             if worker.__class__.__name__ == "Caretaker":
#                 total_caretakers += 1
#                 caretakers.append(worker)
#
#         result += f"----- {total_caretakers} Caretakers:" + "\n"
#         for caretaker in caretakers:
#             result += caretaker.__repr__() + "\n"
#
#         total_vets = 0
#         vets = []
#         for worker in self.workers:
#             if worker.__class__.__name__ == "Vet":
#                 total_vets += 1
#                 vets.append(worker)
#
#         result += f"----- {total_vets} Vets:" + "\n"
#         for vet in vets:
#             result += vet.__repr__() + "\n"
#
#         return result.strip()
