from random import randint

range = int(input("Enter the range of the numbers (0 is the starting number): "))

randomly_generated_number = randint(0, range)

count = 0
num_tries = range//10*4

print(f"\nYou have {num_tries} tries to guess the number!\n")

user_guess = int(input("Enter your guess: "))

if user_guess == randomly_generated_number:
    print("You guessed correctly on your first try!")
else:
    count += 1
    while user_guess is not randomly_generated_number:
        if num_tries-count == 0:
            print("You have used all your guesses! You lose!")
            break
        if user_guess < randomly_generated_number:
            print("You guessed too low! Please try again!")
            print(f"You have {num_tries-count} guesses remaining!")
            count +=1
            user_guess = int(input("Enter your guess: "))
        if user_guess > randomly_generated_number:
            print("You guessed too high! Please try again!")
            print(f"You have {num_tries-count} guesses remaining!")
            count +=1
            user_guess = int(input("Enter your guess: "))
        if user_guess == randomly_generated_number:
            print("You guessed the correct number! You win!")
            break
