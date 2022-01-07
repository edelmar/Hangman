import random
from hangman_words import word_list # List of 5,482 words. 4 to 7 letters long


def display(i):
    p,sl,bsl,sp,u = list('|/\ _')  # pipe, slash, back slash, space, underscore
    h = [sp, 'O', 'O', 'O', 'O', 'O', 'O'] # head
    arms = [sp, sp, sp+p, sl+p, sl+p+bsl, sl+p+bsl, sl+p+bsl]
    legs = [sp,sp,sp, sp, sp, sl, sl+sp+bsl]
    pics = [sp*3+u*5, sp*2+p+sp*4+p, f'{sp*2+p+sp*4}{h[i]}', f'{sp*2+p+sp*3}{arms[i]}', f'{sp*2+p+sp*3}{legs[i]}', u*2+p+u*6]
    print(*pics, sep='\n', flush=True)



def make_guess():
    global counter, progress, i
    #clearConsole()
    guess = input('Make a guess: ')

    print('', flush=True)

    if guess in word:
        good_guesses.append(guess)
        display(counter)
    else:
        bad_guesses.append(guess)
        counter += 1
        display(counter)

    progress = ' '.join(letter if letter in good_guesses else '_' for letter in word)
    print('\n\n', progress, end = '\t')
    print(*bad_guesses)



word = random.choice(word_list)
good_guesses = []
bad_guesses = ['Bad Guesses:']
progress = '_'
counter = 0


if __name__ == '__main__':
    display(0)
    while counter < 6:
        if '_' not in progress:
            break
        make_guess()

    print('\n', word)
