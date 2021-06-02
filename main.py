from gameplay import word_to_guess, guess_word, hint

def game_intro():
    print("Hangman is a paper and pencil guessing game for two or more players.\nOne player thinks of a word, phrase or sentence and the other tries to guess it by suggesting letters within a certain number of guesses.")

def welcome_player(name):
    print("Welcome to the game " + name)



if __name__ == '__main__':
    game_intro()
    player = input("Player  enter your name")
    welcome_player(player)
    word = word_to_guess()
    game_hint = hint(word)
    print(game_hint)
    guess_word(word)







