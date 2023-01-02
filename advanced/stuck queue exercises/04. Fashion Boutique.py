clothes = [int(i) for i in input().split()]

rack_capacity = int(input())

racks = 1
counter = 0

while clothes:
    current_number = clothes[-1]
    if current_number + counter <= rack_capacity:
        counter += current_number
        clothes.pop()
    else:
        if len(clothes) > 0:
            racks += 1
            counter = 0

print(racks)


# clothes = [int(x) for x in input().split()]
#
# capacity = int(input())
# result = 0
# racks = 0
#
# while clothes:
#     racks += 1
#     current_capacity = capacity
#     result = 0
#     if len(clothes) == 0:
#         break
#     current_clothing = clothes.pop()
#     if len(clothes) == 0:
#         break
#     next_clothing = clothes[-1]
#     result += current_clothing + next_clothing
#     if result > current_capacity:
#         continue
#
#     elif result == current_capacity:
#         clothes.pop()
#         continue
#
#     elif result < current_capacity:
#         current_capacity -= result
#         clothes.pop()
#         while current_capacity > 0:
#             if len(clothes) == 0:
#                 break
#             next_c = clothes[-1]
#             if current_capacity - next_c < 0:
#                 break
#             elif current_capacity - next_c == 0:
#                 clothes.pop()
#                 break
#             else:
#                 clothes.pop()
#                 current_capacity -= next_c
#
# print(racks)
