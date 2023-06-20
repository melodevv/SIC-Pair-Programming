# Pair programming

def word_count(S, word):
    count = 1
    for i in S:
        if word in i:
            count += 1
            return count
        else:
            count = 0

    return count


S = list(input("Enter a sentence: ").split())
x = input("Enter a word to search: ")
print(f"The word - ({x}) appears {word_count(S,x)} times in the sentence.")
