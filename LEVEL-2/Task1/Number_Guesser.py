import random

randNumber = random.randint(1,100)
userGuess = True

attempts = 0

print("*******Welcome to the Guessing Game!*******")

while(userGuess is not randNumber):
    
        userGuess = int(input("Enter your Guess: "))
        attempts += 1

        if (userGuess == randNumber):
           print("Congratulation! You guessed it Right!")

        elif(userGuess > 100):
            print("Please enter a valid number.From 1 to 100 any number")

        else:
            if (userGuess>randNumber):
                print("Incorrect Guess", "Too high! Try again. Enter a smaller number.")
        
            else:
                print("Incorrect Guess", "Too low! Try again. Enter a larger number.")




print(f"****You guessed the correct number {userGuess} in {attempts} attempts****")

