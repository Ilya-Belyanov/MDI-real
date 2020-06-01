from PyQt5 import QtWidgets
from .SpecterWidget import Ui_Specter
import re


class Specter(QtWidgets.QWidget):
    ALL_WAVE = 1
    RUN_WAVE = 2

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Specter()
        self.ui.setupUi(self)
        self.connectButton()
        self.ui.frameSpecter.removeWav()
        self.loadStyleSheets()

    def loadStyleSheets(self):
        style = "static/qcss/styleSpecterFrame.css"
        with open(style, "r") as f:
            self.setStyleSheet(f.read())

    def connectButton(self):
        self.ui.detailRun.setMinimum(0)
        self.ui.detailRun.setMaximum(9)
        self.ui.detailAll.setMinimum(0)
        self.ui.detailAll.setMaximum(9)

        self.ui.detailRun.valueChanged[int].connect(lambda x: self.ui.frameSpecter.changeRunDetail(x))
        self.ui.detailAll.valueChanged[int].connect(lambda x: self.ui.frameSpecter.changeAllDetail(x))

        self.ui.bRunSpecter.toggled.connect(lambda: self.ui.frameSpecter.changeMode(Specter.RUN_WAVE))
        self.ui.bAllSpecter.toggled.connect(lambda: self.ui.frameSpecter.changeMode(Specter.ALL_WAVE))
        self.ui.bAllSpecter.setChecked(True)
        self.ui.bSwitchOff.toggled.connect(self.ui.frameSpecter.removeWav)

    def showEvent(self, event):
        self.ui.frameSpecter.showWav()

    def closeEvent(self, event):
        self.ui.frameSpecter.removeWav()

    def changePos(self, x):
        self.ui.frameSpecter.changePos(x)

    def newWav(self, media):
        mediaFormat = re.search(r'[^\.]*$', media).group(0)
        if mediaFormat == 'wav':
            self.setButtonEnabled(True)
            self.ui.frameSpecter.showWav()
            self.ui.frameSpecter.newWav(media)
        else:
            self.setButtonEnabled(False)
            self.ui.frameSpecter.removeWav()

    def setButtonEnabled(self, enabled):
        self.ui.bRunSpecter.setEnabled(enabled)
        self.ui.bAllSpecter.setEnabled(enabled)
        self.ui.bSwitchOff.setEnabled(enabled)
