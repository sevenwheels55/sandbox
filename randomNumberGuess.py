import random

num = random.randint(1, 9)
again = False
try:
    while again == False:
        guess = input("Please input a number: ")
        if guess == "exit":
            print("The game has ended.")
            again = True
        else:
            guess = int(guess)
            if guess == num:
                print("You got it!")
                again = True
            elif guess > num:
                print("Your guess is too high.")
            else:
                print("Your guess is too low.")
except:
    print("No problem")
