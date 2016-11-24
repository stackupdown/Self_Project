##
###!/usr/bin/python
### Filename: backup_ver1.py
##import os
##import time
##import zipfile
### 1. The files and directories to be backed up are specified in a list.
##source = [r'C:\Users\hugo\Desktop\DK.jsp', r'C:\Users\hugo\Desktop\MAIN.cpp']
### If you are using Windows, use source = [r'C:\Documents', r'D:\Work'] or somethin
### 2. The backup must be stored in a main backup directory
##target_dir = 'C:\\Users\\hugo\\Desktop\\' # Remember to change this to what you will be using
### 3. The files are backed up into a zip file.
### 4. The name of the zip archive is the current date and time
##target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'
### 5. We use the zip command (in Unix/Linux) to put the files in a zip archive
##zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))
##
##print zip_command
### Run the backup


##if os.system(zip_command) == 0:
##    print 'Successful backup to', target
##else:
##    print os.system(zip_command)#'Backup FAILED'
##

import zipfile
import os
import sys
##f=zipfile.ZipFile('archive.zip','w', ZIP_DEFLATED)
##f.write('hello.py')
##f.write(r'C:\Users\hugo\Desktop\DK.jsp')
##f.write('MAIN.CPP', r'C:\Users\hugo\Desktop\MAIN.cpp')
##f.close()
zfile = zipfile.ZipFile('archive.zip', 'r')
k = 0
try:
    for filename in zfile.namelist():
        print k        
        k=k+1
        data = zfile.read(filename)
        file = open(filename+'d', 'w+b')
        file.write(data)
        file.close()
except:
    zipfile.close()
###!/usr/bin/python
### Filename: backup_ver2.py
##import os
##import time
### 1. The files and directories to be backed up are specified in a list.
##source = ['/home/swaroop/byte', '/home/swaroop/bin']
### If you are using Windows, use source = [r'C:\Documents', r'D:\Work'] or somethin
###Problem Solving - Writing a Python Script
###60
##
##
### 2. The backup must be stored in a main backup directory
##target_dir = '/mnt/e/backup/' # Remember to change this to what you will be using
### 3. The files are backed up into a zip file.
### 4. The current day is the name of the subdirectory in the main directory
##today = target_dir + time.strftime('%Y%m%d')
### The current time is the name of the zip archive
##now = time.strftime('%H%M%S')
### Create the subdirectory if it isn't already there
##if not os.path.exists(today):
##os.mkdir(today) # make directory
##print 'Successfully created directory', today
### The name of the zip file
##target = today + os.sep + now + '.zip'
### 5. We use the zip command (in Unix/Linux) to put the files in a zip archive
##zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))
### Run the backup
##if os.system(zip_command) == 0:
##print 'Successful backup to', target
##else:
##print 'Backup FAILED
