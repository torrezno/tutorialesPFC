def total(a=5, *numbers, **phonebook):
	print('a ' +str(a))
	
	for single_item in numbers:
		print('single_item {}'.format(single_item))
	
	for first_part, second_part in phonebook.items():
		print(first_part,second_part)

total(10,1,2,3,Jack=1123, John=2231, Inge=1560)