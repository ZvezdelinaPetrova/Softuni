n = int(input())

longest = {}

for _ in range(n):
    first, second = input().split("-")
    start_f, end_f = first.split(",")
    start_s, end_s = second.split(",")
    list_1 = {x for x in range(int(start_f), int(end_f) + 1)}
    list_2 = {x for x in range(int(start_s), int(end_s) + 1)}
    current_intersection = list_1.intersection(list_2)
    if len(longest) < len(current_intersection):
        longest = current_intersection

print(f"Longest intersection is {[x for x in longest]} with length {len(longest)}")


# n = int(input())
#
# longest_set = set()
#
# for _ in range(n):
#     first_set = set()
#     second_set = set()
#     data = input().split("-")
#     first = data[0].split(",")
#     second = data[1].split(",")
#     first_start = int(first[0])
#     first_end = int(first[1])
#     second_start = int(second[0])
#     second_end = int(second[1])
#     for m in range(first_start, first_end + 1):
#         first_set.add(m)
#     for j in range(second_start, second_end + 1):
#         second_set.add(j)
#     result = first_set.intersection(second_set)
#     if len(result) > len(longest_set):
#         longest_set = result
#
#
# print(f"Longest intersection is {[i for i in longest_set]} with length {len(longest_set)}")