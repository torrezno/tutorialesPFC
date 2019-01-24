def print_max(a,b):
	if a > b:
		print('{} is maximum'.format(a))
	elif a == b:
		print('{} is equal to {}'.format(a,b))
	else:
		print('{} is maximum'.format(b))

print_max(3,4)

x = 5
y = 7

print_max(x,y)