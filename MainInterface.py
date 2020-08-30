from MainWindow import *
from Player.PlayerInterface import PlayerInterface
from Recorder.RecorderInterface import RecorderInterface


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.tabWidget.setTabText(0, "Player")
        self.ui.tabWidget.setTabText(1, "Record")
        self.setWindowTitle("MDI demo")
        self.playlists = PlayerInterface(self.ui.uiPlayer)
        self.recorder = RecorderInterface(self.ui.uiRecord)
        self.loadStyleSheets()
        self.connectMenu()

    def loadStyleSheets(self):
        style = "static/qcss/style.css"
        with open(style, "r") as f:
            self.setStyleSheet(f.read())

    def connectMenu(self):
        self.ui.action_wav.triggered.connect(lambda: self.playlists.convertTo('wav'))
        self.ui.action_mp3.triggered.connect(lambda: self.playlists.convertTo('mp3'))
        self.ui.actionShow_specter.triggered.connect(self.playlists.showSpecter)