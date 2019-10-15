message = 'Welcome to the number guessing game. Pick a number between 1 and 10.'
print(message)
Userguess = input() 
Userguess = int(Userguess)
import random
import sys
ComputerGuess = random.randint(1,10)
if Userguess == ComputerGuess:
    print('Congratulations! You picked the right number. This is the end!')
    sys.exit()
elif Userguess != ComputerGuess:
    print('Oh no! You picked the wrong number. Try again.')

print('Guess a number between 1 and 10')
import random
Userguess2 = input()
Userguess2 = int(Userguess2)
ComputerGuess2 = random.randint(1,10)
if Userguess2 == ComputerGuess2:
    print('Congratulations! You picked the right number. This is the end!')
    sys.exit()
elif Userguess2 != ComputerGuess2:
    print('Oh no! You picked the wrong number. Try again.')
