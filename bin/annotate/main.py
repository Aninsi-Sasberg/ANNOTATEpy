# needed modes:
# r for reading only
# w for writing on/over the file, creating new one if doesn't exist
# ↑ (rw) standard mode


class File:

    openedFileList = []

    def __init__(self, path, mode, filetype):
        self.path = path
        self.mode = mode
        self.filetype = filetype
        self.openedFileList.append(self)

    def openFile(self, file):
        self.file = file = open(self.path, self.mode)
        return file

    def saveToFile(self, input):
        input = self.file.append()

file1 = File(".\ai\ai.txt", "wr", ".txt")
print(file1)