n_e = int(input())
n_a = int(input())


for i in range(n_e, 0, - 1):
    for j in range(0, n_a):
        if i % 2 == 0:
            if i == n_e:
                print(f"L{i}{j}", end=" ")
            else:
                print(f"O{i}{j}", end=" ")
        elif i % 2 == 1:
            if i == n_e:
                print(f"L{i}{j}", end=" ")
            else:
                print(f"A{i}{j}", end=" ")
    print()



#L{номер на етажа}{номер на апартамента}
#А{номер на етажа}{номер на апартамента}
#О{номер на етажа}{номер на офиса}
