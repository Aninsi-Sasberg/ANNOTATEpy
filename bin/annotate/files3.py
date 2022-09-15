# filename = just filename without extension
# path = path where file is to be stored, no filename; as UNC path
# mode = opening modes
    # needed modes:
    # r for reading only
    # w for writing on/over the file, creating new one if doesn't exist
    # ↑ (w) standard mode
# filetype = just filetype, without filename
# fullName = path + filename + filetype

# new file opening
# each time file gets loaded, saved, created
# new file opening call

import os

def checkFile(fullName):
    if os.path.exists(fullName) == True:
        print("file exists")
        openMode = "r+"
    elif os.path.exists(os.path.dirname(fullName)):
        with open(fullName, "x", encoding="utf-8") as file:
            pass
        print("file will be created")
        openMode = "r+"
    else:
        s = os.makedirs(fullName)
        print("file ${s} will be created")
        openMode = "w+"
    return openMode

# open/create File with self.filemode
def openFile(fullName):
    openMode = checkFile(fullName)
    with open(fullName, openMode, encoding="utf-8") as file:
        fileContentLines = file.readlines()
        # TODO why doesn't self.file.read() work?
        # self.fileContentString = self.file.read()
        fileContentString = "".join(fileContentLines)
    return fileContentString


# TODO saveToFile
def saveToFile(fullName, currentTextContent):
    checkFile(fullName)
    with open(fullName, "w", encoding="utf-8") as file:
        file.write(currentTextContent)

def getFilename(fullName):
    path, filename = os.path.split(fullName)
    filename, filetype = os.path.splitext(filename)
    # print("Your files name is: " + filename + filetype)
    return str(filename) + str(filetype)

# getLastmodified
def getPath(fullName):
    path, filename = os.path.split(fullName)
    print("Your files path is: " + path)
    return path

    # TODO getContentInfo
    # DONE words
    # DONE whitespace (pseudoWhite (the optimal case of one whitespace between each word); realWhite(counts actual whitespaces in the File); tooManyWhite(whitespaces that are unnecessary in the opinion of the programmer (rules doubled whitespaces or Whitespaces at the end of the line as unnecessary)))
    # DONE characters(wordsPseudoWhite(words + pseudoWhite); wordsWhite(words + realWhite); characters; charactersNoWhite(characters - realWhite))
    # DONE lines
    def getContentInfo(self):
        self.tempFileContentLinesGetWords = []
        self.realWhite = 0
        self.characters = 0
        self.lines = 0
        for line in self.fileContentLines:
            self.realWhite += line.count(" ")
            self.characters += len(line.replace("\n", ""))
            self.lines += 1
            for word in line.replace("\n", "").split():
                self.tempFileContentLinesGetWords.append(word)
        self.words = len(self.tempFileContentLinesGetWords)
        self.wordsPseudoWhite = self.words * 2 - len(self.fileContentLines)
        self.pseudoWhite = self.wordsPseudoWhite - self.words
        self.wordsWhite = self.words + self.wordsPseudoWhite
        self.tooManyWhite = self.realWhite - self.pseudoWhite
        self.charactersNoWhite = self.characters - self.realWhite
        # print(self.words, self.pseudoWhite, self.wordsPseudoWhite, self.realWhite, self.wordsWhite, self.tooManyWhite, self.characters, self.charactersNoWhite, self.lines)

    # TODO Undo/Redo