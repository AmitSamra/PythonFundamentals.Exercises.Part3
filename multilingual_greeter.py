def language():
	global lang
	lang = input('Please select a language: English, German, Spanish ')

language()

def greet(name):
	'''
	name is a string.
	Prints a greeting with name.
	'''
	if lang.lower() == 'english':
		print('Hello ' + name)
	elif lang.lower() == 'german':
		print('Guten Tag ' + name)
	elif lang.lower() == 'spanish':
		print('Buenos Dias ' + name)

def name_input():
	'''
	choice is a user input.
	Prints a greeting with user's input.
	'''
	if lang.lower() == 'english':
		choice = input('Please enter your name: ')
		greet(choice)
	elif lang.lower() == 'german':
		choice = input('Gib deinen Namen ein: ')
		greet(choice)
	elif lang.lower() == 'spanish':
		choice = input('Introduzca su nombre: ')
		greet(choice)

name_input()