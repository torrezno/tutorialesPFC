try:
	text = raw_input('Enter something-->')
except EOFError:
	print("Why did you do an EOF on me?")
except KeyboardInterrupt:
	print("You canceled the operation")
else:
	print('You entered {}'.format(text))