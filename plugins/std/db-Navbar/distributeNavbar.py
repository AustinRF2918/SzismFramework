#Only works with HTML for now. We have to add lines of code to CSS so the "compiler" (Very, very
#liberal use of that term here) knows what to add to respective CSS documents.

import os

scriptDirectory = os.getcwd()
homePath = os.path.expanduser("~")

print("Checking local constructed database (webAssets.config) - !Make sure you created your boilerplate with the autogenerate script!")

print("Opening database...")
with open('webAssets.config', 'r') as webAssets:
    paths = webAssets.readlines() #keep in mind, odd is HTML, even is associated CSS.
                                    #We may need to update javascript as well. That will be done by linking
                                    #A seperate linkJavascript thing to this.

for i in range(len(paths)):
    print("Stripping newline character.")
    paths[i] = paths[i][0:-1]
    print(paths[i])

print("Printing out lines of document:")
print(paths)

'''
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
    curr.write("        <title>" + str(i)+"</title>")
    curr.write("\n")
    curr.write("        <link rel = \"stylesheet\" href = \"../CSS/" + str(i) + "Styles.css\" type = \"text/css\">") #cooresponding link data
    curr.write("\n")
    curr.write("        <link rel = \"stylesheet\" href = \"../CSS/" + str(i) + "Styles.css\" type = \"text/css\">") #cooresponding link data
    curr.write("\n")
    curr.write("        <link rel = \"stylesheet\" href = \"https://maxcdn.bootstrapcdn.com/font-awesome/4.5.0/css/font-awesome.min.css\" type = \"text/css\">") #cooresponding link data
    curr.write("\n")
    curr.write("        <link rel = \"stylesheet\" href = \"../CSS/dummyOne.css\" type = \"text/css\">") #dummy for auto refresh on CSS, avoids caching.
    #curr.write("\n")
    #curr.write("\n")
    #curr.write("        <>") #jquery
    #curr.write("\n")
    #curr.write("        <>") #fonts
    curr.write("\n")
    curr.write("    </head>")
    curr.write("\n")
    curr.write("    <body>")
    curr.write("\n")
    curr.write("\n")
    curr.write("    </body>")
    curr.write("\n")
    curr.write("</html>")
os.chdir('../CSS')
for i in HTMLDocNames:
    open(str(i) + "Styles.css", "w")

os.chdir(homePath)
copyfile(globalBootstrapPath, os.path.join(scriptDirectory, "CSS", "Bootstrap", "bootstrap.css"))
'''
