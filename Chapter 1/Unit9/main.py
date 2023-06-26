# Q1
def is_palindrome_number(n):
    num_str = str(n)
    if num_str == num_str[::-1]:
        return True
    else:
        return False
num = int(input("Enter an integer: "))
if is_palindrome_number(num):
    print(num, "is a palindrome number")
else:
    print(num, "is not a palindrome number")

# Q2
import random
correct_answer = random.randint(1, 100)
num_of_tries = 0
while True:
    guess = int(input("Guess a number between 1 to 100\nEnter a number: "))
    num_of_tries += 1
    if guess == correct_answer:
        print("Congratulations. Total try =", num_of_tries)
        break
    elif guess < correct_answer:
        print("Higher!")
    else:
        print("Lower!")