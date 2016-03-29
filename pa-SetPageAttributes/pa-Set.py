import os
import sys
import fnmatch
#Check for existence of "pageProperties.config"
    #Number of Pages (Int)
    #Single Page (Bool)
        #Navbar Type (Must be parsed.)
        #Number Sections
    #Color Scheme Primary Color 1 (Color)
    #Color Scheme Primary Color 2 (Color)
    #Color Scheme Secondary Color 1 (Color)
    #Color Scheme Secondary Color 2 (Color)
    #Color Scheme Extra Color 1 (Color)
    #jsFadeIn (Bool)
    #jsScrollableNavbar (Bool)
    #jsLightableNavbar (Bool)
    #jsDissapearMobileButton (Bool)

getDocumentsGood = False
makeLocalVariables = False

print("paSetPageAttributes Script | Copyright Austin Fell 2016")
homeFolder = os.getcwd()
scriptFolder = os.path.dirname(os.path.realpath(sys.argv[0]))

print("Current directory is: " + homeFolder)
print("If this is wrong, please check your directory and if it was installed correctly.")
print('\n')

cssResults = []
for root, dirs, files in os.walk(homeFolder):
    for _file in files:
        if fnmatch.fnmatch(_file, '*.css'):
            cssResults.append(os.path.join(root, _file))
print("The following CSS documents were discovered.")
print(cssResults)
print('\n')

HTMLResults = []
for root, dirs, files in os.walk(homeFolder):
    for _file in files:
        if fnmatch.fnmatch(_file, '*.html'):
            HTMLResults.append(os.path.join(root, _file))
print("The following HTML documents were discovered.")
print(HTMLResults)
print('\n')

JSResults = []
for root, dirs, files in os.walk(homeFolder):
    for _file in files:
        if fnmatch.fnmatch(_file, '*.js'):
            JSResults.append(os.path.join(root, _file))
print("The following Javascript documents were discovered.")
print(JSResults)
print('\n')

print ("Checking for existence of paths.config inside of SWDL directory.")
if (os.path.isfile(os.path.join(scriptFolder, 'paths.config'))):
    print("File already exists.")
else:
    print("File does not exist. Initializing data.")
    pathsData = open('paths.config', 'w')
    pathsData.write("css.parseFiles")
    pathsData.write("\n")
    for i in cssResults:
        pathsData.write("   " + i)
        pathsData.write("\n")
    pathsData.write("css.parseEnd")
    pathsData.write("\n")
    pathsData.write("html.parseFiles")
    pathsData.write("\n")
    for i in HTMLResults:
        pathsData.write("   " + i)
        pathsData.write("\n")
    pathsData.write("html.parseEnd")
    pathsData.write("\n")
    pathsData.write("js.parseFiles")
    pathsData.write("\n")
    for i in JSResults:
        pathsData.write("   " + i)
        pathsData.write("\n")
    pathsData.write("js.parseEnd")
    pathsData.write("\n")
    getDocumentsGood = True

if getDocumentsGood is True:
    if (os.path.isfile(os.path.join(scriptFolder, 'swdlData.szi'))):
        print("File already exists.")
    else:
        pathsData = open('project.config', 'w')
        pathsData.write("color PRIMARY_BG_COLOR_1 : UNDEFINED")
        pathsData.write("\n")
        pathsData.write("color PRIMARY_BG_COLOR_2 : UNDEFINED")
        pathsData.write("\n")
        pathsData.write("color PRIMARY_FG_COLOR_1 : UNDEFINED")
        pathsData.write("\n")
        pathsData.write("color PRIMARY_FG_COLOR_2 : UNDEFINED")
        pathsData.write("\n")
        pathsData.write("bool pathsInitialized : True")
        pathsData.write("\n")
        pathsData.write("bool colorsInitialized : True")
        pathsData.write("\n")
        pathsData.write("bool swdlDiagnosticsRan : False")
        pathsData.write("\n")

print("Project file successfully written")
