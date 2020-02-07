import sys
import os
import shutil

try:
    fileName = sys.argv[1]
    fileName = fileName[:-4]
except IndexError:
    print("Arguments not supplied")

with open(fileName + ".pyb", "r") as pybFile, open(fileName + ".py", "w") as outputFile:
    pybContent = pybFile.readlines()

    for line in pybContent:
        canWriteLine = True
        try:
            if line.strip() == "}":
                canWriteLine = False
            elif line.strip().endswith(" {"):
                line = line[:-3]
                line = line + ":\n"

            if canWriteLine:
                outputFile.write(line)
        except IndexError:
            pass
    
    os.system("echo Successfully Converted")