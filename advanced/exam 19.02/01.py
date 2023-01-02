from collections import deque

vowels = deque([x for x in input().split()])
consonants = deque((x for x in input().split()))

flowers = {"rose", "tulip", "lotus", "daffodil"}
letters_found = []

test = []
found = False
found_word = ""
while vowels and consonants:
    current_vowel = vowels.popleft()
    current_c = consonants.pop()
    for el in flowers:
        if current_vowel in el:
            letters_found.append(current_vowel)
        if current_c in el:
            letters_found.append(current_c)
    for flower in flowers:
        new = set(letters_found)
        check = set(flower)
        if check.issubset(new):
            found = True
            found_word = flower
            break
        if found:
            break
    if found:
        break

if found:
    print(f"Word found: {found_word}")
else:
    print(f"Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(str(x) for x in vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(str(x) for x in consonants)}")