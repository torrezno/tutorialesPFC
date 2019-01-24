import numpy as np

area = np.array([[2,2,2,2,2],[1,1,1,2,2],[2,2,2,2,10],[2,1,1,3,1],[2,1,1,3,1]],dtype=np.uint8)
print area.shape
x,y = area.shape
maskSize = 2
M = np.ones((maskSize,maskSize))

#Size will be  the size of the area - the size of the mask -1
aux = np.zeros((x-maskSize+1,y-maskSize+1))

for i in range(x-maskSize+1):
	for j in range(y-maskSize+1):
		aux[i,j]=np.sum(area[i:i+maskSize,j:j+maskSize]*M)/(maskSize*maskSize)
		
print area
print aux
		