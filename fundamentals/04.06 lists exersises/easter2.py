gifts = input().split()
new_command = input()
while new_command != "No Money":
    output = new_command.split()
    if output[0] == "OutOfStock":
        searched_word = output[1]
        for i in range(len(gifts)):
            if gifts[i] == searched_word:
                gifts[i] = "None"
    elif output[0] == "Required":
        given_index = int(output[2])
        if 0 <= given_index < len(gifts):
            replaced_word = output[1]
            gifts[given_index] = replaced_word
    elif output[0] == "JustInCase":
        last_gift = len(gifts) - 1
        for m in range(len(gifts)):
            if m == last_gift:
                n = output[1]
                gifts[m] = n
    new_command = input()
for g in gifts:
    if g != "None":
        print(g, end=" ")
