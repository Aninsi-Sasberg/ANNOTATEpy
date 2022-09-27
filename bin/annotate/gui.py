import enum
import files3
import load
import date

import os

from PyQt6 import QtWidgets
# from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWidgets import *
from PyQt6.QtCore import pyqtSlot
# from PyQt6.QtGui import QKeySequence
# from PyQt6.QtGui import QShortcut
from PyQt6.QtGui import QAction, QIcon, QFont, QCloseEvent

import sys
import re
from webbrowser import open as webOpen

class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
    # def __init__(self):
        # super(MainWindow, self).__init__()
        self.setGeometry(200, 200, 400, 400)
        self.setWindowTitle("ANNOTATEpy")
        self.icon = QIcon()
        self.icon.addFile(os.path.normpath(".\\res\\icon\\ANNOTATEpy.png"))
        self.setWindowIcon(self.icon)

        self.fullName = ""
        self.currentTextContent = ""
        self.fileContentString = ""
        self.fileChanged = False
        self.zoomCounter = 0
        self.wrapNum = 1
        self.lastUserID = 0
        self.defaultPreset = 0

        self.initUI()
        self.loadSettings()

    def createNewAction(self, title, shortcut, statusTip, action, menu):
        self.newAction = QAction(title)
        self.newAction.setShortcut(shortcut)
        self.newAction.setStatusTip(statusTip)
        self.newAction.triggered.connect(action)
        menu.addAction(self.newAction)

    def loadSettingsUserPreset(self):
        for userIndex, user in enumerate(load.sroot):
            if userIndex != 0:
                self.menuUser.addSeparator()
            self.userIndex = userIndex
            self.createNewAction(user.attrib["name"], "Ctrl+{}".format(userIndex), "Switch to User: {}".format(user.attrib["name"]), lambda: self.switchUserPreset(userIndex), self.menuUser)
            for presetIndex, preset in enumerate(load.sroot[userIndex]):
                self.presetIndex = presetIndex
                self.createNewAction(preset.attrib["name"], "Ctrl+Alt+{}".format(presetIndex), "Switch to Preset \"{}\" of User \"{}\"".format(preset.attrib["name"], user.attrib["name"]), self.openGithub, self.menuUser)

    # https://doc.qt.io/qtforpython-5/overviews/qtwidgets-mainwindows-menus-example.html#menus-example
    def createMenubarActions(self):
        # # self.menuFile.addAction("New File")
        # self.menuFileNewFile = QAction("New File", self)
        # self.menuFileNewFile.setShortcut("Ctrl+N")
        # self.menuFileNewFile.setStatusTip("Create a new File")
        # # menuFile.triggered.connect(self.close_application)
        # self.menuFile.addAction(self.menuFileNewFile)

        self.menuFileOpenFile = QAction("&Open File", self)
        self.menuFileOpenFile.setShortcut("Ctrl+O")
        self.menuFileOpenFile.setStatusTip("Open a File")
        self.menuFileOpenFile.triggered.connect(self.openFileDialog)
        self.menuFile.addAction(self.menuFileOpenFile)

        self.menuFileSaveFile = QAction("&Save File", self)
        self.menuFileSaveFile.setShortcut("Ctrl+S")
        self.menuFileSaveFile.setStatusTip("Save a File")
        self.menuFileSaveFile.triggered.connect(self.saveToFile)
        self.menuFile.addAction(self.menuFileSaveFile)

        self.menuFileSaveAsFile = QAction("Save &As...", self)
        self.menuFileSaveAsFile.setShortcut("Ctrl+Shift+S")
        self.menuFileSaveAsFile.setStatusTip("Save as a new File")
        self.menuFileSaveAsFile.triggered.connect(self.saveAsFileDialog)
        self.menuFile.addAction(self.menuFileSaveAsFile)

        self.menuFileRefreshFile = QAction("&Refresh File", self)
        self.menuFileRefreshFile.setShortcut("Ctrl+R")
        self.menuFileRefreshFile.setShortcut("F5")
        self.menuFileRefreshFile.setStatusTip("Refresh currently opened File")
        self.menuFileRefreshFile.triggered.connect(self.openFile)
        self.menuFile.addAction(self.menuFileRefreshFile)



        self.menuEditUndo = QAction("&Undo", self)
        self.menuEditUndo.setShortcut("Ctrl+Z")
        self.menuEditUndo.setStatusTip("Undo last Edit")
        self.menuEditUndo.triggered.connect(self.undo)
        self.menuEdit.addAction(self.menuEditUndo)

        self.menuEditRedo = QAction("&Redo", self)
        self.menuEditRedo.setShortcut("Ctrl+Y")
        self.menuEditRedo.setShortcut("Ctrl+Shift+Z")
        self.menuEditRedo.setStatusTip("Redo last Edit")
        self.menuEditRedo.triggered.connect(self.redo)
        self.menuEdit.addAction(self.menuEditRedo)

        self.menuEdit.addSeparator()

        self.menuEditKillWhite = QAction("Delete &Whitespace", self)
        self.menuEditKillWhite.setShortcut("Shift+Alt+F")
        self.menuEditKillWhite.setStatusTip("Delete unnecessary Whitespace in whole File")
        self.menuEditKillWhite.triggered.connect(self.killWhite)
        self.menuEdit.addAction(self.menuEditKillWhite)

        self.menuEditInsertDate = QAction("Insert &Date", self)
        self.menuEditInsertDate.setShortcut("Ctrl+.")
        self.menuEditInsertDate.setStatusTip("Insert current Date to Cursor position")
        self.menuEditInsertDate.triggered.connect(self.insertDate)
        self.menuEdit.addAction(self.menuEditInsertDate)



        self.menuViewNewWindow = QAction("&New Window", self)
        self.menuViewNewWindow.setShortcut("Ctrl+N")
        self.menuViewNewWindow.setStatusTip("Open a new Window")
        self.menuFile.triggered.connect(self.newWindow)
        self.menuView.addAction(self.menuViewNewWindow)

        self.menuViewFontChooser = QAction("Choose &Font", self)
        self.menuViewFontChooser.setShortcut("Ctrl+F")
        self.menuViewFontChooser.setStatusTip("Choose a Font to Display your Text in")
        self.menuViewFontChooser.triggered.connect(self.fontChooser)
        self.menuView.addAction(self.menuViewFontChooser)

        self.menuViewLineWrap = QAction("Switch &Wrap Mode", self)
        self.menuViewLineWrap.setShortcut("Ctrl+Shift+W")
        self.menuViewLineWrap.setStatusTip("Switch between Line Wrapping and no Line Wrapping")
        self.menuViewLineWrap.triggered.connect(self.lineWrapMode)
        self.menuView.addAction(self.menuViewLineWrap)

        self.menuView.addSeparator()
        
        self.menuViewZoomIn = QAction("Zoom &In", self)
        self.menuViewZoomIn.setShortcut("Ctrl++")
        self.menuViewZoomIn.setStatusTip("Zoom In to make Text larger")
        self.menuViewZoomIn.triggered.connect(self.zoomingIn)
        self.menuView.addAction(self.menuViewZoomIn)

        self.menuViewZoomOut = QAction("Zoom &Out", self)
        self.menuViewZoomOut.setShortcut("Ctrl+-")
        self.menuViewZoomOut.setStatusTip("Zoom Out to make Text smaller")
        self.menuViewZoomOut.triggered.connect(self.zoomingOut)
        self.menuView.addAction(self.menuViewZoomOut)

        self.menuViewZoomBack = QAction("Zoom &Back", self)
        self.menuViewZoomBack.setShortcut("Ctrl+0")
        self.menuViewZoomBack.setStatusTip("Zoom Back to make Text original Scale")
        self.menuViewZoomBack.triggered.connect(self.zoomingBack)
        self.menuView.addAction(self.menuViewZoomBack)




        self.menuHelpOpenHelp = QAction("Open &Help File", self)
        self.menuHelpOpenHelp.setShortcut("F1")
        self.menuHelpOpenHelp.setStatusTip("Open the Github Repository of ANNOTATEpy")
        self.menuHelpOpenHelp.triggered.connect(self.openHelpFile)
        self.menuHelp.addAction(self.menuHelpOpenHelp)

        self.menuHelpOpenGithub = QAction("Open &Github", self)
        self.menuHelpOpenGithub.setShortcut("Ctrl+Alt+P")
        self.menuHelpOpenGithub.setStatusTip("Open the Github Repository of ANNOTATEpy")
        self.menuHelpOpenGithub.triggered.connect(self.openGithub)
        self.menuHelp.addAction(self.menuHelpOpenGithub)


    # https://www.binpress.com/building-text-editor-pyqt-1/
    def initMenubar(self):

        self.menubar = self.menuBar()

        self.menuFile = self.menubar.addMenu("&File")
        self.menuEdit = self.menubar.addMenu("&Edit")
        self.menuView = self.menubar.addMenu("&View")
        self.menuUser = self.menubar.addMenu("&User")
        self.menuHelp = self.menubar.addMenu("&Help")

        self.createMenubarActions()
        self.loadSettingsUserPreset()



    def closeEvent(self, a0: QCloseEvent) -> None:
        self.lastUserID = load.sroot[self.currentUser].attrib["id"]
        return super().closeEvent(a0)

    def loadSettings(self):
        self.newFont.setFamily(load.sroot[self.lastUserID][self.defaultPreset][2].attrib["fontFamily"])
        self.newFont.setPointSize(int(load.sroot[self.lastUserID][self.defaultPreset][2].attrib["fontSize"]))

        self.mainText.setFont(self.newFont)


    # @pyqtSlot()
    def switchUserPreset(self, userIndex):
        self.currentUser = load.sroot[userIndex].attrib["id"]


    # https://www.youtube.com/watch?v=-2uyzAqefyE
    def initUI(self):

        self.mainText = QTextEdit(self)
        self.setCentralWidget(self.mainText)
        # self.mainText.resize(400,400)
        # self.mainText.setGeometry(0, 0, 800,800)
        # self.mainText.
        self.mainText.setUndoRedoEnabled(True)
        self.newFont = QFont("Arial")
        self.mainText.setFont(self.newFont)

        self.widget = QWidget()
        self.layout = QVBoxLayout()

        self.layout.addWidget(self.mainText)

        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)
        self.initMenubar()

        with open(os.path.normcase(".\\bin\\annotate\\main.css"), 'r') as style:
            sheet = style.read()

        self.setStyleSheet(sheet)


        self.updateCurrentTextContentSignal = self.mainText.textChanged
        self.updateCurrentTextContentSignal.connect(self.updateCurrentTextContent)


    # https://www.binpress.com/building-text-editor-pyqt-1/
    def newWindow(self):
        print("shit")
        spawnNewWindow = MainWindow(self)
        # spawnNewWindow = MainWindow()
        spawnNewWindow.show()

    # https://www.binpress.com/building-text-editor-pyqt-1/
    @pyqtSlot()
    def openFileDialog(self):
        # Get filename and show only .writer files
        self.newFullName, filters = QFileDialog.getOpenFileName(self, "Open File","","All Files(*);;Text Files (*.txt)")
        if self.newFullName:
            self.fullName = self.newFullName
            self.openFile()
            self.setWindowTitle("ANNOTATEpy  " + self.fullName)

    # TODO else statement and QMessageBox in openFile
    @pyqtSlot()
    def openFile(self):
        if self.fullName:
            self.fileContentString = files3.openFile(self.fullName)
            self.mainText.setText(self.fileContentString)

    @pyqtSlot()
    def saveFileDialog(self):
        self.fullName, filters = QFileDialog.getSaveFileName(self, "Save File","","All Filetypes(*);;Text Files (*.txt);;Markdown Files (*.md)")
        self.saveToOpenedFile()
        self.setWindowTitle("ANNOTATEpy  " + self.fullName)

    @pyqtSlot()
    def saveAsFileDialog(self):
        self.newFullName, filters = QFileDialog.getSaveFileName(self, "Save As",os.path.basename(self.fullName),"All Filetypes(*);;Text Files (*.txt);;Markdown Files (*.md)")
        if self.newFullName:
            self.saveToOpenedFile()
            self.setWindowTitle("ANNOTATEpy  " + self.fullName)
            self.fullName = self.newFullName

    # DONE find out what @pyqtSlot() does; reference: # https://stackoverflow.com/a/25994381
    @pyqtSlot()
    def saveToOpenedFile(self):
        if self.fullName:
            self.updateCurrentTextContent()
            files3.saveToFile(self.fullName, self.currentTextContent)
            self.fileContentString = self.currentTextContent
            self.updateCurrentTextContent()

    @pyqtSlot()
    def saveToFile(self):
        if self.fullName:
            self.updateCurrentTextContent()
            files3.saveToFile(self.fullName, self.currentTextContent)
            self.fileContentString = self.currentTextContent
            self.updateCurrentTextContent()
        else:
            self.saveFileDialog()

    #TODO FileChanged, makes Pop-Up before quitting app; and if 'cancel', keep app open
    def updateCurrentTextContent(self):
        self.currentTextContent = self.mainText.toPlainText()

        if self.currentTextContent != self.fileContentString:
            self.setWindowTitle("ANNOTATEpy  " + self.fullName + " *")
            self.fileChanged = True
        else:
            self.setWindowTitle("ANNOTATEpy  " + self.fullName)
            self.fileChanged = False

        return self.currentTextContent


    def splitToLines(self, input):
        output = input.split("\n")
        return output

    def stitchToLine(self, input):
        output = "\n".join(input)
        return output

    @pyqtSlot()
    def killWhite(self):
        self.tempCurrentTextContentLines = []
        self.currentTextContentLines = self.splitToLines(self.currentTextContent)
        for line in self.currentTextContentLines:
            # TODO let user choose if to strip and if strip then lstrip()/rstrip()/strip() options
            self.tempCurrentTextContentLines.append(re.sub(" +", " ",line).strip())
            # https://statisticsglobe.com/python-remove-whitespace-in-string
        self.currentTextContent = self.stitchToLine(self.tempCurrentTextContentLines)
        # TODO make it so that killWhite doesn't erase Undo Memory
        self.mainText.setText(self.currentTextContent)

    @pyqtSlot()
    def undo(self):
        self.mainText.undo()

    @pyqtSlot()
    def redo(self):
        self.mainText.redo()

    @pyqtSlot()
    def zoomingIn(self):
        self.mainText.zoomIn(+1)
        self.zoomCounter += 1

    @pyqtSlot()
    def zoomingOut(self):
        self.mainText.zoomOut(+1)
        self.zoomCounter -= 1

    @pyqtSlot()
    def zoomingBack(self):
        self.mainText.zoomOut(self.zoomCounter)
        self.zoomCounter = 0

    # https://codingshiksha.com/python/python-3-pyqt5-file-dialogfont-pickercolor-picker-using-qfontdialog-qcolordialog-widgets-gui-desktop-app-full-project-for-beginners/
    def fontChooser(self):
        self.newFont, self.fontFine = QFontDialog.getFont(self.newFont, self)
        if self.fontFine:
            self.mainText.setFont(self.newFont)
            self.zoomingBack()

    # TODO fix bug that gets rid of scrollbar if switching lineWrapMode when window not maximized
    def lineWrapMode(self):
        if self.wrapNum == 0:
            self.mainText.setLineWrapMode(QTextEdit.LineWrapMode.WidgetWidth)
            self.wrapNum = 1
        else:
            self.mainText.setLineWrapMode(QTextEdit.LineWrapMode.NoWrap)
            self.wrapNum = 0

    # TODO Implement Date Format setting
    @pyqtSlot()
    def setDateFormat(self):
        # self.mainText.insertPlainText(date.getDate("%Y"))
        pass

    # TODO Implement Date Format loading
    @pyqtSlot()
    def insertDate(self):
        self.mainText.insertPlainText(date.getDate("%Y"))

    @pyqtSlot()
    def openHelpFile(self):
        self.fileContentString = files3.openFile(os.path.normpath(".\\res\\docs\\help.txt"))
        self.mainText.setText(self.fileContentString)

    @pyqtSlot()
    def openGithub(self):
        webOpen('https://github.com/Aninsi-Sasberg/ANNOTATEpy')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec()