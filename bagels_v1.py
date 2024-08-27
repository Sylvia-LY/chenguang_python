import random
import os
import time

# generates a 3-digit number with unique digits
def generate_secret_number():
    secret_number = random.sample(range(10), k=3)
    return ''.join(str(digit) for digit in secret_number)


def get_clues(guess, secret_number):
    if guess == secret_number:
        return 'You got it'
    
    clues = []
    for i, j in zip(guess, secret_number):
        if i==j:
            clues.append('Fermi')
        elif i in secret_number:
            clues.append('Pico')
    if len(clues)==0:
        return 'Bagels'

    clues.sort()
    return ' '.join(clues)

def is_valid_guess(guess):
    return len(guess) == 3 \
        and len(set(guess)) == len(guess) \
        and guess.isdigit()


# clear the console screen
def clear_screen():
    # Windows
    if os.name=='nt':
        os.system('cls')
    else:
        os.system('clear')


def main():
    clear_screen()
    # intro - explain the rules of the game
    print("I'm thinking of a 3-digit number, try to guess what it is")
    print("Here are some clues: ")
    print("Fermi - 1 digit is correct and in the right position")
    print("Pico - 1 digit is correct but in the wrong position")
    print("Bagels - none of them is correct")

    while 1:
        # timer - record how long it takes for the player to make the correct guess
        start_time = time.perf_counter()
        secret_number = generate_secret_number()
        attempts = 10

        while attempts>0:
            guess = input('Enter your guess: ')

            # validate player's input
            if not is_valid_guess(guess):
                print('Invalid input, please enter a 3-digit number with unique digits')
                continue
            
            # 若猜测合法 给予相应提示
            clues = get_clues(guess, secret_number)
            print(clues)
            attempts-=1

            if guess == secret_number:
                end_time = time.perf_counter()
                elapsed_time = end_time - start_time
                print(f"You took {elapsed_time:.2f} seconds to guess the number")
                break
            else:
                print(f"You have {attempts} attempts left")
        
        if attempts==0:
            print(f"You've run out of attempts, the number was {secret_number}")

        play_again = input("Do you want to play again? (yes or no): ")
        if not play_again.lower().startswith('y'):
            break


if __name__ == "__main__":
    main()