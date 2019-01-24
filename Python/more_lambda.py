points = [{'x': 2, 'y':3},
		{'x':4, 'y':1}]
		
def myOrder(i):
	return i['x']
	
#points.sort(key=lambda i: i['y'])
points.sort(key=myOrder)
print(points)