import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

import datetime as pydatetime
import pandas as pd
# from PIL import Image
form_2nd_cls = uic.loadUiType("ui/test_widget.ui")[0]
from confidence_page import ThirdWindowCls

class SecondWindowCls(QDialog, QWidget, form_2nd_cls):
    def __init__(self, mainInfoDict):
        super(SecondWindowCls, self).__init__()
        self.initUi(mainInfoDict)
        # self.initUi()
        # self.show()

        # 선택지
        self.ansRBtn1.clicked.connect(self.radioBtn_clicked)
        self.ansRBtn2.clicked.connect(self.radioBtn_clicked)
        self.ansRBtn3.clicked.connect(self.radioBtn_clicked)
        self.ansRBtn4.clicked.connect(self.radioBtn_clicked)
        self.ansRBtn5.clicked.connect(self.radioBtn_clicked)

        self.rBtnList = [self.ansRBtn1, self.ansRBtn2, self.ansRBtn3, self.ansRBtn4, self.ansRBtn5]
        self.radioGroup = QButtonGroup()

        for i, rbtn in enumerate(self.rBtnList, 1):
            self.radioGroup.addButton(rbtn, i)

        self.teSubmitBtn.clicked.connect(self.teSubmitBtn_cicked)


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
        self.expTypeLabel2.setText(self.infoDict['expType'])

        self.testIdxList = []
        self.idx4test = int(self.infoDict['expCnt'])

        self.imgFullPath = 'imgs/resizing2/' + str(self.idx4test) + '/'
        self.imgList = os.listdir(self.imgFullPath)
        self.imgList.sort()

        self.teAns = 0

        self.imgIdx = 0
        if self.expTypeLabel2.text() == 'Pre-Test':
            self.imgIdx = self.testCnt * 2 - 1
        else:
            self.imgIdx = self.testCnt * 2 - 2

        # questPixmap = QPixmap("imgs/questions/" + str(self.testCnt) + "_resizing.jpg")
        questPixmap = QPixmap(self.imgFullPath + self.imgList[self.imgIdx])
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
        # QMessageBox.about(self, '선택정답', str(self.teAns)+'번')
        if self.teAns == 0:
            QMessageBox.information(self, 'error!', '정답을 선택하세요!')

        else:
            self.teEndTs = self.get_now_timestamp()

            # self.df2.append({'status':'TE'+str(self.testCnt)+'_END', 'ts':self.teEndTs, 'ans':self.teAns, 'confidence':-1}, ignore_index=True)
            self.df3 = pd.DataFrame([['TE'+str(self.testCnt)+'_END&CONF'+str(self.testCnt)+'_START', self.teEndTs, self.teAns, -1]],
                                    index=[self.infoDict['idxCnt']], columns=['status', 'ts', 'ans', 'confidence'])
            self.infoDict['idxCnt'] += 1
            self.df3.to_csv(self.infoDict['fileName'], mode='a', header=False, index=True)

            self.hide()
            self.confidence_page = ThirdWindowCls(self.infoDict, self.testCnt, self)
            # self.third = ThirdWindowCls(self.infoDict, self.testCnt)
            # self.third.exec()
            # self.show()


            if self.testCnt < 6:
                self.testCnt += 1
                # self.updateUI()
                self.confidence_page.show()
            else:
                self.close()


    def updateUI(self):
        self.radioGroup.setExclusive(False)
        self.ansRBtn1.setChecked(False)
        self.ansRBtn2.setChecked(False)
        self.ansRBtn3.setChecked(False)
        self.ansRBtn4.setChecked(False)
        self.ansRBtn5.setChecked(False)
        self.radioGroup.setExclusive(True)

        self.teAns = 0
        if self.expTypeLabel2.text() == 'Pre-Test':
            self.imgIdx = self.testCnt * 2 - 1
        else:
            self.imgIdx = self.testCnt * 2 - 2


        questPixmap = QPixmap(self.imgFullPath + self.imgList[self.imgIdx])
        self.testLabel.setPixmap(questPixmap)
        self.testLabel.resize(questPixmap.width(), questPixmap.height())

        stateOfTestCnt = str(self.testCnt) + ' / 5'
        self.testCntLabel.setText(stateOfTestCnt)



        # self.teStartTs = self.get_now_timestamp()
        # self.df2 = pd.DataFrame([['CONF'+str(self.testCnt-1)+'_START', self.teStartTs, -1, -1]],
        #                        index=[self.infoDict['idxCnt']], columns=['status', 'ts', 'ans', 'confidence'])
        # self.infoDict['idxCnt'] += 1

        # self.df2.to_csv(self.infoDict['fileName'], mode='a', header=False, index=True)

    def get_now(self):
        # 현재 시스템 시간을 datetime형으로 반환
        return pydatetime.datetime.now()

    def get_now_timestamp(self):
        # 현재 시스템 시간을 POSIX timestamp float형으로 반환
        return self.get_now().timestamp()
