import argparse
from subprocess import call
import sys
import os
import re

print("")
parsePack = re.compile(r'(.*)' + '\.' + 'parsePack')
parsePackEnd = re.compile(r'(.*)' + '\.' + 'parseEnd')
parseScripts = re.compile(r'(.*)' + '\.' + 'parseScripts')
parsePath = re.compile(r'(.*' + r'/' + r'.*)')
parseEntryPoint = re.compile(r'(.*)' + r'\^' + 'entryPoint')

startPointDict = {}
currentEntryPointState = False
currentEntryPointRegister = ""

scopeQueue = []
fileList = []
scriptList = []
entryPointDic = {}
tempPackBuffer = ""

global currentParseState
currentParseState = 0


def checkMultipleArguments(stringData):
    if (len(stringData) == 1):
        return 0
    elif(len(stringData) > 1):
        print("Error: Multiple arguments in file at point: ")
        print(stringData)
        return 1
    elif(len(stringData) == 0):
        return 2

def parseRC(lineList, showData):
    global currentParseState
    global currentEntryPointState
    global entryPointDic
    for i in lineList:
        packData = parsePack.findall(i)
        scriptsData = parseScripts.findall(i)
        endPackData = parsePackEnd.findall(i)
        pathData = parsePath.findall(i)
        entryPointData = parseEntryPoint.findall(i)

        #pack data queue push.
        if (checkMultipleArguments(packData) == 0):
            if (showData):
                print("Pushing: " + packData[0] + " to queue.")
            scopeQueue.append(packData[0])
            tempPackBuffer = packData[0]


        #parse scripts queue push
        if (checkMultipleArguments(scriptsData) == 0):
            if (showData):
                print("Pushing: " + scriptsData[0] + " to queue.")
            scopeQueue.append(scriptsData[0])
            scriptList.append(scriptsData[0].replace(' ', ''))
            currentParseState = 1

      #check if under current state we are scanning files.
        if (currentParseState == 1):
            if(checkMultipleArguments(pathData) == 0):
                if (showData):
                    print("Adding: " + pathData[0] + " to fileList.")
                    fileList.append("plugins" + "/" + tempPackBuffer + "/" + packData[0].replace(' ', ''))
            if currentEntryPointState is True:
                entryPointDic[scriptList[len(scriptList) - 1].replace(' ', '')] = os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), "plugins", tempPackBuffer, pathData[0].replace(' ', ''))
                currentEntryPointState = False

        if (currentParseState == 1):
            if (len(entryPointData) != 0):
                currentEntryPointState = True

        #parse data queue pop
        if (checkMultipleArguments(endPackData) == 0):
            if (endPackData[0] == scopeQueue[len(scopeQueue) - 1]):
                if (showData):
                    print("Found scope end. Popping: " + endPackData[0])
                if (currentParseState == 1):
                    currentParseState = 0
                scopeQueue.pop()
            else:
                print("Error at descoping by: " + endPackData[0])

    if len(scopeQueue) == 0:
        print("RC File parsed successfully.")
    else:
        print("RC File not parsed successfuly. Please check for matching tags..")

    for i in fileList:
        strippedData = i.replace(' ', '')
        if os.path.isfile(strippedData):
            if (showData):
                print(i + " successfully found.")
        else:
            print(i + " could not be found. Please check that scripts directory.")

        if (showData):
            print("FoundPD: " + str(packData) + " " + "FoundSD: " + str(scriptsData))

print("SWDL Framework | Copyright 2016 | Austin Fell")

rcScript = []

rcLocation = "configuration/swdl.rc"
rcLocation = os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), rcLocation)
rcExists = os.path.isfile(rcLocation)

if (not rcExists):
    print("swdl.rc does not exist. Please configure a RC file by creating a putting it in a local configuration file with syntax in documentation.")
    print("Standard library can be found on https://github.com/AustinRF2918/SzismTools.")
    print("with the pathname to swdl.rc. Make it relative.")
else:
    rcScriptUnrefined = open(rcLocation).readlines()
    for i in rcScriptUnrefined:
        rcScript.append(i.rstrip("\n"))

    parseRC(rcScript, False)
cla = argparse.ArgumentParser()
cla.add_argument("-helpMe", "--helpVar", dest = "helpVar", default="Type showScripts to display all loaded scripts.")
cla.add_argument("-showScripts", "--showScripts", action="store_true")
cla.add_argument("-showConfig", "--showConfig", action="store_true")
cla.add_argument("-showInitialization", "--showInitialization", action="store_true")
cla.add_argument("-run", "--run", dest = "runVar", default="Run with scripts shown in the -showScripts argument. You can load custom scripts via the RC file.")
#Adds all scripts to cla possibilities

arguments = cla.parse_args()

if (arguments.showInitialization):
    parseRC(rcScript, True)

print("Type -showScripts in argument list for all underlying modules")

for i in scriptList:
    if (arguments.runVar == i):
        print(entryPointDic)
        print((entryPointDic[arguments.runVar]))
        os.system("python3 " + entryPointDic[arguments.runVar])

print("Make sure ALL SUBDIRECTORIES/SCRIPTS ARE IN DIRECTORY BELOW THIS SCRIPT!")

if (arguments.showScripts):
    print("Available Scripts:")
    for i in scriptList:
        print(i)

if (arguments.helpVar == "agBoilerplate"):
    print("Usage:")
    print("Generates boilerplate code and links CSS, HTML, Images, and JavaScript from a global directory.")
    print("Make sure to run config argument on Szism before using: global paths are neccessary.")

if (arguments.helpVar == "dbNavbar"):
    print("Usage:")
    print("Run on pseudocompiled building blocks. This will link navbar across pages based on page names.")
    print("DO NOT corrupt page names if you are calling this script as they are in a hidden config file")

if (arguments.helpVar == "jsCherryOnTop"):
    print("Usage:")
    print("Generates multiple JS scripts based on snippet code. Must use pseudo compiled code or else")
    print("it may result in errors. All the names of pseudocompiled code made by ag-Boilerplate in")
    print("will be utilized.")

if (arguments.helpVar == "paSetPageAttributes"):
    print("Usage:")
    print("Relatively user friendly way to analyize pseudo-compiled code and make changes and fix errors.")

if (arguments.helpVar == "rc"):
    print ("Usage:")
    print("Easily modify your RC and download addon scripts :).")


