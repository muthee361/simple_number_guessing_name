import random

initial_trials = 1
max_trials = 3
score = 0
# to do: implement a function that allows a user to play again.
while initial_trials <= max_trials:
    secret_number = random.randint(0, 5)
    guess_number = int(input('Enter a guess number between 0 - 5: '))
#    keep a count of the remaining trials
    attempts = max_trials - initial_trials

    if guess_number == secret_number:
         print(f'Bingo! That was correct. You have {attempts} attempts remaining.')
         initial_trials += 1
         score +=1
         continue
    else:
         print(f'Wrong guess! You have {attempts} attempts remaining.')
         print(f'The answer is: {secret_number}')
         initial_trials += 1
         continue
print(f'Game over!! \nYou scored: {score}/{max_trials}')
