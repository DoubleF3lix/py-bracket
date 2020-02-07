import sys
import subprocess
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
    
print("Successfully Converted")
print("Running file...\n")
print("Output:")
cmdInstance = subprocess.Popen(f'py "{fileName}.py"', stdout=subprocess.PIPE)
output, errors = cmdInstance.communicate()
print(output.decode())
os.remove(f"{fileName}.py")
