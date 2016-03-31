#This requires significant overhaul to work properly as a SASS object holder.
#A basic idea for myself is to use this to modularly create websites even
#Better than I was before.

import os
import sys
import errno
import shutil

#Stolen from stack overflow, google it
def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)

print("Object Script (Collection)| Copyright Austin Fell 2016 | Templates Copyright Start Bootstrap")

scriptFolder = os.path.dirname(os.path.realpath(sys.argv[0]))
currentDirectory = os.getcwd()
subDirectories = []
currentInput = 'Z'

while (currentInput != 'E' and currentInput != 'e'):
    print("V to view a hierarchy of data, A to place an object into current folder, E to exit.")
    currentInput = input()
    if (currentInput == "V" or currentInput == "v"):
        print("Displaying all template folders inside " + scriptFolder + "/templates")
        subFiles = os.listdir(scriptFolder + "/templates")
        for i in subFiles:
            print(i)
            if os.path.isdir(i):
                subDirectories.append(i)
                print("Found" + i)
    elif (currentInput == "A" or currentInput == "a"):
        print("Please enter uniqid (prefaced with ui) or shorthand (prefaced with sh) (If you do not know, the V command can help you with this)")
        inputFolder = input()
        #modify this
        copytree(scriptFolder + "/" + "templates" + "/" + inputFolder, os.getcwd());
