
# This is an attempt to use the box layout manager
# from: https://coderslegacy.com/python/pyqt-layout-management/
#
"""PySide6 port of the widgets/dialogs/findfiles example from Qt v5.x"""

from PySide6 import QtCore, QtGui, QtWidgets


class Window(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.InitMyUI()
        
    def InitMyUI(self):
        Button1 = self.createButton('PySIde', self.DoButton1)
        Button2 = self.createButton("MY Button 2", self.DoButton2)
        Button3 = self.createButton("MY Button 3", self.DoButton3)
        #vbox = QtWidgets.QHBoxLayout()
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(Button1)
        vbox.addWidget(Button2)
        vbox.addWidget(Button3)
        self.setLayout(vbox)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("My Box Layout Example from code")

    def DoButton1(self):
        print("Button One Clicked!")

    def DoButton2(self):
        print("Button Two Clicked!")

    def DoButton3(self):
        print("Button Three Clicked!")

    def createButton(self, text, member):
        button = QtWidgets.QPushButton(text)
        button.clicked.connect(member)
        return button


if __name__ == '__main__':

    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
