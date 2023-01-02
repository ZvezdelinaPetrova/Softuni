n = int(input())
m = int(input())


for symbol_1 in range(1, n):
    for symbol_2 in range(1, n):
        for symbol_3 in range(1, m + 1):
            new_letter = chr(96 + symbol_3)
            for symbol_4 in range(1, m + 1):
                next_letter = chr(96 + symbol_4)
                for symbol_5 in range(1, n + 1):
                    if symbol_1 > symbol_5 and symbol_2 > symbol_5:
                        continue
                    elif symbol_1 < symbol_5 and symbol_2 < symbol_5:
                        last_symbol = symbol_5
                        print(f"{symbol_1}{symbol_2}{new_letter}{next_letter}{last_symbol}", end=" ")
