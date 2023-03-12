import random


bet_amount = float(input("How much would you like to bet? "))
red_or_black = input("Red or black? ")
number_up_to_100 = float(input("Pick a number between 1 and 100. "))


def colour():
    random_number = random.randint(1, 2)

    if random_number == 1:
        colour = "red"

    else:
        colour = "black"

    return colour


colour_result = colour()
print("The colour is {}.".format(colour_result))

if red_or_black == colour_result:
    print("{}.".format(bet_amount), "You keep what you bet!")

else:
    print("No colour match this time!")


def number():
    random_number = random.randint(1, 100)
    return random_number


number_result = number()
print("The number is {}.".format(number_result))

if number_up_to_100 == number_result:
    total = (bet_amount * 2)
    print(print("{}.".format(total), "You have doubled what you bet!"))

else:
    print("No number match this time!")

if number_up_to_100 == number_result and red_or_black == colour_result:
    winning_total = (bet_amount * 100)
    print(print("{}.".format(winning_total), "You have won 100 times what you bet! Congratulations!"))

elif number_up_to_100 != number_result and red_or_black != colour_result:
    print("You haven't managed to match anything. You win nothing.")

else:
    print("You didn't manage to match both! Halfway there!")