from project.cat import Task


class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task):
        for x in self.tasks:
            if x.name == new_task.name:
                return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        for x in self.tasks:
            if x.name == task_name:
                x.completed = True
                return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        total = 0
        for x in self.tasks:
            # for y in x:
            if x.completed:
                total += 1
                self.tasks.remove(x)
        return f"Cleared {total} tasks."

    def view_section(self):
        result = ''
        result += f"Section {self.name}:" + "\n"

        for task in self.tasks:
            result += f"{task.details()}" + "\n"

        return result
