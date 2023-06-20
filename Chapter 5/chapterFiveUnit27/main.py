def are_anagrams(str1, str2):
    str1 = str1.lower().replace(" ", "").strip()
    str2 = str2.lower().replace(" ", "").strip()

    if len(str1) != len(str2):
        return False

    freq1 = {}
    freq2 = {}

    for char in str1:
        if char in freq1:
            freq1[char] += 1
        else:
            freq1[char] = 1

    for char in str2:
        if char in freq2:
            freq2[char] += 1
        else:
            freq2[char] = 1

    return freq1 == freq2


word1 = input("Enter first word:")
word2 = input("Enter second word:")

if are_anagrams(word1, word2):
    print("True")
else:
    print("False")
