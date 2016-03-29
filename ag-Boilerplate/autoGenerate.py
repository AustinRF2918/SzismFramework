import os
from shutil import copyfile
import shutil

#this one just takes the whole damn folder and puts it into our thing: repurposed from
# pythoncentral.io/how-to-recursively-copy-a-directory-folder-in-python/
def recursiveCopy(src, dest, purpose):
    try:
        shutil.copytree(src, dest)
    except shutil.Error as e:
        print('Could not: ' + purpose)
        print(e)
    except OSError as e:
        print('Could not: ' + purpose)
        print('OSError')
        print(e)


scriptDirectory = os.getcwd()
homePath = os.path.expanduser("~")

print("Number of HTML/CSS Documents?")
numDocs = input()
HTMLDocNames = []

for i in range(int(numDocs)):
    print("Name of document " + str(i) + "?")
    HTMLDocNames.append(input())

print("Website name?")
websiteName = input()


CSSPath = "CSS"
HTMLPath = "HTML"
JavaScriptPath = "JS"
ImagePath = "IMG"
BootstrapPath = "CSS/Bootstrap"
RelativeBootstrapPath = "Bootstrap"
JQueryPath = "JS/JQuery"
RelativeJQueryPath = "JQuery"

os.makedirs(CSSPath, exist_ok = True)
os.makedirs(HTMLPath, exist_ok = True)
os.makedirs(JavaScriptPath, exist_ok = True)
os.makedirs(ImagePath, exist_ok = True)

#maybe consolidate these into one file.
with open(os.path.join('configFiles', 'bPath.config'), 'r') as currentBootstrapConfiguration:
    globalBootstrapPath = currentBootstrapConfiguration.read().replace('\n', '')

with open(os.path.join('configFiles', 'jPath.config'), 'r') as currentJavaScriptConfiguration:
    globalJavascriptPaths = currentJavaScriptConfiguration.readlines()


with open(os.path.join('configFiles', 'prototypeImages.config'), 'r') as currentPrototypeImagesConfiguration:
    globalImageData = currentPrototypeImagesConfiguration.read().replace('\n', '')

os.chdir("CSS")
os.makedirs(RelativeBootstrapPath, exist_ok = True)
os.chdir("../JS")
os.makedirs(RelativeJQueryPath, exist_ok = True)

#Make the documents synchronized across CSS and HTML
os.chdir("../HTML")
for i in HTMLDocNames:
    curr = open(str(i) + ".html", "w")
    curr.write("<!DOCTYPE html>")
    curr.write("\n")
    curr.write("<!-- Generated with the SWDL Framework | Created by Austin Fell | Copyright 2016 -->")
    curr.write("\n")
    curr.write("<html>")
    curr.write("\n")
    curr.write("    <head>")
    curr.write("\n")
    curr.write("        <meta charset = \"utf-8\">")
    curr.write("\n")
    curr.write("        <meta name = \"viewport\">")
    curr.write("\n")
    curr.write("        <title>" + websiteName +"</title>")
    curr.write("\n")
    curr.write("        <link rel = \"stylesheet\" href = \"../CSS/" + str(i) + "Styles.css\" type = \"text/css\">") #cooresponding link data
    curr.write("\n")
    curr.write("        <link rel = \"stylesheet\" href = \"../CSS/Bootstrap/" + "bootstrap.css\" type = \"text/css\">") #cooresponding link ata
    curr.write("\n")
    curr.write("        <link rel = \"stylesheet\" href = \"https://maxcdn.bootstrapcdn.com/font-awesome/4.5.0/css/font-awesome.min.css\" type = \"text/css\">") #cooresponding link data
    curr.write("\n")
    curr.write("        <link rel = \"stylesheet\" href = \"https://fonts.googleapis.com/css?family=Montserrat\" type = \"text/css\">") #cooresponding link data
    curr.write("\n")
    #curr.write("\n")
    #curr.write("        <>") #jquery
    #curr.write("\n")
    #curr.write("        <>") #fonts
    curr.write("    </head>")
    curr.write("\n")
    curr.write("    <body>")
    curr.write("\n")
    curr.write('    <script src=../JS/jquery.js></script>')
    curr.write("\n")
    curr.write('    <script src=../JS/main.js></script>')
    curr.write("\n")
    curr.write('    <script src=../JS/jquery.easing.min.js></script>')
    curr.write("\n")
    curr.write('    <script src=../JS/bootstrap.js></script>')
    curr.write("\n")
    curr.write("    </body>")
    curr.write("\n")
    curr.write("</html>")
os.chdir('../CSS')
for i in HTMLDocNames:
    open(str(i) + "Styles.css", "w")

os.chdir(homePath)
copyfile(globalBootstrapPath, os.path.join(scriptDirectory, "CSS", "Bootstrap", "bootstrap.css"))

copyfile(globalJavascriptPaths[0].rstrip("\n"), os.path.join(scriptDirectory, "JS", "jquery.js" ))
copyfile(globalJavascriptPaths[1].rstrip("\n"), os.path.join(scriptDirectory, "JS", "main.js" ))
copyfile(globalJavascriptPaths[2].rstrip("\n"), os.path.join(scriptDirectory, "JS", "jquery.easing.min.js" ))

recursiveCopy(globalImageData, os.path.join(scriptDirectory, "IMG", "Prototype"), "Copying prototype image data.")
