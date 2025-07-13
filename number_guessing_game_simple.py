import random

def play_game():
    print("\nWelcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 20.")
    print("You have 3 tries to guess it.\n")

    number = random.randint(1, 20)
    tries = 3
    score = 0

    while tries > 0:
        guess = input(f"Guess a number (Tries left: {tries}): ")

        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)

        if guess == number:
            score = tries * 20
            print("\nYou guessed it! Great job!")
            print(f"Your score for this round: {score}\n")
            break
        elif guess < number:
            print("Too low. Try higher.")
        else:
            print("Too high. Try lower.")

        tries -= 1

    if tries == 0:
        print(f"\nGame over! The number was {number}.\n")

    return score

def main():
    total_score = 0
    while True:
        total_score += play_game()
        print(f"Total score: {total_score}")
        replay = input("Play again? (y/n): ").lower()
        if replay != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
