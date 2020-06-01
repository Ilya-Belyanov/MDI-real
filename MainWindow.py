# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PlayerWidget import Ui_Player
from RecordWidget import Ui_RecordWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 735)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")

        self.Player = QtWidgets.QWidget()
        self.Player.setObjectName("Player")
        self.uiPlayer = Ui_Player()
        self.uiPlayer.setupUi(self.Player)
        self.tabWidget.addTab(self.Player, "")

        self.Record = QtWidgets.QWidget()
        self.Record.setObjectName("Record")
        self.uiRecord = Ui_RecordWidget()
        self.uiRecord.setupUi(self.Record)
        self.tabWidget.addTab(self.Record, "")

        self.horizontalLayout_2.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuAudio = QtWidgets.QMenu(self.menubar)
        self.menuAudio.setObjectName("menuAudio")
        self.menuConvert_to = QtWidgets.QMenu(self.menuAudio)
        self.menuConvert_to.setObjectName("menuConvert_to")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_wav = QtWidgets.QAction(MainWindow)
        self.action_wav.setObjectName("action_wav")
        self.actionShow_specter = QtWidgets.QAction(MainWindow)
        self.actionShow_specter.setObjectName("actionShow_specter")
        self.actionShow_frequency = QtWidgets.QAction(MainWindow)
        self.actionShow_frequency.setObjectName("actionShow_frequency")
        self.actionStyle = QtWidgets.QAction(MainWindow)
        self.actionStyle.setObjectName("actionStyle")
        self.action_mp3 = QtWidgets.QAction(MainWindow)
        self.action_mp3.setObjectName("action_mp3")
        self.menuConvert_to.addAction(self.action_wav)
        self.menuConvert_to.addAction(self.action_mp3)
        self.menuAudio.addAction(self.menuConvert_to.menuAction())
        self.menuAudio.addSeparator()
        self.menuAudio.addAction(self.actionShow_specter)
        self.menuAudio.addAction(self.actionShow_frequency)
        self.menuSettings.addAction(self.actionStyle)
        self.menubar.addAction(self.menuAudio.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Player), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Record), _translate("MainWindow", "Tab 2"))
        self.menuAudio.setTitle(_translate("MainWindow", "Audio"))
        self.menuConvert_to.setTitle(_translate("MainWindow", "Convert to"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.action_wav.setText(_translate("MainWindow", ".wav"))
        self.actionShow_specter.setText(_translate("MainWindow", "Show specter"))
        self.actionShow_frequency.setText(_translate("MainWindow", "Show frequency"))
        self.actionStyle.setText(_translate("MainWindow", "Style"))
        self.action_mp3.setText(_translate("MainWindow", ".mp3"))
