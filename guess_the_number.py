import random


print("---------------------- Welcome to Guess the Number! ---------------------")
print("------ You,ve got to guess what was the number generated randomly! ------")
print("-------------------------------------------------------------------------\n")

x = int(input("The range of guessing will be from 1 to? "))
print(
    "\n---------The number you have to guess is in the range of 1 to {}---------\n".format(
        x
    )
)

number_to_guess = random.randint(1, x)

prediction = 0

while prediction != number_to_guess:
    prediction = int(input("Write a number: "))

    if prediction > number_to_guess:
        print("Ups! You failed, number you gave is too big!")

    if prediction < number_to_guess:
        print("Ups! You failed, number you gave is too small!")

print("Congratulations! You guessed the number!")
