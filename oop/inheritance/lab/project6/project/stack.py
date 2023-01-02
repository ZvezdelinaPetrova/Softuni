class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        if self.data:
            return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        if not self.data:
            return True
        return False

    def __str__(self):
        return f"[{', '.join(reversed(self.data))}]"


a = Stack()
a.push("1")
a.push("3")
a.push("5")
print(a)
