n = int(input())
result = ""
for x in range(n):
    stars = x + 1
    spaces = n - x - 1
    result += ' ' * spaces + ' '.join('*' * stars) + '\n'


for h in range(n-2, -1, -1):
    stars = h + 1
    spaces = n - h - 1
    result += ' ' * spaces + ' '.join('*' * stars) + '\n'

print(result)