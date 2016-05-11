import os
import sys
import shutil

#Add the 3 initializeation scripts and the preset  gulp here. After
#that it would be desirable to have the ability to modularize gulp functions
#And append them to a file to use.


#Stolen from stack overflow, google it
def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)

print("Gulp file auto generation Script | Copyright Austin Fell 2016")

scriptFolder = os.path.dirname(os.path.realpath(sys.argv[0]))
currentDirectory = os.getcwd()
subDirectories = []
currentInput = 'Z'

while (currentInput != 'E' and currentInput != 'e'):
    print("V to view loaded gulp files, A to generate templates into current directory, E to exit.")
    currentInput = input()
    if (currentInput == "V" or currentInput == "v"):
        print("Displaying all template folders inside " + scriptFolder + "/templates")
        subFiles = os.listdir(scriptFolder + "/gulp-files")
        for i in subFiles:
            print(i)
            if os.path.isdir(i):
                subDirectories.append(i)
                print("Found" + i)
    elif (currentInput == "A" or currentInput == "a"):
        print("Please enter gulp-file name (If you do not know, the V command can help you with this)")
        inputFolder = input()
        copytree(scriptFolder + "/" + "gulp-files" + "/" + inputFolder, os.getcwd());
        exit(0);
