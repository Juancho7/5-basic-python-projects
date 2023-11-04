from random import randint


print("-----------------------------------------------------------------------")
print("-------------------- Hello, I Am The Machine, Welcome! ----------------")
print("------------- I will guess the number you're thinking on! -------------")
print("-----------------------------------------------------------------------\n")

x = int(input("The number you're thinking is in the range of 1 to?: "))
print(
    "\n--------- The number you're thinking is in the range of 1 to {} --------\n".format(
        x
    )
)

attempts_given = 0

while attempts_given < 3:
    attempts_given = int(input("How many attempts do you give me? Minimum 3: "))

    if attempts_given < 3:
        print("Come on! Minimun 3 please")

feedback = ""
minimum_limit = 1
maximum_limit = x
attempts_done = 1

while feedback != "C" and attempts_given >= 1:
    prediction = randint(minimum_limit, maximum_limit)

    feedback = input(
        f"\nMy prediction is {prediction}.\nIf your number is smaller write A, if your number is greater write B, if it's correct write C: "
    ).upper()

    if feedback == "A":
        maximum_limit = prediction - 1
        attempts_given -= 1
        attempts_done += 1

    if feedback == "B":
        minimum_limit = prediction + 1
        attempts_given -= 1
        attempts_done += 1


if attempts_given < 1:
    print("\nI lost! You won! Congratulations!")
else:
    print(f"\nI did it on {attempts_done} attempts! Nice to play with you!")
