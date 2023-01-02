movie = input()

total_tickets = 0
student_counter = 0
standard_counter = 0
kids_counter = 0
movie_counter = 0

while movie != "Finish":
    free_places = int(input())
    movie_counter += 1
    occupancy = 0
    while occupancy < free_places:
        type_ticket = input()
        if type_ticket == "End":
            movie_percent = abs(occupancy / free_places) * 100
            print(f"{movie} - {movie_percent:.2f}% full.")
            break
        occupancy += 1
        if type_ticket == "student":
            student_counter += 1
        elif type_ticket == "standard":
            standard_counter += 1
        elif type_ticket == "kid":
            kids_counter += 1
        if occupancy >= free_places:
            movie_percent = abs(occupancy / free_places) * 100
            print(f"{movie} - {movie_percent:.2f}% full.")
    movie = input()

total_tickets = kids_counter + standard_counter + student_counter
student_tickets_percentage = (student_counter / total_tickets) * 100
standard_tickets_percentage = (standard_counter / total_tickets) * 100
kids_tickets_percentage = (kids_counter / total_tickets) * 100
print(f"Total tickets: {total_tickets}")
print(f"{student_tickets_percentage:.2f}% student tickets.")
print(f"{standard_tickets_percentage:.2f}% standard tickets.")
print(f"{kids_tickets_percentage:.2f}% kids tickets.")

