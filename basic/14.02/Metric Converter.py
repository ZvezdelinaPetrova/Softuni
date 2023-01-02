number = float(input())
m_1 = input()
m_2 = input()

if m_1 == "mm" and m_2 == "m":
    number = number / 1000
    print(f"{number:.3f}")
elif m_1 == "mm" and m_2 == "cm":
    number = number / 10
    print(f"{number:.3f}")

elif m_1 == "m" and m_2 == "cm":
    number = number * 100
    print(f"{number:.3f}")
elif m_1 == "m" and m_2 == "mm":
    number = number * 1000
    print(f"{number:.3f}")

elif m_1 == "cm" and m_2 == "mm":
    number = number * 10
    print(f"{number:.3f}")
elif m_1 == "cm" and m_2 == "m":
    number = number / 100
    print(f"{number:.3f}")


#print(f"{number:.3f}")
