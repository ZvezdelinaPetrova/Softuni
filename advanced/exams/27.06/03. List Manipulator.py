from collections import deque


def list_manipulator(new_list, action, where, *args):
    l = deque(new_list)
    if action == "add":
        if where == "beginning":
            for x in reversed(args):
                l.appendleft(x)
            return list(l)
        elif where == "end":
            for x in args:
                l.append(x)
            return list(l)
    elif action == "remove":
        if args:
            number_to_remove = sum(args)
            if where == "beginning":
                while number_to_remove != 0:
                    if l:
                        l.popleft()
                        number_to_remove -= 1
                return list(l)
            elif where == "end":
                while number_to_remove != 0:
                    if l:
                        l.pop()
                        number_to_remove -= 1
                return list(l)
        else:
            if where == "beginning":
                l.popleft()
                return list(l)
            elif where == "end":
                l.pop()
                return list(l)


# from collections import deque
#
#
# def list_manipulator(list_object, operation, position, *args) -> list:
#     new_list = deque(list_object.copy())
#     if operation == 'add':
#         assert len(args) >= 0
#         if position == 'beginning':
#             new_list = deque(args) + new_list
#
#         elif position == 'end':
#             new_list += deque(args)
#
#     elif operation == 'remove':
#         assert 0 <= len(args) <= 1
#         n = args[0] if len(args) == 1 else 1
#         fn = new_list.popleft if position == 'beginning' else new_list.pop
#         for _ in range(n):
#             fn()
#
#     return list(new_list)


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))