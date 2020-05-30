from MainWindow import *
from Player.PlayerInterface import PlayerInterface
from PyQt5 import QtWidgets


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.tabWidget.setTabText(0, "Player")
        self.ui.tabWidget.setTabText(1, "Record")
        self.setWindowTitle("MDI demo")
        self.playlists = PlayerInterface(self.ui.uiPlayer)
        self.loadStyleSheets()
        self.connectMenu()

    def loadStyleSheets(self):
        style = "static/style.css"
        with open(style, "r") as f:
            self.setStyleSheet(f.read())

    def connectMenu(self):
        self.ui.action_wav.triggered.connect(self.playlists.convertToWav)