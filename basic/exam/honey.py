from math import floor

flight_company = int(input())
counter_flights = 0
passengers = 0

for i in range(flight_company):
    flight_company_name = input()
    passengers = 0
    counter_flights = 0
    while flight_company_name != "Finish":
        new_command = input()
        if new_command == "Finish":
            average_passengers = floor(passengers / counter_flights)
            print(f"{flight_company_name}: {average_passengers} passengers.")
            break
        counter_flights += 1
        new_passes = int(new_command)
        passengers += new_passes




