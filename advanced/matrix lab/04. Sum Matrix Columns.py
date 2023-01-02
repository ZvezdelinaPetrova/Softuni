rows, columns = [int(x) for x in input().split(", ")]

matrix = []

results = []

for r in range(rows):
    matrix.append([int(x) for x in input().split(" ")])

for c in range(columns):
    current_sum = 0
    for r in range(rows):
        current_sum += matrix[r][c]
    results.append(current_sum)

for k in results:
    print(k)