import files3

import os

from PyQt6 import QtWidgets
# from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWidgets import *
from PyQt6.QtCore import pyqtSlot
from PyQt6.QtGui import QKeySequence
from PyQt6.QtGui import QShortcut

import sys
import re

# def saveFileDialog():
#     try:
#         # TODO: need condition to break if user presses close button on dialog, or else user is stuck in loop even if he doesn't want to save a file anymore
#         path = filedialog.asksaveasfilename(confirmoverwrite=True, defaultextension=".txt")
#         if not path:
#             raise Exception
#         print("You've selected the directory + filename:\n" + path)
#     except:
#         print("You have to choose a directory.")
#     return path

# def guiCreateFile():
#     # select directory
#     path = saveFileDialog()

#     path, filename = os.path.split(path)
#     filename, filetype = os.path.splitext(filename)
#     files3.File(filename, path, filetype)

#     # TODO, is this necessary?
#     guiFileCreated = 1
#     return guiFileCreated

class MainWindow(QMainWindow):
    # def __init__(self, parent = None):
    #     super(MainWindow, self).__init__(parent)
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(200, 200, 400, 400)
        self.setWindowTitle("ANNOTATEpy")
        self.currentTextContent = ""

        self.initUI()
        self.killWhite()

    # https://www.binpress.com/building-text-editor-pyqt-1/
    def initMenubar(self):

        menubar = self.menuBar()

        file = menubar.addMenu("File")
        edit = menubar.addMenu("Edit")
        view = menubar.addMenu("Help")

    # https://www.youtube.com/watch?v=-2uyzAqefyE
    def initUI(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.mainText = QTextEdit(self)
        self.setCentralWidget(self.mainText)
        self.mainText.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        # self.mainText.resize(400,400)
        self.mainText.insertPlainText(self.currentTextContent)
        # self.mainText.textChanged().self.saveToCurrentTextContent()

        self.layout.addWidget(self.mainText)
        self.initMenubar()
        
        # https://stackoverflow.com/a/25994381
        self.shortcut = QShortcut(QKeySequence("Ctrl+S"), self)
        self.shortcut.activated.connect(self.saveToCurrentTextContent)

        # self.shortcut = QShortcut(QKeySequence("Ctrl+N"), self)
        # self.shortcut.activated.connect(self.newWindow)

        self.shortcut = QShortcut(QKeySequence("Ctrl+O"), self)
        self.shortcut.activated.connect(self.openFileDialog)

    # TODO Change Line Wrap Mode

    # https://www.binpress.com/building-text-editor-pyqt-1/
    # def newWindow(self):
        # spawnNewWindow = MainWindow(self) -> well the behavior...
        # spawnNewWindow = MainWindow() -> without parent doesn't work, must have parent, but behavior isn't favorable in that way, because if main Window is closed everything gets shut down
        # spawnNewWindow.show()

    # https://www.binpress.com/building-text-editor-pyqt-1/
    def openFileDialog(self):
        # Get filename and show only .writer files
        self.fullName, filters = QFileDialog.getOpenFileName(self, "Open File",".","Text Files (*.txt)()")

        if self.fullName:
            fileContentString = files3.openFile(self.fullName)
            self.mainText.setText(fileContentString)
            

    def splitToLines(self, input):
        output = input.split("\n")
        return output

    def stitchToLine(self, input):
        output = "\n".join(input)
        return output

    # DONE killWhite
    def killWhite(self):
        self.tempCurrentTextContentLines = []
        self.currentTextContentLines = self.splitToLines(self.currentTextContent)
        for line in self.currentTextContentLines:
            self.tempCurrentTextContentLines.append(re.sub(" +", " ",line).strip())
            # https://statisticsglobe.com/python-remove-whitespace-in-string
        self.currentTextContent = self.stitchToLine(self.tempCurrentTextContentLines)
        self.mainText.setText(self.currentTextContent)

    # TODO update currentTextContent if text in QTextEdit changes
    # def saveToCurrentTextContent(self):
    #     self.currentTextContent = ???

    # TODO find out what @pyqtSlot() does; reference: # https://stackoverflow.com/a/25994381
    # @pyqtSlot()
    def saveToOpenedFile(self):
        files3.saveToFile(self.fullName, self.currentTextContent)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec()