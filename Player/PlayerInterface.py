from PyQt5 import QtWidgets, QtCore
from PyQt5.QtMultimedia import *
from .playlists import Playlists
from .converter import Converter
import time


class PlayerInterface(QtWidgets.QMainWindow):
    AVAILABLE_FORMAT = ['.mp3', '.wav']

    def __init__(self, ui, parent=None):
        super().__init__(parent)
        self.ui = ui
        self.treePlaylists = Playlists(self.ui.treePlaylists, self.ui.treePlaylist, self.ui.label)

        self.player = self.treePlaylists.player
        self.player.signaler.clear.connect(self.setEmptyPanel)
        self.player.signaler.playPause.connect(self.changeButtonText)
        self.player.signaler.nameSignal.connect(lambda name: self.ui.lName.setText(name))
        self.player.getAudio().mediaStatusChanged.connect(self.setStartPositionPanel)
        self.player.getAudio().positionChanged.connect(self.changePanelPosition)

        self.converter =  Converter()
        self.modeButton = QtWidgets.QButtonGroup()
        self.connectModePanel()
        self.connectDownPanel()
        self.connectPositionPanel()

    def connectModePanel(self):
        self.modeButton.addButton(self.ui.buttonCircleAll, id=0)
        self.modeButton.addButton(self.ui.buttonRandom, id=1)
        self.modeButton.addButton(self.ui.buttonLoopOne, id=2)
        self.modeButton.buttonClicked.connect(self.setMode)
        self.setMode(self.modeButton.button(0))

    def connectDownPanel(self):
        self.ui.bPlay.clicked.connect(self.player.pausePlay)
        self.ui.bPlay.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_MediaPlay))
        self.ui.bStop.clicked.connect(self.player.stop)
        self.ui.bStop.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_MediaStop))
        self.ui.bNext.clicked.connect(self.player.next)
        self.ui.bBack.clicked.connect(self.player.previous)

    def connectPositionPanel(self):
        self.ui.slPosition.setMinimum(0)
        self.ui.slPosition.sliderMoved[int].connect(lambda x: self.player.setPosition(x))
        self.ui.sliderVolume.setValue(100)
        self.ui.sliderVolume.sliderMoved[int].connect(lambda x: self.player.setVolume(x))

    def setStartPositionPanel(self, state):
        if state == QMediaPlayer.LoadedMedia or state == QMediaPlayer.BufferedMedia:
            self.ui.slPosition.setValue(0)
            self.ui.slPosition.setMaximum(self.player.duration())
            self.ui.lPosition.setText(time.strftime('%M:%S', time.localtime(self.player.position() / 1000)))
            self.ui.lDuratio.setText(time.strftime('%M:%S', time.localtime(self.player.duration() / 1000)))\


    def changePanelPosition(self):
        self.ui.slPosition.setValue(self.player.position())
        self.ui.lPosition.setText(time.strftime('%M:%S', time.localtime(self.player.position() / 1000)))

    def changeButtonText(self):
        if self.player.playState():
            self.ui.bPlay.setText('Pause')
            self.ui.bPlay.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_MediaPause))
        else:
            self.ui.bPlay.setText('Play')
            self.ui.bPlay.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_MediaPlay))

    def setMode(self, button):
        self.player.setMode(self.modeButton.id(button))
        for bt in self.modeButton.buttons():
            if bt == button:
                bt.setEnabled(False)
            else:
                bt.setEnabled(True)

    def setEmptyPanel(self):
        self.ui.lName.setText("")
        self.ui.lPosition.setText('00:00')
        self.ui.lDuratio.setText('00:00')
        self.ui.slPosition.setMaximum(0)

    def convertToWav(self):
        media = self.player.getCurrentMedia().canonicalUrl().toString()
        if media:
            self.converter.convertTo(media, 'wav')
