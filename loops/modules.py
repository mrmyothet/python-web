import random

# randint(range)
num = random.randint(1, 10)
# print(num)

guess = 0


while guess != num:
    guess = int(input("Enter the number : "))
    if guess < num:
        print("Too low!")
    elif guess > num:
        print("Too high")

print("Congratulations!")
