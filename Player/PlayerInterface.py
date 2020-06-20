import time

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtMultimedia import *

from .Support.Specter.SpecterInterface import SpecterInterface
from .Support.Converter.converter import Converter
from .playlists import Playlists
from .Support.json import Json


class PlayerInterface(QtWidgets.QMainWindow):

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

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.updatePositionSpecter)
        self.timer.start(200)

        self.specter = SpecterInterface()
        self.converter = Converter()
        self.json = Json()

        self.modeButton = QtWidgets.QButtonGroup()
        self.connectModePanel()
        self.connectDownPanel()
        self.connectPositionPanel()
        self.connectJSONButton()

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

    def connectJSONButton(self):
        self.ui.savePlaylists.clicked.connect(self.savePlaylist)
        self.ui.loadPlaylists.clicked.connect(self.loadPlaylist)

    def setStartPositionPanel(self, state):
        if state == QMediaPlayer.LoadedMedia or state == QMediaPlayer.BufferedMedia:
            self.ui.slPosition.setValue(0)
            self.ui.slPosition.setMaximum(self.player.duration())
            self.ui.lPosition.setText(time.strftime('%M:%S', time.localtime(self.player.position() / 1000)))
            self.ui.lDuratio.setText(time.strftime('%M:%S', time.localtime(self.player.duration() / 1000)))
            print(self.player.duration())
            self.updateMediaSpecter()

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

    def convertTo(self, format):
        if self.player.getCurrentMedia():
            self.converter.convertTo(self.player.getCurrentMedia(), format)

    def showSpecter(self):
        if self.player.getCurrentMedia():
            self.specter.show()
            self.specter.newWav(self.player.getCurrentMedia())

    def updateMediaSpecter(self):
        if self.specter.isVisible():
            self.specter.newWav(self.player.getCurrentMedia())

    def updatePositionSpecter(self):
        if self.specter.isVisible():
            self.specter.changePos(self.player.position())

    def savePlaylist(self):
        self.json.savePlaylist(self.treePlaylists.dataPlaylist())

    def loadPlaylist(self):
        self.treePlaylists.loadPlaylists(self.json.loadPlaylist())