import random
import math

a = int(input("Enter starting number: "))
b = int(input("Enter ending number: "))

c = random.randint(a,b)
d = round(math.log(b -a+1,2))
print(f"You have only {d} chances to gues a number")

count = 0
while count < d:
    count+=1

    guess = int(input("Guess a number: "))

    if c == guess:
        print(f"Congratulations you did it in {count} try")
        break
    elif c > guess:
        print("You guessed too small")
    elif c < guess:
        print("You guessed too high")

if count >= d:
    print("\nThe number is %d" % c)
    print("\tBetter Luck Next time!")