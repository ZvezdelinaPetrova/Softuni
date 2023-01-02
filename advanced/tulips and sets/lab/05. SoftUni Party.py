guest_count = int(input())

regular = []
vip = []

expected_guests = []

for x in range(guest_count):
    guest = input()
    expected_guests.append(guest)

command = input()

while command != "END":
    current_guest = command
    if current_guest in expected_guests:
        expected_guests.remove(current_guest)
    command = input()

for x in expected_guests:
    for letter in x:
        if letter.isdigit():
            vip.append(x)
            break
        else:
            regular.append(x)
            break
print(len(expected_guests))

for i in sorted(vip):
    print(i)

for j in sorted(regular):
    print(j)


#
# n = int(input())
#
# vip_guests = set()
# regular_guests = set()
#
# for _ in range(n):
#     ticket = input()
#     if ticket[0].isdigit() and len(ticket) == 8:
#         vip_guests.add(ticket)
#     elif len(ticket) == 8:
#         regular_guests.add(ticket)
#
# guest = input()
#
# not_on_the_party = []
#
# while guest != "END":
#     if guest in vip_guests:
#         vip_guests.remove(guest)
#     elif guest in regular_guests:
#         regular_guests.remove(guest)
#     guest = input()
#
# print(len(vip_guests) + len(regular_guests))
#
# for i in sorted(vip_guests):
#     print(i)
# for j in sorted(regular_guests):
#     print(j)