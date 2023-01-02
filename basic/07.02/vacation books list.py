number_of_lists = int(input())
pages_per_hour = int(input())
days_to_read_the_book = int(input())
total_time_to_read_the_book = number_of_lists / pages_per_hour
needed_hours_per_day = total_time_to_read_the_book / days_to_read_the_book
print(needed_hours_per_day)


