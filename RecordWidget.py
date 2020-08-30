# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RecordWidget.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RecordWidget(object):
    def setupUi(self, RecordWidget):
        RecordWidget.setObjectName("RecordWidget")
        RecordWidget.resize(631, 768)
        self.gridLayout_3 = QtWidgets.QGridLayout(RecordWidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.btStopRecord = QtWidgets.QPushButton(RecordWidget)
        self.btStopRecord.setObjectName("btStopRecord")
        self.horizontalLayout_7.addWidget(self.btStopRecord)
        self.btRecord = QtWidgets.QPushButton(RecordWidget)
        self.btRecord.setObjectName("btRecord")
        self.horizontalLayout_7.addWidget(self.btRecord)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.lbPosition = QtWidgets.QLabel(RecordWidget)
        self.lbPosition.setObjectName("lbPosition")
        self.horizontalLayout_16.addWidget(self.lbPosition)
        self.horizontalSlider_3 = QtWidgets.QSlider(RecordWidget)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.horizontalLayout_16.addWidget(self.horizontalSlider_3)
        self.lbDuration = QtWidgets.QLabel(RecordWidget)
        self.lbDuration.setObjectName("lbDuration")
        self.horizontalLayout_16.addWidget(self.lbDuration)
        self.verticalLayout_6.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem1)
        self.btStop = QtWidgets.QPushButton(RecordWidget)
        self.btStop.setObjectName("btStop")
        self.horizontalLayout_17.addWidget(self.btStop)
        self.btPlayAll = QtWidgets.QPushButton(RecordWidget)
        self.btPlayAll.setObjectName("btPlayAll")
        self.horizontalLayout_17.addWidget(self.btPlayAll)
        self.btPlayOne = QtWidgets.QPushButton(RecordWidget)
        self.btPlayOne.setObjectName("btPlayOne")
        self.horizontalLayout_17.addWidget(self.btPlayOne)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem2)
        self.verticalLayout_6.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_15.addLayout(self.verticalLayout_6)
        self.slVolume = QtWidgets.QSlider(RecordWidget)
        self.slVolume.setMaximumSize(QtCore.QSize(100, 100))
        self.slVolume.setOrientation(QtCore.Qt.Vertical)
        self.slVolume.setObjectName("slVolume")
        self.horizontalLayout_15.addWidget(self.slVolume)
        self.gridLayout_3.addLayout(self.horizontalLayout_15, 1, 0, 1, 2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.gridLayout.addLayout(self.horizontalLayout_18, 0, 0, 1, 1)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem3)
        self.lbCurrentRecord = QtWidgets.QLabel(RecordWidget)
        self.lbCurrentRecord.setMinimumSize(QtCore.QSize(200, 0))
        self.lbCurrentRecord.setStyleSheet("qproperty-alignment:AlignCenter;\n"
"")
        self.lbCurrentRecord.setObjectName("lbCurrentRecord")
        self.horizontalLayout_20.addWidget(self.lbCurrentRecord)
        self.horizontalLayout_19.addLayout(self.horizontalLayout_20)
        self.gridLayout.addLayout(self.horizontalLayout_19, 1, 1, 1, 1)
        self.treeRecords = QtWidgets.QTreeView(RecordWidget)
        self.treeRecords.setMinimumSize(QtCore.QSize(100, 0))
        self.treeRecords.setMaximumSize(QtCore.QSize(250, 16777215))
        self.treeRecords.setObjectName("treeRecords")
        self.gridLayout.addWidget(self.treeRecords, 2, 0, 1, 1)
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.bxInputDevice = QtWidgets.QComboBox(RecordWidget)
        self.bxInputDevice.setObjectName("bxInputDevice")
        self.horizontalLayout_22.addWidget(self.bxInputDevice)
        self.bxOutputDevice = QtWidgets.QComboBox(RecordWidget)
        self.bxOutputDevice.setObjectName("bxOutputDevice")
        self.horizontalLayout_22.addWidget(self.bxOutputDevice)
        self.gridLayout.addLayout(self.horizontalLayout_22, 1, 0, 1, 1)
        self.treeRecordParts = QtWidgets.QTreeView(RecordWidget)
        self.treeRecordParts.setObjectName("treeRecordParts")
        self.gridLayout.addWidget(self.treeRecordParts, 2, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 1, 1, 1)

        self.retranslateUi(RecordWidget)
        QtCore.QMetaObject.connectSlotsByName(RecordWidget)

    def retranslateUi(self, RecordWidget):
        _translate = QtCore.QCoreApplication.translate
        RecordWidget.setWindowTitle(_translate("RecordWidget", "Form"))
        self.btStopRecord.setText(_translate("RecordWidget", "Stop record"))
        self.btRecord.setText(_translate("RecordWidget", "Record"))
        self.lbPosition.setText(_translate("RecordWidget", "00:00"))
        self.lbDuration.setText(_translate("RecordWidget", "00:00"))
        self.btStop.setText(_translate("RecordWidget", "Stop"))
        self.btPlayAll.setText(_translate("RecordWidget", "PlayAll"))
        self.btPlayOne.setText(_translate("RecordWidget", "PlayDedicated"))
        self.lbCurrentRecord.setText(_translate("RecordWidget", "Current record"))
