x = 50

def func():
	global x
	print('x is {}'.format(x))
	x = 2
	print('Changed global x to {}'.format(x))
	
func()
print('Value of x is {}'.format(x))