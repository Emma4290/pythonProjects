import random

print("This is the lottery!")

ticket = [3, 15, 19, 27, 34, 45, 49]
ti = (sorted(ticket))

number1 = random.randint(1, 50)
number2 = random.randint(1, 50)
number3 = random.randint(1, 50)
number4 = random.randint(1, 50)
number5 = random.randint(1, 50)
number6 = random.randint(1, 50)
number7 = random.randint(1, 50)

lottery = [number1, number2, number3, number4, number5, number6, number7]
lot = sorted(lottery)

points = 0
for number in ti:
    if number in lot:
        points = points + 1

print(f"Lottery numbers: {lot}")
print(f"Ticket: {ti}")
print(f"You got {points} matches.")

if points < 3:
    print("Better luck next time!")
if points == 3:
    print("You matched 3 numbers and win £20. Congratulations!")
if points == 4:
    print("You matched 4 numbers and win £40. Congratulations!")
if points == 5:
    print("You matched 5 numbers and win £100. Congratulations!")
if points == 6:
    print("You matched 6 numbers and win £10000. Congratulations!")
if points == 7:
    print("You matched 7 numbers and win £1000000. Congratulations!")