import os

def checkFile(fullName):
    if os.path.exists(fullName) == True:
        pass
    elif os.path.exists(os.path.dirname(fullName)):
        with open(fullName, "x", encoding="utf-8") as file:
            pass
    else:
        s = os.makedirs(os.path.dirname(fullName))
        with open(fullName, "x", encoding="utf-8") as file:
            pass

# open/create File with self.filemode
def openFile(fullName):
    checkFile(fullName)
    with open(fullName, "r+", encoding="utf-8") as file:
        fileContentLines = file.readlines()
        fileContentString = "".join(fileContentLines)
    return fileContentString


# TODO saveToFile
def saveToFile(fullName, currentTextContent):
    checkFile(fullName)
    with open(fullName, "w", encoding="utf-8") as file:
        file.write(currentTextContent)