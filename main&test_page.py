import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

import datetime as pydatetime
import pandas as pd
import openpyxl

# from test_page import SecondWindowCls
from tmp_test_page import tmpSecondWindowCls

form_class = uic.loadUiType("ui/main_page.ui")[0]

class WindowCls(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.mainStartTs = self.get_now_timestamp()
        self.expInfoDict = {"name":"", "birth":"", "expCnt":"", "1st_ts":str(self.mainStartTs), "idxCnt":0}
        self.df = pd.DataFrame([['EXP_START', self.mainStartTs, -1, -1]],
                               index=[self.expInfoDict['idxCnt']], columns=['status', 'ts', 'ans', 'confidence'])
        self.expInfoDict['idxCnt'] += 1
        self.nowTime = pydatetime.datetime.today().strftime("%Y%m%d%H%M")

        self.setupUi(self)

        self.submitBtn.clicked.connect(self.submitBtn_clicked)

    def submitBtn_clicked(self):
        self.mainEndTs = self.get_now_timestamp()
        self.expInfoDict['name'] = self.nameLEdit.text()
        self.expInfoDict['birth'] = self.birthLEdit.text()
        self.expInfoDict['expCnt'] = self.expCntLEdit.text()
        self.expInfoDict['2nd_ts'] = str(self.get_now_timestamp())
        self.expInfoDict['fileName'] = 'output/' + self.nowTime + '_' \
                                       + self.expInfoDict['name'] + '_' \
                                       + self.expInfoDict['expCnt'] \
                                       + '.csv'

        print('expInfo', self.expInfoDict)

        self.df.to_csv(self.expInfoDict['fileName'], mode='a', header=True, index=True)

        self.hide()
        # self.second = SecondWindowCls(self.expInfoDict)
        self.second = tmpSecondWindowCls(self.expInfoDict)
        self.second.exec()
        self.show()


    def get_now(self):
        # 현재 시스템 시간을 datetime형으로 반환
        return pydatetime.datetime.now()

    def get_now_timestamp(self):
        # 현재 시스템 시간을 POSIX timestamp float형으로 반환
        return self.get_now().timestamp()

        #QMessageBox.about(self, '선택된 항목', msg+'선택됨')


# class SecondWindowCls(QDialog, QWidget, form_2nd_cls):
#     def __init__(self):
#         super(SecondWindowCls, self).__init__()
#         self.initUi()
#         self.show()
#
#         # self.teSubmitBtn.clicked.connect(self.teSubmitBtn_cicked)
#         self.homeBtn.clicked.connect(self.teSubmitBtn_cicked)
#
#     def initUi(self):
#         self.setupUi(self)
#
#     def teSubmitBtn_cicked(self):
#         self.close()



if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowCls()
    myWindow.show()
    app.exec_()