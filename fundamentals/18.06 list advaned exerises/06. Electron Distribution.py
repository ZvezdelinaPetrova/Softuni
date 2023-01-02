number = int(input())
n = 1
shell = []
counter = number
while True:
    max_electrons = 2 * n ** 2
    n += 1
    if counter <= max_electrons:
        last_shell = counter
        shell.append(counter)
        break
    shell.append(max_electrons)
    counter -= max_electrons

print(shell)