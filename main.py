# This Python file uses the following encoding: utf-8
import sys
from mainwindow import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import *
from PySide6.QtGui import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.CustomInitialization()

    # Do the custom initialization for the GUI.
    def CustomInitialization(self):
        QObject.connect(self.ui.findButton, SIGNAL("clicked()"), self.find_clicked)
        self.loadTextFile()

    def find_clicked(self):
        self.searchString = self.ui.lineEdit.text()
        self.ui.textEdit.find(self.searchString, QTextDocument.FindWholeWords)

    def loadTextFile(self):
        self.inputFile = QFile("input.txt")
        if self.inputFile.open(QIODevice.ReadOnly | QIODevice.Text):
            self.textStrmData = QTextStream(self.inputFile)
            self.text = self.textStrmData.readAll()
            self.inputFile.close()
        else:
            self.text = "File Open failed"
        self.ui.textEdit.setPlainText(self.text)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())

