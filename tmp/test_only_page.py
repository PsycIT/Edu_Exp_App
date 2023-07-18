import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

from PIL import Image

form_cls = uic.loadUiType("ui/test_widget.ui")[0]

class secondWindowClass(QMainWindow, form_cls) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.fontSize = 10

        self.teAns = 0

        self.name = ""
        self.birth = ""
        self.expCnt = 0

        # 문제지
        # basewidth = 600
        # self.setResizeImg(basewidth)

        questPixmap = QPixmap("imgs/questions/2_resize.jpg")
        self.testLabel.setPixmap(questPixmap)
        self.testLabel.resize(questPixmap.width(), questPixmap.height())

        # 선택지
        self.ansRBtn1.clicked.connect(self.radioBtn_clicked)
        self.ansRBtn2.clicked.connect(self.radioBtn_clicked)
        self.ansRBtn3.clicked.connect(self.radioBtn_clicked)
        self.ansRBtn4.clicked.connect(self.radioBtn_clicked)
        self.ansRBtn5.clicked.connect(self.radioBtn_clicked)

        self.teSubmitBtn.clicked.connect(self.teSubmitBtn_clicked)

    def radioBtn_clicked(self):
        if self.ansRBtn1.isChecked(): self.teAns = 1
        elif self.ansRBtn2.isChecked(): self.teAns = 2
        elif self.ansRBtn3.isChecked(): self.teAns = 3
        elif self.ansRBtn4.isChecked(): self.teAns = 4
        elif self.ansRBtn5.isChecked(): self.teAns = 5

        print("The selected answer is ", self.teAns)

    def teSubmitBtn_clicked(self):
        self.name = "it"
        self.birth = "1114"
        self.expCnt = "1회차"

        print(self.name, self.birth, self.expCnt)

        QMessageBox.about(self, '선택정답', str(self.teAns)+'번')

        # self.close()


    # img 비율 유지하여 resizing & save
    def setResizeImg(self, basewidth=600):
        img = Image.open('imgs/questions/5.jpg')
        wpercent = (basewidth / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img_resize = img.resize((basewidth, hsize), Image.ANTIALIAS)
        img_resize.save('imgs/questions/5_resize.jpg')


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = secondWindowClass()
    myWindow.show()
    app.exec_()