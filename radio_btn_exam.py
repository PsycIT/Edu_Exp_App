import sys
from PyQt5.QtWidgets import *


class MyWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test")
        self.setGeometry(1000, 200, 700, 700)

        # Groupbox1. 여기에 라디오 버튼 3개 올릴 것임
        self.gpbox1 = QGroupBox(self)
        self.gpbox1.setGeometry(50, 100, 200, 300)

        # Groupbox2. 여기에 라디오 버튼 2개 올릴 것임
        self.gpbox2 = QGroupBox(self)
        self.gpbox2.setGeometry(400, 100, 200, 300)

        # 라디오버튼 3개, 이것들은 Groupbox1에 올라가고 자기들끼리 exclusive
        self.radio11 = QRadioButton("radio1-1", self.gpbox1)
        self.radio11.move(0, 0)

        self.radio12 = QRadioButton("radio1-2", self.gpbox1)
        self.radio12.move(0, 100)

        self.radio13 = QRadioButton("radio1-3", self.gpbox1)
        self.radio13.move(0, 200)

        # 라디오버튼 2개, 이것들은 Groupbox2에 올라가고 자기들끼리 exclusive
        self.radio21 = QRadioButton("gp2_radio1", self.gpbox2)
        self.radio21.move(0, 0)
        self.radio22 = QRadioButton("gp2_radio2", self.gpbox2)
        self.radio22.move(0, 100)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()

    app.exec_()