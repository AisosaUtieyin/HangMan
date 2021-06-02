import random
def word_to_guess():
    list = ['banana','milan','prince','elite']
    mysterious_word = random.randint(0,len(list)-1)
    return list[mysterious_word]

def hint(mystery_word):

    if mystery_word == 'banana':
        return 'it is a famous fruit'
    elif mystery_word == 'milan':
        return 'it is a famous italian city'
    elif mystery_word == 'prince':
        return  'it is a famous black singer'
    elif mystery_word == 'elite':
        return 'it is a famous spanish tv show'

def guess_word(mystery_word):
    attempt = 0
    correct_player_input = False

    for i in mystery_word:
        print('_ ' , end='')
    player_guess(mystery_word)

def player_guess(mystery_word):
    winner_array=[]
    for i in mystery_word:
        winner_array.append(i)

    print(len(winner_array))

    attempt = len(mystery_word)
    index=0
    already_guessed = []
    while index<attempt:

        player_attpempt = input('\nEnter a letter you have '+ str (attempt-index) + ' attempt')
        letter = player_attpempt[0]
        for i in mystery_word:
            if letter == i or i in already_guessed:
                print(i, end='')
                if i not in already_guessed:

                   already_guessed.append(i)
            else:
                print(' _ ', end='')

        if len(already_guessed) == len(winner_array):
            print('You won')
            break



        index+=1











