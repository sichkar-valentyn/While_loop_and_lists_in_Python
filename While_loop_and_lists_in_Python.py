# File: While_loop_and_lists_in_Python.py
# Description: Working with while loop and lists in Python
# Environment: Spyder IDE in Anaconda environment
#
# MIT License
# Copyright (c) 2018 Valentyn N Sichkar
# github.com/sichkar-valentyn
#
# Reference to:
# [1] Valentyn N Sichkar. Working with while loop and lists in Python // GitHub platform [Electronic resource]. URL: https://github.com/sichkar-valentyn/While_loop_and_lists_in_Python (date of access: XX.XX.XXXX)

"""
Created on Mon Jan 08 14:52:15 2018

@author: Valentyn
"""
import os
import psutil
import shutil
import sys

print("This is a Great Python Program!")
print("Hello there, programmer!")

name = input("What is your name? ")
print(name, ", Welcome!")

answer = ''

while answer != 'Q':   
    answer = input("Let's work? (Y/N/Q)")    
    if answer == 'Y':
        print("Great choice!") # type "pass" for the empty construction
        print("I can do for you:")
        print("[1] - show list of files and folders in current directory")
        print("[2] - show information about System")
        print("[3] - show list of running tasks in the System")
        print("[4] - duplication of all files in the current directory")
        print("[5] - change the current directory")
        print("[6] - duplication of specific file in the current directory")
        print("[7] - deleting all files with ending '.duplication'")
        todo = int(input("Make your choice: "))    
        if todo == 1:
            print(os.listdir())
        elif todo == 2:
            print("Current directory: ", os.getcwd())
            print("Number of CPU: ", os.cpu_count())
            print("Operation System: ", sys.platform)
            print("File system encoding: ", sys.getfilesystemencoding())
        elif todo == 3:
            print("List of current running PIDs: ", psutil.pids())
        elif todo == 4:
            print("All files in the current directory are duplicated now!")
            file_list = os.listdir()
            i = 0
            while i < len(file_list):
                if os.path.isfile(file_list[i]): # Checking if the file_name[i] is a file and isn't folder
                    new_file = file_list[i] + '.duplication'
                    shutil.copy(file_list[i], new_file)
                else:
                    pass
                i += 1
        elif todo == 5:
            print("Type the name of the derictory you want to change in.")
            current_directory = input("Input name of the directory: ")
            os.chdir(current_directory)
            file_list = os.listdir()
            print("List of files in chosen directory:")
            for file_name in file_list:
                print(file_name)
        elif todo == 6:
            print("Type the name of the file you want to duplicate")
            file_to_duplicate = input("Input name of the file: ")
            new_file = file_to_duplicate + '.duplication'
            if os.path.isfile(file_to_duplicate):
                shutil.copy(file_to_duplicate, new_file)
                print("File was successfully duplicated!")
            else:
                pass
        elif todo == 7:
            print("All duplicated files are deleted now!")
            file_list = os.listdir()
            i = 0
            while i < len(file_list):
                if file_list[i].endswith('.duplication'): # Checking if the file has the ending 'duplication'
                    os.remove(file_list[i])
                else:
                    pass
                i += 1
        else: pass # for the empty construction        
    elif answer == 'N':
        print("Good by, see you next time!")
    else:
        print("Unknown input, try again")
