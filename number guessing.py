import random

def game():
    a = int(input("Enter a range of number you want to guess through :"))
    guesses = 0 
    random_number = random.randint(0,a)
    while True:
        guesses += 1
        user_guess = int(input("Make a guess : "))
        if user_guess == random_number:
            print("You got it!")
            print("You got it in" ,guesses,"guesses")
            break
        else:
            print("You got it wrong")
            if random_number > user_guess:
                    print("Your guess is smaller than the actual number.")
            if random_number < user_guess:
                    print("Your guess is bigger than the actual number")

game()
