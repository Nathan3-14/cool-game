from random import randint as random

number = random(1, 10)
while True:
    print('Guess my number!')
    player_number = int(input(' '))
    if player_number < number: print('Guess Higher!')
    if player_number > number: print('Guess Lower!')
    if player_number == number:
        print('Well Done! You guessed it')
        break