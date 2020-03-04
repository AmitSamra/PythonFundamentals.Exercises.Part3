# Exercise 2

'''
Create a program called higher_or_lower.py

The program must meet the following criteria.

A function that asks the user to provide a number between 0 and 10.
A function that returns a random number between 1 and 10.
A function that evaluates the randomly generated number against the user's guess.
At the end, the program must output the following:
The random number that was generated.
The user's guess.
An indication if the user guess correctly or if the user's guess was too high/too low.
'''

from random import randrange

def rand_num():
	global num
	num = randrange(0,10)
	print(f'This is the random number: {num}\nPretend like you cannot see it.')
rand_num()

print(' ')

def user_guess():
	global guess
	guess = int(input('Guess a number in [0,10]: '))

def compare():
	for i in range(0, 3):
		user_guess()
		if num < guess:
			print('Too high!')
		elif num > guess:
			print('Too low!')
		else:
			print('You win!')
			break
	print('You lose!')
compare()