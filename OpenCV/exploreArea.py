#ExploreArea

import numpy as np
import cv2 as cv

def getValue(area, M):
	x,y = M.shape
	return np.sum(area*M)/(x*y)
	
def view(area,pov,pos):
	xc,yc,zc = pos
	x,y,c = pov.shape
	x = x + zc*VERTICALSTEP
	y = y + zc*VERTICALSTEP
	r0 = xc-x/2
	r1 = xc+x/2
	c0 = yc-y/2
	c1 = yc+y/2
	print('View from pos {} is {},{}'.format(pos,(r0,r1),(c0,c1)))
	return area[r0:r1,c0:c1,:] 

def getImage(pos, area):
	global pov
	theView = view(area,pov,pos)
	x,y,color = theView.shape
	xc,yc,zc = pos
	maskSize = zc*VERTICALSTEP+1
	M = np.ones((maskSize,maskSize))
	#TODO Cambiar el bucle por np 
	for i in range(x-maskSize+1):
		for j in range(y-maskSize+1):
			for c in range(color):
				pov[i,j,c]=getValue(theView[i:i+maskSize-1,j:j+maskSize-1,c],M)
				
		
	return pov

def moveCamera(pos, direction):
	global area, pov
	x,y, colors = pov.shape
	print pov.shape
	maxX,maxY, colors2= area.shape
	
	aux = pos[:]
	if direction == 0: #UP
		aux[0]-=STEP
	elif direction == 1: #DOWN
		aux[0]+=STEP
	elif direction == 2: #RIGHT
		aux[1]+=STEP
	elif direction == 3: #LEFT
		aux[1]-=STEP
	elif direction == 4: #UP
		aux[2]+=1
	elif direction == 5: #DOWN
		aux[2]-=1
	
	print('Trying to move from {} to {}'.format(pos,aux))
	print('The pov will be {}'.format([(aux[1]-x/2,aux[0]-y/2),(aux[1]+x/2,aux[0]+y/2)]))
	if aux[1]-x/2 < 0 or aux[1]+x/2 > maxX or aux[0]-y/2 < 0 or aux[0]+y/2 > maxY or aux[2] < 0 or aux[2]>10:
		print 'Camera didnt move'
		return pos
	else:
		print 'Legal move'
		return aux

def moveCameraUp(pos):
	return moveCamera(pos,0)
	
def moveCameraDown(pos):
	return moveCamera(pos,1)

def moveCameraRight(pos):
	return moveCamera(pos,2)
	
def moveCameraLeft(pos):
	return moveCamera(pos,3)
def moveCameraZoomOut(pos):
	return moveCamera(pos,4)
def moveCameraZoomIn(pos):
	return moveCamera(pos,5)
		

BACKGROUND_COLOR = (0,0,0)
UP = 119 # W
DOWN = 115 # S
RIGHT = 100 # D
LEFT = 97 # A
ZOOMOUT = 111 # O
ZOOMIN = 108 # L
STEP = 16
VERTICALSTEP = 4

#Area of work
area = np.zeros((1024,1024,3),dtype=np.uint8) 
area[:,:] = BACKGROUND_COLOR
area[:,1020:1023] = (255,255,255)
area[:,0:3] = (255,255,255)
area[1020:1023,:] = (255,255,255)
area[0:3:,:] = (255,255,255)

#Objects in area
objectsCenters = [(128,128),(512,400), (512,800)]
cv.circle(area,objectsCenters[0],40,(255,0,0),-1)
cv.circle(area,objectsCenters[1],40,(0,255,0),-1)
cv.circle(area,objectsCenters[2],40,(0,0,255),-1)

#Camera
pov = np.zeros((256,256,3),dtype=np.uint8) # Camera view
x,y, colors = pov.shape
cameraPos = [x/2,y/2,0]
cv.namedWindow('pov')
cv.namedWindow('area')



while(True):
	pov = getImage(cameraPos,area)
	cv.imshow('pov',pov)
	cv.imshow('area',area)
	k = cv.waitKey(5) & 0xFF
	if k == 27:
		break
	elif k == 255:
		pass
	elif k == UP:
		cameraPos = moveCameraUp(cameraPos)
	elif k == DOWN:
		cameraPos = moveCameraDown(cameraPos)
	elif k == RIGHT:
		cameraPos = moveCameraRight(cameraPos)
	elif k == LEFT:
		cameraPos = moveCameraLeft(cameraPos)
	elif k == ZOOMOUT:
		cameraPos = moveCameraZoomOut(cameraPos)
	elif k == ZOOMIN:
		cameraPos = moveCameraZoomIn(cameraPos)
	else:
		print k
	
		
cv.destroyAllWindows()
	






