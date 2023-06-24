# Pair programming

def word_count(s, word):
    count = 0
    for i in range(0, len(s) - 1):
        if word == s[i]:
            count += 1
    return count


s = list(input("Enter a sentence: ").split())
x = input("Enter a word to search: ")
print(f"The word - ({x}) appears {word_count(s,x)} times in the sentence.")