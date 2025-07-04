import random

def play_game():
    print("\nWelcome to the Mystic Number Guessing Game!")
    print("I'm thinking of a number between 1 and 50.")
    print("You have 5 tries to guess it. Good luck!\n")

    number = random.randint(1, 50)
    tries = 5
    score = 0

    while tries > 0:
        guess = input(f"Guess a number (Tries left: {tries}): ")

        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)

        if guess == number:
            score = tries * 20
            print("\n🎉 Wow! You guessed it! You’re a true mystic!")
            print_ascii_art()
            print(f"Your score for this round: {score}\n")
            break
        elif guess < number:
            print("Too low... The number is higher.")
        else:
            print("Too high... The number is lower.")

        tries -= 1

    if tries == 0:
        print(f"\nGame over! The number was {number}. Better luck next time!\n")

    return score

def print_ascii_art():
    print(r"""
      __     __          __          ___       _ 
      \ \   / /          \ \        / (_)     | |
       \ \_/ /__  _   _   \ \  /\  / / _ _ __ | |
        \   / _ \| | | |   \ \/  \/ / | | '_ \| |
         | | (_) | |_| |    \  /\  /  | | | | |_|
         |_|\___/ \__,_|     \/  \/   |_|_| |_(_)
    """)

def main():
    total_score = 0
    while True:
        round_score = play_game()
        total_score += round_score
        print(f"Your total score so far: {total_score}")
        replay = input("Do you want to play again? (y/n): ").lower()
        if replay != 'y':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
