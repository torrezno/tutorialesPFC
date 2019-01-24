from __future__ import print_function
import os
import time

#Source of the list  of files to be backed up

source = [r'D:\Documents\list']

#Target Directory 

target_dir = r'D:\backup'

#Create target dir if not present
if not os.path.exists(target_dir):
	os.mkdir(target_dir)

#Build the name of the backup file and directory tree
today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

#Name of the file
target_name = today + os.sep + now + '.zip'

#Create directory tree if it doesnt exists
if not os.path.exists(today):
	os.mkdir(today)
	print('Successfully created directory', today)
	
#Build the zip command

zip_command = 'zip -r {} {}'.format(target_name,' '.join(source))

#Run

print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command)  == 0:
	print('Successful backup to', target_dir)
else:
	print('Backup FAILED')