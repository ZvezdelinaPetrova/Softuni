def print_ascii_code(chr_1, chr_2):
    first_letter = ord(chr_1)
    end_letter = ord(chr_2)
    new_list = []
    for ch in range(first_letter + 1, end_letter):
        next_symbol = chr(ch)
        new_list.append(next_symbol)
    return new_list


first_symbol = input()
end_symbol = input()

result = print_ascii_code(first_symbol, end_symbol)
print(" ".join(result))