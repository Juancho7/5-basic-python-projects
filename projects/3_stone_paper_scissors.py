from random import choice


def stone_paper_scissors():
    user = input(
        "Choose an option:\nWrite sto for stone, pa for paper or sci for scissors: "
    ).lower()

    options = {"sto": "stone", "pa": "paper", "sci": "scissors"}
    machine = choice(list(options.keys()))

    if user == machine:
        return "\nTie! Machine chose {}.\n".format(options[machine])
    elif winner(user, machine):
        return "You win! Congratulations! Machine chose {}.".format(options[machine])
    else:
        return "You lose! Maybe next time! Machine chose {}.".format(options[machine])


def winner(user, machine):
    if (
        (user == "sto" and machine == "sci")
        or (user == "pa" and machine == "sto")
        or (user == "sci" and machine == "pa")
    ):
        return True

    return False


print("Welcome to Stone, Paper or Scissors!\n")
print(stone_paper_scissors())
