gifts = input().split()
new_command = ''
while new_command != "No Money":
    new_command = input()
    output = new_command.split()
    if output[0] == "OutOfStock":
        searched_word = output[1]
        for i in range(len(gifts)):
            if gifts[i] == searched_word:
                gifts[i] = "None"
    elif output[0] == "Required":
        if int(output[2]) <= len(gifts):
            given_index = int(output[2])
            for j in range(len(gifts)):
                if j == given_index:
                    replaced_word = output[1]
                    gifts[j] = replaced_word
    elif output[0] == "JustInCase":
        last_gift = len(gifts) - 1
        for m in range(len(gifts)):
            if m == last_gift:
                n = output[1]
                gifts[m] = n
for g in gifts:
    if g != "None":
        print(g, end=" ")
