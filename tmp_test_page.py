import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

import datetime as pydatetime
import pandas as pd
# from PIL import Image
form_2nd_cls = uic.loadUiType("ui/test_widget.ui")[0]
from confidence_page import ThirdWindowCls

#class SecondWindowCls(QDialog, QWidget, form_2nd_cls):
class tmpSecondWindowCls(QDialog, QWidget, form_2nd_cls):
    def __init__(self, mainInfoDict):
        #super(SecondWindowCls, self).__init__()
        super(tmpSecondWindowCls, self).__init__()
        self.initUi(mainInfoDict)
        # self.initUi()
        self.show()

        # 선택지
        self.ansRBtn1.clicked.connect(self.radioBtn_clicked)
        self.ansRBtn2.clicked.connect(self.radioBtn_clicked)
        self.ansRBtn3.clicked.connect(self.radioBtn_clicked)
        self.ansRBtn4.clicked.connect(self.radioBtn_clicked)
        self.ansRBtn5.clicked.connect(self.radioBtn_clicked)

        self.teSubmitBtn.clicked.connect(self.teSubmitBtn_cicked)
        self.homeBtn.clicked.connect(self.homeBtn_cicked)


    def initUi(self, mainInfo):
    # def initUi(self):
        self.setupUi(self)

        self.infoDict = mainInfo
        self.testCnt = 1
        self.teStartTs = self.get_now_timestamp()

        self.df2 = pd.DataFrame([['TE'+str(self.testCnt)+'_START', self.teStartTs, -1, -1]],
                               index=[self.infoDict['idxCnt']], columns=['status', 'ts', 'ans', 'confidence'])
        self.infoDict['idxCnt'] += 1

        self.df2.to_csv(self.infoDict['fileName'], mode='a', header=False, index=True)

        self.nameLabel2.setText(self.infoDict['name'])
        self.birthLabel2.setText(self.infoDict['birth'])
        self.expCntLabel2.setText(self.infoDict['expCnt'])

        self.teAns = 0
        questPixmap = QPixmap("imgs/questions/" + str(self.testCnt) + "_resize.jpg")
        self.testLabel.setPixmap(questPixmap)
        self.testLabel.resize(questPixmap.width(), questPixmap.height())


    def radioBtn_clicked(self):
        if self.ansRBtn1.isChecked(): self.teAns = 1
        elif self.ansRBtn2.isChecked(): self.teAns = 2
        elif self.ansRBtn3.isChecked(): self.teAns = 3
        elif self.ansRBtn4.isChecked(): self.teAns = 4
        elif self.ansRBtn5.isChecked(): self.teAns = 5

        print("The selected answer is ", self.teAns)


    def teSubmitBtn_cicked(self):
        QMessageBox.about(self, '선택정답', str(self.teAns)+'번')
        self.teEndTs = self.get_now_timestamp()

        # confidence 받아오는 창 다녀오기 필요

        # self.df2.append({'status':'TE'+str(self.testCnt)+'_END', 'ts':self.teEndTs, 'ans':self.teAns, 'confidence':-1}, ignore_index=True)
        self.df3 = pd.DataFrame([['TE'+str(self.testCnt)+'_END', self.teEndTs, self.teAns, -1]],
                                index=[self.infoDict['idxCnt']], columns=['status', 'ts', 'ans', 'confidence'])
        self.infoDict['idxCnt'] += 1
        self.df3.to_csv(self.infoDict['fileName'], mode='a', header=False, index=True)

        # self.hide()
        # self.third = ThirdWindowCls(self.infoDict, self.testCnt)
        # self.third.exec()
        # self.show()

        self.testCnt += 1

        if self.testCnt < 6:
            self.updateUI()
        else:
            self.close()

    def updateUI(self):
        self.teAns = 0
        questPixmap = QPixmap("imgs/questions/" + str(self.testCnt) + "_resize.jpg")
        self.testLabel.setPixmap(questPixmap)
        self.testLabel.resize(questPixmap.width(), questPixmap.height())

        stateOfTestCnt = str(self.testCnt) + ' / 5'
        self.testCntLabel.setText(stateOfTestCnt)

        self.teStartTs = self.get_now_timestamp()
        self.df2 = pd.DataFrame([['TE'+str(self.testCnt)+'_START', self.teStartTs, -1, -1]],
                               index=[self.infoDict['idxCnt']], columns=['status', 'ts', 'ans', 'confidence'])
        self.infoDict['idxCnt'] += 1

        self.df2.to_csv(self.infoDict['fileName'], mode='a', header=False, index=True)

        # 문제 변경 필요
        # self.teAns = 0
        # questPixmap = QPixmap("imgs/questions/2_resize.jpg")
        # self.testLabel.setPixmap(questPixmap)
        # self.testLabel.resize(questPixmap.width(), questPixmap.height())
        # if self.testCnt < 5:


    def homeBtn_cicked(self):

        self.close()


    def get_now(self):
        # 현재 시스템 시간을 datetime형으로 반환
        return pydatetime.datetime.now()

    def get_now_timestamp(self):
        # 현재 시스템 시간을 POSIX timestamp float형으로 반환
        return self.get_now().timestamp()
