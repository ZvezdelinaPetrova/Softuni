from collections import deque


def fill_the_box(height, length, width, *args):
    max_size = height * length * width
    d = deque(args)
    finished = False
    while d:
        current_el = d.popleft()
        if current_el == "Finish":
            finished = True
            break
        if max_size - current_el <= 0:
            result = current_el - max_size
            max_size = 0
            d.appendleft(result)
            break
        else:
            max_size -= current_el

    if max_size <= 0 and not finished:
        d = list(d)
        d = d[0:-1]
        return f"No more free space! You have {sum(d)} more cubes."
    else:
        return f"There is free space in the box. You could put {abs(max_size)} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))