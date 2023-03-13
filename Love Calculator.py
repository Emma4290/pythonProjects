print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

lower_name = name1.lower() + name2.lower()

t = lower_name.count("t")
r = lower_name.count("r")
u = lower_name.count("u")
e = lower_name.count("e")

l = lower_name.count("l")
o = lower_name.count("o")
v = lower_name.count("v")
e2 = lower_name.count("e")

true = int(t) + int(r) + int(u) + int(e)
love = int(l) + int(o) + int(v) + int(e2)

true_love = str(true) + str(love)
true_love_int = int(true_love)

if true_love_int < 10 or true_love_int > 90:
    print(f"Your score is {true_love}, you go together like coke and mentos.")

elif true_love_int >= 40 and true_love_int <= 50:
    print(f"Your score is {true_love}, you are alright together.")

else:
    print(f"Your score is {true_love}.")