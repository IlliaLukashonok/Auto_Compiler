import os
import re
import time

VER = '0.7.0'

def vr(line):
    version = line.split("'")
    return version[1]

def take_version(file):
    '''This def take version from programm'''
    i = 1
    pattern = 'VERSION'
    while i: # Reading line by line
        line = file.readline()
        line = line.rstrip('\n')
        if re.search(pattern, line):   
            version = vr(line)
            i = 0 #Stop loop
    return version
NAME = input("Enter programm name: ")
file_name = input("Enter file name: ")
flags = input("Enter flags: ")
prev_version = '0.1.0'
i = 1

while i:
    time.sleep(60) # Delay
    while i:
        try: # Safety device if we can't use a file
            file = open(file_name, "r") # Open file
        except:
            time.sleep(30)
        else:
            i = 0
    version = take_version(file) # Take version
    file.close() # Close file
    if version != prev_version: # Checking for changes
        try: # Safety device if there is not this dir
            os.rmdir(dist) # Delete dir with prev compile file
        except:
            pass
        new_name = NAME + version # Making a name
        # Send command to compile to cmd
        eval("os.system('pyinstaller -n' + new_name + flags + ' ' + file_name)")
        prev_version = version