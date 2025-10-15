import random
score = 0

def game(max_number, max_tries, points):
    number = random.randint(1, max_number)
    print(f"\nThe number is between 1 and {max_number}.")

    for tries_left in range(max_tries, 0, -1):
        guess = int(input(f"Take a guess ({tries_left} tries left), {number}: "))
        

        if guess == number:
            print("Correct! You guessed it!")
            score = tries_left * points
            print(f"Your score: {score}")
            return score
            break     

        elif guess < number:
            if guess < number - 10 or guess > number + 10:
                print("Too low! Try a higher number.")
            elif guess  >= number - 10 or guess <= number + 10:
                print("You're close! Try once more.")

        elif guess > number:
            if guess < number - 10 or guess > number + 10:
                print("Too low! Try a higher number.")
            elif guess  >= number - 10 or guess <= number + 10:
                print("You're close! Try once more.")

        else: 
            ("Invalid input!")
            continue

    else:
        print(f"You are out of tries! The number was {number}.")


print("Welcome to the Number Guess Game!")

while True:
        print("\n||  ``  MENU  ``  ||")
        print("1. Play")
        print("2. Score")
        print("3. Exit")
        ch = input("Enter the index of your choice: ")
        
        if ch == '1':
            print("\nChoose difficulty: Easy | Medium | Hard")
            dif = input("Enter your choice: ").lower()

            if dif == "easy":
                score += game(20, 7, 10)

            elif dif == "medium":
                score += game(50, 5, 20)

            elif dif == "hard":
                score += game(100, 3, 40)

            else:
                print("\nInvalid choice! Please pick a valid difficulty.")
        
        elif ch == '2':
            print(f"Your total score is: {score}")

        elif ch == '3':
            print("Thank you for playing! See you again!")
            break

        else:
            print("Invalid input, Try again!")
