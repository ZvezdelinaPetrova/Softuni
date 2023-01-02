book = input()

book_counter = 0
is_book_found = False

new_book = input()
while new_book != "No More Books":
    if new_book == book:
        is_book_found = True
        break
    book_counter += 1
    new_book = input()

if is_book_found:
    print(f"You checked {book_counter} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {book_counter} books.")
