from __future__ import print_function
import os
import time

#Source of the list  of files to be backed up

source = [r'D:\Documents\list']

#Target Directory 

target_dir = r'D:\backup'

#Build the name of the backup file
target_name = target_dir + os.sep + \
	time.strftime('%Y%m%d%H%M%S') + '.zip'
	

#Create target dir if not present
if not os.path.exists(target_dir):
	os.mkdir(target_dir)
	
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