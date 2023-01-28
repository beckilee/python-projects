# Becki's Wordle clone! Inspired by:
# https://www.nytimes.com/games/wordle/index.html

import random
from colorama import init, Fore, Back

# Initialize colorama
init(autoreset=True)

# Randomly select an answer from the word list file, words.txt
def select_answer():
    random_number = random.randint(1, 15)
    # Handle error if file doesn't exist
    try:
        r = open("words.txt", "r")
        lines = r.readlines()

        word = lines[random_number].strip()
        r.close()
        return word
    except FileNotFoundError:
        print("Sorry, I can't find the words.txt file. Are you inside the wordle directory?")
        exit()

# Associate each letter in the answer with its position
class AnswerLetterClass:
    def __init__(self, letter, position):
        self.letter = letter
        self.position = position

# Associate each letter with its position and color (green, yellow, blank)
class GuessedLetterClass:
    def __init__(self, letter, position, color):
        self.letter = letter
        self.position = position
        self.color = color
    
    def print_guessed_letter(self):
        print(self.letter, self.position, self.color)

# Request input from user; handle scenarios where the user doesn't input
# exactly 5 characters
def get_entry(i):
    while True:
        entry = input("Enter guess " + str(i) + ": ")
        if entry.lower() == "i give up":
            give_up(word)
        if len(entry) != 5:
            print("Sorry, guess must be 5 letters.")
            continue
        else:
            break

    return entry.lower()

# Convert answer to AnswerLetterClass to track each letter's position
def convert_word_to_class(word):
    for i in range(0, 5):
        correct_letters = AnswerLetterClass(word[i], i)
        answer_list.append(correct_letters)
    return answer_list

# Check whether the user's guess is correct
def check_guess(guess, answer_list):
    guess_list = list()
    green_letters = list()
    yellow_letters = list()
    
    # Convert guess to GuessedLetterClass to track each letter's position and
    # color; add each guessed letter to used_letters_set
    for i in range(0, 5):
        guessed_letters = GuessedLetterClass(guess[i], i, "blank")
        guess_list.append(guessed_letters)
        used_letters_set.add(guess[i])

    # If a guessed letter is in the correct spot, set its color to green
    for i in range(0, 5):
        if guess_list[i].letter == answer_list[i].letter:
            guess_list[i].color = "green"
            green_letters.append(guess_list[i].letter)

    # If a guessed letter is in the word, but is not in the correct space, set
    # its color to yellow. Handle scenarios where there are multiple letters in
    # the same word
    for i in range(0, 5):
        for j in range(0, 5):

            if guess_list[i].letter == answer_list[j].letter and guess_list[i].position != answer_list[j].position and guess_list[i].color != "green" and word.count(guess_list[i].letter) != green_letters.count(guess_list[i].letter) and word.count(guess_list[i].letter) != yellow_letters.count(guess_list[i].letter):
                guess_list[i].color = "yellow"
                yellow_letters.append(guess_list[i].letter)

    print("Used letters: " + str(sorted(used_letters_set)) + "\n")

    return used_letters_set, guess_list

# Print each letter of the user's guess in green if it's a correct letter in
# the correct place, or yellow if it's a correct letter in the incorrect place
def print_guess(guess_list):
    for item in guess_list:
        if item.color == "green":
            print(Back.GREEN + Fore.BLACK + item.letter, end="")
        elif item.color == "yellow":
            print(Back.YELLOW + Fore.BLACK + item.letter, end="")
        else:
            print(item.letter, end="")
    print("\n")

def give_up(word):
    print("The answer was " + Back.GREEN + Fore.BLACK + word, end="")
    print(". Better luck next time!")
    exit()

# Initialize variables
guess_list = list()
answer_list = list()
used_letters_set = set()
i = 0
entry = ""

# Select answer from word list
word = select_answer()

# Convert answer to AnswerLetterClass
answer_list = convert_word_to_class(word)

# Print introductory message and directions
print("==========BECKI'S WORDLE CLONE==========")
print("Guess the 5-letter word!")
print(Back.GREEN + Fore.BLACK + "Green", end="")
print(" letters are in the correct place.")
print(Back.YELLOW + Fore.BLACK + "Yellow", end="")
print(" letters are in the wrong place.\nIf there's no color, the letter isn't in the word.\n")
print("Keep guessing until you get the answer. To end the game early, enter: I GIVE UP")
print("Good luck!\n")

# Loop until user guesses the answer or gives up: get guess from user, check
# guess, print guess
while entry != word:
    i += 1
    entry = get_entry(i)
    used_letters_s, guess_l = check_guess(entry, answer_list)
    print_guess(guess_l)

# If the user guesses the answer, print success message
if entry == word:
    if i == 1:
        print("Wait, are you psychic? It only took 1 guess!")
    else:
        print("🎉YOU DID IT!🎉 It only took " + str(i) + " guesses!")