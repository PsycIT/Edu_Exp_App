import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5 import uic

import pandas as pd
import openpyxl
import datetime as pydatetime

form_class = uic.loadUiType("ui/main_page_test.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.initUI()
        self.show()

    def initUI(self):
        self.ts = self.get_now_timestamp()
        self.df = pd.DataFrame([['EXP_START', self.ts, -1, -1]],
                               index=[1], columns=['status', 'ts', 'ans', 'confidence'])

        self.setupUi(self)

        self.expInfoDict = {"name":"", "birth":"", "expCnt":"", "1st_ts":str(self.ts)}

        self.submitBtn.clicked.connect(self.submitBtn_clicked)


    def submitBtn_clicked(self):
        self.expInfoDict['name'] = self.nameLEdit.text()
        self.expInfoDict['birth'] = self.birthLEdit.text()
        self.expInfoDict['expCnt'] = self.expCntLEdit.text()
        self.expInfoDict['2nd_ts'] = str(self.get_now_timestamp())

        print('expInfo', self.expInfoDict)

        nowTime = pydatetime.datetime.today().strftime("%Y%m%d%H%M%S")
        print(nowTime)

        exit(1)
        # fileName = self.expInfoDict['name']+self.expInfoDict['birth']+
        # self.df.to_csv('output/'+self.expInfoDict['name'])


    def get_now(self):
        # 현재 시스템 시간을 datetime형으로 반환
        return pydatetime.datetime.now()

    def get_now_timestamp(self):
        # 현재 시스템 시간을 POSIX timestamp float형으로 반환
        return self.get_now().timestamp()





if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()