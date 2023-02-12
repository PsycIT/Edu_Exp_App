import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class LayoutWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        # self.setWindowTitle('Subject Infomation')
        self.setWindowTitle('TEST')
        self.setGeometry(150, 100, 1000, 850)
        self.questIdx = 1


        self.showVBoxLayout()
        self.show()

    def showVBoxLayout(self):
        # GroupBox 생성
        expInfoGroupBox = QGroupBox("Experiments Infomation")
        contentGroupBox = QGroupBox("Test Infomation")
        questGroupBox = QGroupBox("문제지")
        ansGroupBox = QGroupBox("선택지")

        d_btn = QPushButton('4')
        e_btn = QPushButton('5')

        # Experiments Infomation (피험자명, test 유형, 회차)
        # 피험자명
        nameText = QLabel(self)
        # nameText = QTextBrowser(self)
        nameText.resize(50, 20)
        nameText.setText("정인택")

        # TEST 유형
        titleText = QLabel(self)
        titleText.setText("Pre-test (경제)")
        titleText.resize(100, 20)

        # TEST 회차
        expCntText = QLabel(self)
        expCntText.setText("1회차")
        expCntText.resize(50, 20)

        # TEST Infomation (문제지, 선택지, 잔여문제 정보, 제출 버튼)
        # 문제지
        questPixmap = QPixmap("imgs/questions/1.jpg")
        questLabel = QLabel(self)
        questLabel.setPixmap(questPixmap)
        questLabel.setContentsMargins(10, 10, 10, 10)
        questLabel.resize(questPixmap.width(), questPixmap.height())

        # 선택지
        self.ansRBtn1 = QRadioButton('1', self)
        self.ansRBtn1.clicked.connect(self.radioBtn_clicked)
        self.ansRBtn2 = QRadioButton('2', self)
        self.ansRBtn2.clicked.connect(self.radioBtn_clicked)
        self.ansRBtn3 = QRadioButton('3', self)
        self.ansRBtn3.clicked.connect(self.radioBtn_clicked)
        self.ansRBtn4 = QRadioButton('4', self)
        self.ansRBtn4.clicked.connect(self.radioBtn_clicked)
        self.ansRBtn5 = QRadioButton('5', self)
        self.ansRBtn5.clicked.connect(self.radioBtn_clicked)

        # 잔여문제
        questCntLabel = QLabel(self)
        questCntLabel.setText("1 / 10")

        # 제출버튼
        submitBtn = QPushButton('제출하기')
        submitBtn.setStyleSheet('border-image:url(./imgs/submitBtn.png) ;border;0px;')


        # Layout 설정

        # main page Top layout (Exp Info part) 설정
        upInnerLayout = QHBoxLayout()
        upInnerLayout.addWidget(nameText)
        upInnerLayout.addWidget(titleText)
        upInnerLayout.addWidget(expCntText)
        expInfoGroupBox.setLayout(upInnerLayout)

        upLayout = QHBoxLayout()
        # upLayout.addStretch(1)
        upLayout.addSpacing(40)
        upLayout.addWidget(expInfoGroupBox)
        # upLayout.addStretchF(expInfoGroupBox, 7)
        # upLayout.addStretch(2)
        upLayout.addSpacing(120)

        # main page Down layout (Test Info + Timer&Submit part) 설정
        # 문제지 layout
        lTopInnerLayout = QVBoxLayout()
        lTopInnerLayout.addWidget(questLabel)
        questGroupBox.setLayout(lTopInnerLayout)

        # 선택지 layout
        lMidInnnerLayout = QHBoxLayout()
        lMidInnnerLayout.addWidget(self.ansRBtn1)
        lMidInnnerLayout.addWidget(self.ansRBtn2)
        lMidInnnerLayout.addWidget(self.ansRBtn3)
        lMidInnnerLayout.addWidget(self.ansRBtn4)
        lMidInnnerLayout.addWidget(self.ansRBtn5)
        lMidInnnerLayout.addStretch(1)
        ansGroupBox.setLayout(lMidInnnerLayout)

        leftInnerLayout = QVBoxLayout()
        leftInnerLayout.addWidget(questGroupBox)
        leftInnerLayout.addWidget(ansGroupBox)
        leftInnerLayout.addStretch(1)
        leftInnerLayout.addWidget(questCntLabel, alignment=Qt.AlignCenter)
        contentGroupBox.setLayout(leftInnerLayout)

        # Test Info layout 통합 (문제지 + 선택지)
        leftLayout = QVBoxLayout()
        leftLayout.addWidget(contentGroupBox)

        rightLayout = QVBoxLayout()
        rightLayout.addWidget(d_btn)
        rightLayout.addWidget(submitBtn, alignment=Qt.AlignBottom)

        downLayout = QHBoxLayout()
        downLayout.addStretch(1)
        downLayout.addLayout(leftLayout)
        downLayout.addStretch(1)
        downLayout.addLayout(rightLayout)


        layout = QVBoxLayout()
        layout.addLayout(upLayout)
        # layout.addStretch(1)
        layout.addSpacing(10)
        layout.addLayout(downLayout)

        self.setLayout(layout)



    def radioBtn_clicked(self):
        msg = ""
        if self.ansRBtn1.isChecked():
            msg = "항목 1"
        elif self.ansRBtn2.isChecked():
            msg = "항목 2"
        elif self.ansRBtn3.isChecked():
            msg = "항목 3"
        elif self.ansRBtn4.isChecked():
            msg = "항목 4"
        elif self.ansRBtn5.isChecked():
            msg = "항목 5"

        QMessageBox.about(self, '선택된 항목', msg+'선택됨')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LayoutWindow()
    window.show()
    sys.exit(app.exec_())