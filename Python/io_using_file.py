from __future__ import print_function
poem = '''\
Programing is fun
When the work is done
if you wanna make your work also fun:
	use Python!
'''

#Open for writing
f = open('poem.txt','w')
#Write to file
f.write(poem)
#Close file
f.close()

f = open('poem.txt')

while True:
	line = f.readline()
	if len(line) == 0:
		break
	
	print(line, end='')
f.close()