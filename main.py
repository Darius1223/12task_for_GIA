import sys
import os
from PyQt5 import QtWidgets

import design


class MyString:
    string = ""

    def __init__(self, ss=""):
        self.string = ss

    def __str__(self):
        return self.string

    def find(self, temp):
        if temp in self.string:
            return True
        else:
            return False

    def remove(self, a, b):
        self.string = self.string[0:self.string.find(a)] + b + self.string[self.string.find(a) + len(a):]

    def clear(self):
        self.string = ""


class Task12App(QtWidgets.QMainWindow, design.Ui_MainWindow):
    fragmentCount = 0
    currentString = MyString()
    newString = MyString()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.addFragmentButton.clicked.connect(self.getFragment)
        self.deleteButton.clicked.connect(self.deleteItem)
        self.startToEndButton.clicked.connect(self.startToEnd)
        self.removeButton.clicked.connect(self.remove)
        self.findButton.clicked.connect(self.find)


    def remove(self):
        a = self.removeA.text()
        b = self.removeB.text()

        if (self.newString.find(a)):
            self.newString.remove(a, self.removeB.text())
            self.endString.clear()
            self.endString.addItem(self.newString.string)

    def find(self):
        a = self.findCharBox.text()
        self.boolWidget.clear()
        if self.newString.find(a):
            self.boolWidget.addItem("True")
        else:
            self.boolWidget.addItem("False")

    def getFragment(self):
        count = self.countChar.value()
        char = self.getChar.text()

        if count == 0 or char == 0:
            return

        self.fragmentCount += 1
        temp = "{}. [{}: '{}'] ==> {}".format(self.fragmentCount, count, char, count * char)
        self.currentString.string += count * char
        self.stringWidget.addItem(temp)

        self.startString.clear()
        self.startString.addItem(self.currentString.string)

    def startToEnd(self):
        self.endString.clear()
        self.endString.addItem(self.currentString.string)
        self.newString.string = self.currentString.string

    def deleteItem(self):
        self.fragmentCount = 0
        self.stringWidget.clear()
        self.currentString.clear()
        self.startString.clear()

    def getString(self):
        pass


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Task12App()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
