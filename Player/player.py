from .treePlaylist import TreePlaylist
from .Signallers.signallers import PlayerSignaller
from PyQt5.QtMultimedia import *
from PyQt5 import QtCore
#import audio_metadata
import re


class Player:
    MODES = [QMediaPlaylist.Loop, QMediaPlaylist.Random, QMediaPlaylist.CurrentItemInLoop]

    def __init__(self, tree):
        self.audio = QMediaPlayer()
        self.playlist = QMediaPlaylist()
        self.signaler = PlayerSignaller()

        self.playlist.currentMediaChanged.connect(self.setNewName)

        self.currentPlaylist = TreePlaylist(tree)
        self.currentPlaylist.signaler.song.connect(self.changeCurrentSong)
        self.currentPlaylist.signaler.deleteSongSignal.connect(self.deleteSong)

    def setNewName(self, media):
        self.signaler.nameTrigger(re.search(r'[^/]*$', media.canonicalUrl().toString()).group(0))
        if self.playlist.mediaCount() != 0 and self.playlist.currentIndex() != -1:
            self.currentPlaylist.backlightCurrent(self.playlist.currentIndex())

    def setPlaylist(self, audio: list):
        self.removePlaylist()
        self.currentPlaylist.setPlaylist(audio)
        for song in audio:
            self.playlist.addMedia(QMediaContent(QtCore.QUrl(song)))
        self.audio.setPlaylist(self.playlist)
        self.signaler.playPauseEmit()

    def changeCurrentSong(self, id):
        if self.playlist.currentIndex() != id:
            self.playlist.setCurrentIndex(id)
            self.stop()
        self.pausePlay()

    def deleteSong(self, id):
        oldIndex = self.playlist.currentIndex()
        self.playlist.removeMedia(id)
        self.checkDelete(oldIndex)
        self.signaler.deleteSong(id)
        self.signaler.playPauseEmit()

    def checkDelete(self, oldIndex):
        if self.playlist.currentIndex() != oldIndex:
            self.playlist.setCurrentIndex(oldIndex - 1)

    def removePlaylist(self):
        self.currentPlaylist.clearRoot()
        self.playlist.clear()
        self.signaler.clearPanel()
        self.signaler.playPauseEmit()

    def pausePlay(self):
        if self.audio.state() == QMediaPlayer.PlayingState:
            self.audio.pause()
        else:
            self.audio.play()
        self.signaler.playPauseEmit()

    def playState(self):
        return self.audio.state() == QMediaPlayer.PlayingState

    def stop(self):
        self.audio.stop()
        self.signaler.playPauseEmit()

    def next(self):
        self.playlist.next()

    def previous(self):
        self.playlist.previous()

    def setMode(self, id):
        self.playlist.setPlaybackMode(Player.MODES[id])

    def getAudio(self):
        return self.audio

    def getCurrentMedia(self):
        return self.playlist.currentMedia().canonicalUrl().toString()

    def setPosition(self, pos):
        self.audio.setPosition(pos)

    def setVolume(self, vol):
        self.audio.setVolume(vol)

    def position(self):
        return self.audio.position()

    def duration(self):
        return self.audio.duration()

    def availableMetaData(self):
        return self.audio.availableMetaData()


