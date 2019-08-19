import os
import re
import time

VER = '0.7.0'

def take_version(file):
    '''This def take version prom programm'''
    i = 1
    pattern = 'VERSION'
    while i: # Reading line by line
        line = file.readline()
        line = line.rstrip('\n')
        if re.search(pattern, line):   
            exec(line) # Make a VERSION var
            v = v + VERSION
            i = 0 #Stop loop
    return v
NAME = input("Enter programm name: ")
file_name = input("Enter file name: ")
flags = input("Enter flags: ")
prev_version = '0.1.0'
i = 1

while i:
    # time.sleep(30) # Delay
    file = open(file_name, "r") # Open file
    version = take_version(file) # Take version
    file = close() # Close file
    if version != prev_version: # Checking for changes
        try: # Safety device if there is not this dir
            os.rmdir(dist) # Delete dir with prev compile file
        except:
            pass
        new_name = name + version # Making a name
        # Send command to compile to cmd
        eval("os.system('pyinstaller -n' + new_name + flags + file_name)")
        prev_version = version