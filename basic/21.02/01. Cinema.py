type_of_the_movie = input()
rows = int(input())
columns = int(input())

# traybva da anmerim lceto na mestata v zalata = rows * columns
# traybva da napraim if za da precenim po tipa zala kolko pari do vtori znak

full_hall = rows * columns
price = 0

if type_of_the_movie == "Premiere":
    price = full_hall * 12
elif type_of_the_movie == "Normal":
    price = full_hall * 7.5
elif type_of_the_movie == "Discount":
    price = full_hall * 5
print(f"{price:.2f}")

