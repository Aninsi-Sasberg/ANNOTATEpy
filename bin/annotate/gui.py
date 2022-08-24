import os
from tkinter import filedialog
from files import File
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def saveFileDialog():
    try:
        # TODO: need condition to break if user presses close button on dialog, or else user is stuck in loop even if he doesn't want to save a file anymore
        path = filedialog.asksaveasfilename(confirmoverwrite=True, defaultextension=".txt")
        if not path:
            raise Exception
        print("You've selected the directory + filename:\n" + path)
    except:
        print("You have to choose a directory.")
    return path

def guiCreateFile():
    # select directory
    path = saveFileDialog()

    path, filename = os.path.split(path)
    filename, filetype = os.path.splitext(filename)
    File(filename, path, "w", filetype)

    # TODO, is this necessary?
    guiFileCreated = 1
    return guiFileCreated

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 400, 400)
    win.setWindowTitle("ANNOTATEpy")

    win.show()
    sys.exit(app.exec_())

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        