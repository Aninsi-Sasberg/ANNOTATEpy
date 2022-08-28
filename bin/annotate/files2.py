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
import terminal as term


class File:

    openedFileList = []

    def __init__(self, filename, path, filetype):
        self.filename = filename
        self.path = path
        self.filetype = filetype
        self.fullFilename = self.filename + self.filetype
        self.fullName = os.path.join(self.path, self.filename + self.filetype)
        self.checkPath()
        self.openFile()
        # # TODO always get Error: not readable
        self.getContentInfo()
        self.openedFileList.append(self)
        # self.saveToFile()


    def checkFile(self):
        if os.path.exists(self.fullName) == True:
            print("file exists")
            self.openMode = "r+"
        else:
            s = os.makedirs(self.fullName)
            print("file %s will be created"%s)
            self.openMode = "w+"
        return self.openMode

    # open/create File with self.filemode
    def openFile(self):
        self.checkFile()
        with open(self.fullName, self.openMode, encoding="utf-8") as self.file:
            self.fileContentLines = self.file.readlines()
            # TODO why doesn't self.file.read() work?
            # self.fileContentString = self.file.read()
            self.fileContentString = "".join(self.fileContentLines)


    # TODO saveToFile
    def saveToFile(self, currentTextContent):
        self.checkFile()
        with open(self.fullName, "w", encoding="utf-8") as self.file:
            self.file.write(currentTextContent)

    # check if path exists and if not create it
    def checkPath(self):
        try:
            if os.path.exists(self.path) == True:
                print("path exists")
            else:
                s = os.makedirs(self.path)
                print("path %s has been created"%s)
        except:
            print("Could not create path.")
        
        '''make except clearer'''

    # TODO saveToFile method
    # def saveToFile(self, input):
    #     # input = self.file.append() ???
    #     return input

    # TODO think about Fileattributes to be getgot

    def getFilename(self):
        print("Your files name is: " + self.filename + self.filetype)
        return self.filename + self.filetype

    # getLastmodified
    def getPath(self):
        print("Your files path is: " + self.path)
        return self.path

    # getLength

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

    # TODO proper file closing

einsa = File("eyo", ".\\nee\\eyo", ".txt")
