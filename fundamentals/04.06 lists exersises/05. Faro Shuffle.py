cards = input().split()
numbers = int(input())

length_of_decks = int(len(cards) / 2)
current_list = cards
final_list = []

for i in range(numbers):
    final_list = []
    deck_a = current_list[:length_of_decks]
    deck_b = current_list[length_of_decks:]
    for j in range(length_of_decks):
        final_list.append(deck_a[j])
        final_list.append(deck_b[j])
    current_list = final_list
print(final_list)
