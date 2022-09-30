import os

# checks for existing file
# if file exists open as read/write (no truncating);; else if file doesn't exist, but directory exists, create file;; else create directory and then create file in directory
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

# opens File after calling checkFile()
def openFile(fullName):
    checkFile(fullName)
    with open(fullName, "r+", encoding="utf-8") as file:
        fileContentLines = file.readlines()
        fileContentString = "".join(fileContentLines)
    return fileContentString


# saves to file after calling checkFile()
def saveToFile(fullName, currentTextContent):
    checkFile(fullName)
    with open(fullName, "w", encoding="utf-8") as file:
        file.write(currentTextContent)