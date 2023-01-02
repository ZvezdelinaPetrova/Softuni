def palindrome(word, index=0, left_index = -1):
    if index == len(word) // 2:
        return f'{word} is a palindrome'
    if not word[index] == word[left_index]:
        return f'{word} is not a palindrome'

    return palindrome(word, index+1, left_index-1)


print(palindrome("abcdba", 0))
print(palindrome("peter", 0))
