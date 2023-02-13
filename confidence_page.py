import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

import datetime as pydatetime
import pandas as pd
# from PIL import Image
form_3rd_cls = uic.loadUiType("ui/confidence_widget.ui")[0]

class ThirdWindowCls(QDialog, QWidget, form_3rd_cls):
    def __init__(self, mainInfoDict, teCnt, parent_widget):
        super(ThirdWindowCls, self).__init__()
        self.initUi(mainInfoDict, teCnt)
        # self.initUi()
        # self.show()

        # 선택지
        self.cnfRBtn1.clicked.connect(self.cnfRadioBtn_clicked)
        self.cnfRBtn2.clicked.connect(self.cnfRadioBtn_clicked)
        self.cnfRBtn3.clicked.connect(self.cnfRadioBtn_clicked)
        self.cnfRBtn4.clicked.connect(self.cnfRadioBtn_clicked)
        self.cnfRBtn5.clicked.connect(self.cnfRadioBtn_clicked)

        self.cnfSubmitBtn.clicked.connect(self.cnfSubmitBtn_cicked)

        self.parent_widget = parent_widget

    def initUi(self, mainInfo, teCnt):
    # def initUi(self):
        self.setupUi(self)

        self.infoDict = mainInfo
        self.cnfCnt = teCnt
        stateOfCnfCnt = str(self.cnfCnt) + ' / 5'
        self.cnfCntLabel.setText(stateOfCnfCnt)
        self.cnfStartTs = self.get_now_timestamp()

        # self.df2 = pd.DataFrame([['CONFIDENCE'+str(self.cnfCnt)+'_START', self.cnfStartTs, -1, -1]],
        #                        index=[self.infoDict['idxCnt']], columns=['status', 'ts', 'ans', 'confidence'])
        # self.infoDict['idxCnt'] += 1
        #
        # self.df2.to_csv(self.infoDict['fileName'], mode='a', header=False, index=True)

        self.cnfAns = 0


    def cnfRadioBtn_clicked(self):
        if self.cnfRBtn1.isChecked(): self.cnfAns = 1
        elif self.cnfRBtn2.isChecked(): self.cnfAns = 2
        elif self.cnfRBtn3.isChecked(): self.cnfAns = 3
        elif self.cnfRBtn4.isChecked(): self.cnfAns = 4
        elif self.cnfRBtn5.isChecked(): self.cnfAns = 5

        print("The selected condfidence value is ", self.cnfAns)


    def cnfSubmitBtn_cicked(self):
        # QMessageBox.about(self, '선택정답', str(self.cnfAns)+'번')
        self.cnfEndTs = self.get_now_timestamp()

        # confidence 받아오는 창 다녀오기 필요

        statusMsg = ""
        if self.cnfCnt < 5:
            statusMsg = 'CONF'+str(self.cnfCnt)+'_END&TE'+str(self.cnfCnt+1)+'_START'
        else:
            statusMsg = 'CONF'+str(self.cnfCnt)+'_END'

        # # self.df2.append({'status':'TE'+str(self.cnfCnt)+'_END', 'ts':self.teEndTs, 'ans':self.teAns, 'confidence':-1}, ignore_index=True)
        # self.df4 = pd.DataFrame([['CONF'+str(self.cnfCnt)+'_END&TE'+str(self.cnfCnt+1)+'_START', self.cnfEndTs, -1, self.cnfAns]],
        #                         index=[self.infoDict['idxCnt']], columns=['status', 'ts', 'ans', 'confidence'])
        self.df4 = pd.DataFrame([[statusMsg, self.cnfEndTs, -1, self.cnfAns]])
        self.infoDict['idxCnt'] += 1
        self.df4.to_csv(self.infoDict['fileName'], mode='a', header=False, index=True)

        self.cnfCnt += 1

        self.hide()

        if self.cnfCnt < 6 :
            self.parent_widget.show()
        else:
            self.close()
        # sys.exit(ui.exec_())


    def get_now(self):
        # 현재 시스템 시간을 datetime형으로 반환
        return pydatetime.datetime.now()

    def get_now_timestamp(self):
        # 현재 시스템 시간을 POSIX timestamp float형으로 반환
        return self.get_now().timestamp()
