#Guess the number game
import random

print('Hi, what is your name?')
name = input()

print('Hello there ' + name + ', I am thinking of a number between 1 and 20.')
secnum = random.randint(1, 20)

for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secnum:
        print('Too low! Shoot higher!')
    elif guess > secnum:
        print('Too high! Try again!')
    else:
        break #breaks loop on accurate guess

if guess == secnum:
    print('Congratulations ' + name + '! You took ' + str(guessesTaken) + ' guesses to reach my number!')
else:
    print('Sorry ' + name + ' , you ran out of guesses and the correct answer was ' + str(secnum))
