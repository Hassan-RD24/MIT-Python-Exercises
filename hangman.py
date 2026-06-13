# Problem Set 2
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    return random.choice(wordlist)


wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    result = ""
    for letter in secret_word:
        if letter in letters_guessed:
            result += letter
        else:
            result += "_ "
    return result


def get_available_letters(letters_guessed):
    result = ""
    for letter in string.ascii_lowercase:
        if letter not in letters_guessed:
            result += letter
    return result


def hangman(secret_word):
    guesses_remaining = 6
    warnings_remaining = 3
    letters_guessed = []
    vowels = 'aeiou'

    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    print("You have", warnings_remaining, "warnings left.")
    print("-------------")

    while guesses_remaining > 0 and not is_word_guessed(secret_word, letters_guessed):
        print("\nYou have", guesses_remaining, "guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))

        guess = input("Please guess a letter: ").lower()

        if not guess.isalpha():
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print("Oops! That is not a valid letter. You have", warnings_remaining, "warnings left:", get_guessed_word(secret_word, letters_guessed))
            else:
                guesses_remaining -= 1
                print("Oops! That is not a valid letter. You have no warnings left so you lose one guess:", get_guessed_word(secret_word, letters_guessed))

        elif guess in letters_guessed:
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print("Oops! You've already guessed that letter. You have", warnings_remaining, "warnings left:", get_guessed_word(secret_word, letters_guessed))
            else:
                guesses_remaining -= 1
                print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:", get_guessed_word(secret_word, letters_guessed))

        else:
            letters_guessed.append(guess)
            if guess in secret_word:
                print("Good guess:", get_guessed_word(secret_word, letters_guessed))
            else:
                if guess in vowels:
                    guesses_remaining -= 2
                else:
                    guesses_remaining -= 1
                print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))

        print("------------")

    if is_word_guessed(secret_word, letters_guessed):
        unique_letters = len(set(secret_word))
        score = guesses_remaining * unique_letters
        print("Congratulations, you won!")
        print("Your total score for this game is:", score)
    else:
        print("Sorry, you ran out of guesses. The word was", secret_word + ".")


def match_with_gaps(my_word, other_word):
    my_word = my_word.replace(" ", "")
    if len(my_word) != len(other_word):
        return False
    guessed_letters = [c for c in my_word if c != '_']
    for i in range(len(my_word)):
        if my_word[i] == '_':
            if other_word[i] in guessed_letters:
                return False
        else:
            if my_word[i] != other_word[i]:
                return False
    return True


def show_possible_matches(my_word):
    matches = [word for word in wordlist if match_with_gaps(my_word, word)]
    if matches:
        print("Possible word matches are:", " ".join(matches))
    else:
        print("No matches found")


def hangman_with_hints(secret_word):
    guesses_remaining = 6
    warnings_remaining = 3
    letters_guessed = []
    vowels = 'aeiou'

    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    print("You have", warnings_remaining, "warnings left.")
    print("-------------")

    while guesses_remaining > 0 and not is_word_guessed(secret_word, letters_guessed):
        print("\nYou have", guesses_remaining, "guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))

        guess = input("Please guess a letter: ").lower()

        if guess == '*':
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))

        elif not guess.isalpha():
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print("Oops! That is not a valid letter. You have", warnings_remaining, "warnings left:", get_guessed_word(secret_word, letters_guessed))
            else:
                guesses_remaining -= 1
                print("Oops! That is not a valid letter. You have no warnings left so you lose one guess:", get_guessed_word(secret_word, letters_guessed))

        elif guess in letters_guessed:
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print("Oops! You've already guessed that letter. You have", warnings_remaining, "warnings left:", get_guessed_word(secret_word, letters_guessed))
            else:
                guesses_remaining -= 1
                print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:", get_guessed_word(secret_word, letters_guessed))

        else:
            letters_guessed.append(guess)
            if guess in secret_word:
                print("Good guess:", get_guessed_word(secret_word, letters_guessed))
            else:
                if guess in vowels:
                    guesses_remaining -= 2
                else:
                    guesses_remaining -= 1
                print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))

        print("------------")

    if is_word_guessed(secret_word, letters_guessed):
        unique_letters = len(set(secret_word))
        score = guesses_remaining * unique_letters
        print("Congratulations, you won!")
        print("Your total score for this game is:", score)
    else:
        print("Sorry, you ran out of guesses. The word was", secret_word + ".")


if __name__ == "__main__":
    secret_word = choose_word(wordlist)
    hangman(secret_word)

    # secret_word = choose_word(wordlist)
    # hangman_with_hints(secret_word)