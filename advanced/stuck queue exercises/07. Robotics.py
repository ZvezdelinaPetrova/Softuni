from collections import deque


def get_seconds_from_time(start_time):  # превръщане от стринг на секунди
    h, m, s = start_time.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)


def new_seconds(previous_seconds):  # добавяне на 1 секунда към миналото време
    previous_seconds += 1
    return previous_seconds


def sec_to_hours(seconds):  # превръщане на секунди в стринг - час, минути, секунди
    h = seconds // 3600 % 24
    m = (seconds % 3600) // 60
    s = (seconds % 3600) % 60
    result = f'[{h:02d}:{m:02d}:{s:02d}]'

    return result


robots = deque(input().split(";"))
starting_time = input()

products = deque()

command = input()
while command != "End":
    products.append(command)
    command = input()

time = get_seconds_from_time(starting_time)

robots_dict = {}

for robot in robots:
    name, processing_time = robot.split("-")
    robots_dict[name] = int(processing_time)

available_robots = deque([x.split("-")[0] for x in robots])  # взимам само имента на роботите
processing_robots = {}

while products:
    current_product = products.popleft()

    next_seconds = new_seconds(time)
    time = next_seconds
    current_time = sec_to_hours(time)

    for process_r in [x for x in processing_robots]:
        processing_robots[process_r] -= 1
        if processing_robots[process_r] <= 0:
            processing_robots.pop(process_r)

    for robot_name in available_robots:
        if robot_name not in processing_robots:
            print(f"{robot_name} - {current_product} {current_time}")
            processing_robots[robot_name] = robots_dict[robot_name]
            break
    else:
        products.append(current_product)