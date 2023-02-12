import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

form_class = uic.loadUiType("ui/main_page.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.fontSize = 10

        self.name = ""
        self.birth = ""
        self.expCnt = 0

        self.submitBtn.clicked.connect(self.submitBtn_clicked)



    def submitBtn_clicked(self):
        self.name = self.nameLEdit.toPlainText()
        self.birth = self.birthLEdit.toPlainText()
        self.expCnt = self.expCntLEdit.toPlainText()

        print(self.name, self.birth, self.expCnt)

        #QMessageBox.about(self, '선택된 항목', msg+'선택됨')


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()