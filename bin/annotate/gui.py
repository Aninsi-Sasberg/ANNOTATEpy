import files
import date
import os
import sys
import re
from webbrowser import open as webOpen

from PyQt6.QtWidgets import QMainWindow, QApplication, QTextEdit, QWidget, QVBoxLayout, QFileDialog, QFontDialog
from PyQt6.QtCore import pyqtSlot
from PyQt6.QtGui import QAction, QIcon, QFont


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(200, 200, 400, 400)
        self.setWindowTitle("ANNOTATEpy")
        self.icon = QIcon()
        self.icon.addFile(os.path.normcase(".\\res\\icon\\ANNOTATEpy.png"))
        self.setWindowIcon(self.icon)

        self.fullName = ""
        self.currentTextContent = ""
        self.fileContentString = ""
        self.fileChanged = False
        self.zoomCounter = 0
        self.dialogExit = False

        self.initUI()

    # https://doc.qt.io/qtforpython-5/overviews/qtwidgets-mainwindows-menus-example.html#menus-example
    def createMenubarActions(self):
        # File
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

        self.menuFileSaveAsFile = QAction("Save &As File", self)
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


        # Edit
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


        # View
        self.menuViewFontChooser = QAction("Choose &Font", self)
        self.menuViewFontChooser.setShortcut("Ctrl+Shift+F")
        self.menuViewFontChooser.setStatusTip("Choose a Font to Display your Text in")
        self.menuViewFontChooser.triggered.connect(self.fontChooser)
        self.menuView.addAction(self.menuViewFontChooser)

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


        # Help
        self.menuHelpOpenHelp = QAction("Open &Help File", self)
        self.menuHelpOpenHelp.setShortcut("F1")
        self.menuHelpOpenHelp.setStatusTip("Open the Github Repository of ANNOTATEpy")
        self.menuHelpOpenHelp.triggered.connect(self.openHelpFile)
        self.menuHelp.addAction(self.menuHelpOpenHelp)

        self.menuHelpOpenGithub = QAction("Open on &Github", self)
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
        self.menuHelp = self.menubar.addMenu("&Help")

        self.createMenubarActions()


    # https://www.youtube.com/watch?v=-2uyzAqefyE
    def initUI(self):
        self.mainText = QTextEdit(self)
        self.setCentralWidget(self.mainText)
        self.mainText.setUndoRedoEnabled(True)
        self.newFont = QFont("Arial", 12)
        self.mainText.setFont(self.newFont)

        self.widget = QWidget()
        self.layout = QVBoxLayout()

        self.layout.addWidget(self.mainText)

        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)
        self.initMenubar()

        self.updateCurrentTextContentSignal = self.mainText.textChanged
        self.updateCurrentTextContentSignal.connect(self.updateCurrentTextContent)

    # https://www.binpress.com/building-text-editor-pyqt-1/
    @pyqtSlot()
    def openFileDialog(self):
        # Get filename and show only .writer files
        self.newFullName, filters = QFileDialog.getOpenFileName(self, "Open File","","All Files(*);;Text Files (*.txt)")
        if self.newFullName:
            self.fullName = self.newFullName
            self.openFile()
            self.setWindowTitle("ANNOTATEpy  " + self.fullName)

    @pyqtSlot()
    def openFile(self):
        if self.fullName:
            self.fileContentString = files.openFile(self.fullName)
            self.mainText.setText(self.fileContentString)

    @pyqtSlot()
    def saveFileDialog(self):
        self.fullName, filters = QFileDialog.getSaveFileName(self, "Save File","","All Filetypes(*);;Text Files (*.txt);;Markdown Files (*.md)")
        self.saveToFile()
        self.setWindowTitle("ANNOTATEpy  " + self.fullName)

    @pyqtSlot()
    def saveAsFileDialog(self):
        self.newFullName, filters = QFileDialog.getSaveFileName(self, "Save As File",os.path.basename(self.fullName),"All Filetypes(*);;Text Files (*.txt);;Markdown Files (*.md)")
        if self.newFullName:
            self.fullName = self.newFullName
            self.saveToFile()
            self.setWindowTitle("ANNOTATEpy  " + self.fullName)

    # https://stackoverflow.com/a/25994381
    @pyqtSlot()
    def saveToFile(self):
        if self.fullName:
            self.updateCurrentTextContent()
            files.saveToFile(self.fullName, self.currentTextContent)
            self.fileContentString = self.currentTextContent
            self.updateCurrentTextContent()
        elif self.dialogExit == False:
            self.dialogExit = True
            self.saveFileDialog()
            self.dialogExit = False

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
            # https://statisticsglobe.com/python-remove-whitespace-in-string
            self.tempCurrentTextContentLines.append(re.sub(" +", " ",line).strip())
        self.currentTextContent = self.stitchToLine(self.tempCurrentTextContentLines)
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

    @pyqtSlot()
    def insertDate(self):
        self.mainText.insertPlainText(date.getDate("%d.%m.%Y"))

    @pyqtSlot()
    def openHelpFile(self):
        self.fileContentString = files.openFile(os.path.normcase(".\\res\\docs\\help.txt"))
        self.mainText.setText(self.fileContentString)

    @pyqtSlot()
    def openGithub(self):
        webOpen('https://github.com/Aninsi-Sasberg/ANNOTATEpy')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec()