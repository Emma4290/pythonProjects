import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

number_generator = random.randint(0, len(names)-1)
chosen_victim = names[number_generator]

print(f"{chosen_victim} is going to buy the meal today!")