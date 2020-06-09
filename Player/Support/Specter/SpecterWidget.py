from PyQt5 import QtCore, QtGui, QtWidgets

from .SpecterFrame.SpecterFrame import SpecterFrame


class Ui_Specter(object):
    def setupUi(self, Specter):
        Specter.setObjectName("Specter")
        Specter.resize(722, 400)
        Specter.setMaximumSize(QtCore.QSize(800, 400))
        self.gridLayout = QtWidgets.QGridLayout(Specter)
        self.gridLayout.setObjectName("gridLayout")
        self.frameSpecter = SpecterFrame(Specter)
        self.frameSpecter.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameSpecter.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameSpecter.setObjectName("frameSpecter")
        self.gridLayout.addWidget(self.frameSpecter, 0, 0, 1, 1)
        self.specterPanel = QtWidgets.QGroupBox(Specter)
        self.specterPanel.setMaximumSize(QtCore.QSize(16777215, 60))
        self.specterPanel.setObjectName("specterPanel")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.specterPanel)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.detailRun = QtWidgets.QSpinBox(self.specterPanel)
        self.detailRun.setMaximumSize(QtCore.QSize(50, 16777215))
        self.detailRun.setObjectName("detailRun")
        self.horizontalLayout.addWidget(self.detailRun)
        self.bRunSpecter = QtWidgets.QRadioButton(self.specterPanel)
        self.bRunSpecter.setObjectName("bRunSpecter")
        self.horizontalLayout.addWidget(self.bRunSpecter)
        self.detailAll = QtWidgets.QSpinBox(self.specterPanel)
        self.detailAll.setMaximumSize(QtCore.QSize(50, 16777215))
        self.detailAll.setObjectName("detailAll")
        self.horizontalLayout.addWidget(self.detailAll)
        self.bAllSpecter = QtWidgets.QRadioButton(self.specterPanel)
        self.bAllSpecter.setObjectName("bAllSpecter")
        self.horizontalLayout.addWidget(self.bAllSpecter)
        self.bSwitchOff = QtWidgets.QRadioButton(self.specterPanel)
        self.bSwitchOff.setObjectName("bSwitchOff")
        self.horizontalLayout.addWidget(self.bSwitchOff)
        self.gridLayout.addWidget(self.specterPanel, 1, 0, 1, 1)

        self.retranslateUi(Specter)
        QtCore.QMetaObject.connectSlotsByName(Specter)

    def retranslateUi(self, Specter):
        _translate = QtCore.QCoreApplication.translate
        Specter.setWindowTitle(_translate("Specter", "Form"))
        self.specterPanel.setTitle(_translate("Specter", "Specter Panel"))
        self.bRunSpecter.setText(_translate("Specter", "Run Specter"))
        self.bAllSpecter.setText(_translate("Specter", "All Specter"))
        self.bSwitchOff.setText(_translate("Specter", "Switch off"))
