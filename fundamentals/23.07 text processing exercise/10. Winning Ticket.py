tickets = input().split(", ")
new_list = [el.strip() for el in tickets]

winning_at = "@" * 6
winning_hash = "#" * 6
winning_tent = "^" * 6
winning_dollar = "$" * 6
winning_sign = ''


for ticket in new_list:
    if len(ticket) == 20:
        left_half = ticket[:10]
        right_half = ticket[10:]
        if winning_at in left_half and winning_at in right_half:
            winning_sign = "@"
            how_many_times = left_half.count("@")
            how_many_times_2 = right_half.count("@")
            result = min(how_many_times, how_many_times_2)
            if result == 10:
                print(f'ticket "{ticket}" - {result}{winning_sign} Jackpot!')
            else:
                print(f'ticket "{ticket}" - {result}{winning_sign}')
        elif winning_hash in left_half and winning_hash in right_half:
            winning_sign = "#"
            how_many_times = left_half.count("#")
            how_many_times_2 = right_half.count("#")
            result = min(how_many_times, how_many_times_2)
            if result == 10:
                print(f'ticket "{ticket}" - {result}{winning_sign} Jackpot!')
            else:
                print(f'ticket "{ticket}" - {result}{winning_sign}')
        elif winning_tent in left_half and winning_tent in right_half:
            winning_sign = "^"
            how_many_times = left_half.count("^")
            how_many_times_2 = right_half.count("^")
            result = min(how_many_times, how_many_times_2)
            if result == 10:
                print(f'ticket "{ticket}" - {result}{winning_sign} Jackpot!')
            else:
                print(f'ticket "{ticket}" - {result}{winning_sign}')
        elif winning_dollar in left_half and winning_dollar in right_half:
            winning_sign = "$"
            how_many_times = left_half.count("$")
            how_many_times_2 = right_half.count("$")
            result = min(how_many_times, how_many_times_2)
            if result == 10:
                print(f'ticket "{ticket}" - {result}{winning_sign} Jackpot!')
            else:
                print(f'ticket "{ticket}" - {result}{winning_sign}')
        else:
            print(f'ticket "{ticket}" - no match')
    else:
        print("invalid ticket")

