from PyQt5.Qt import QStandardItemModel
from PyQt5.QtGui import QColor
from PyQt5 import QtWidgets, QtCore
from TreeItem.variationItem import StandardItem
from .Parser.parser import Parser
from .player import Player
import re
from itertools import groupby


class Playlists:
    AVAILABLE_FORMAT = ['.mp3', '.wav']

    def __init__(self, tree, treePlaylist, label):
        self.lCurrentPlaylistName = label
        self.parser = Parser()
        self.root = StandardItem(text="Плейлисты")
        self.model = QStandardItemModel()
        self.rootNode = self.model.invisibleRootItem()
        self.playlists = dict()
        self.rootNode.appendRow(self.root)

        self.treePlaylists = tree
        self.player = Player(treePlaylist)
        self.player.signaler.deleteSongSignal.connect(self.deleteSong)
        self.treePlaylists.setModel(self.model)
        self.treePlaylists.setHeaderHidden(True)
        self.treePlaylists.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treePlaylists.clicked.connect(lambda: self.checkCurrentPlaylist())
        self.treePlaylists.customContextMenuRequested.connect(self.openTreeMenu)

    def deleteSong(self, id):
        self.playlists[self.lCurrentPlaylistName.text()].pop(id)

    def checkCurrentPlaylist(self):
        __index = self.treePlaylists.selectionModel().currentIndex()
        __playlist = __index.data()
        if __index.parent().isValid() and self.lCurrentPlaylistName.text() != __playlist:
            self.setCurrentPlaylist(__playlist)

    def setCurrentPlaylist(self, playlist):
        self.lCurrentPlaylistName.setText(playlist)
        self.player.setPlaylist(self.playlists[playlist])

    def openTreeMenu(self, point):
        __index = self.treePlaylists.selectionModel().currentIndex()
        menu = QtWidgets.QMenu()
        if __index.parent().isValid():
            self.openMenuChild(__index, menu)
        else:
            self.openMenuFather(__index, menu)
        menu.exec(self.treePlaylists.viewport().mapToGlobal(point))

    def openMenuFather(self, index, menu):
        menu.addAction('Add Playlist').triggered.connect(self.addPlaylist)
        menu.addSeparator()
        menu.addAction('Recolor Text').triggered.connect(lambda: self.changeTextColorItem(index))
        menu.addAction('Recolor Background').triggered.connect(lambda: self.changeBackColorPlaylist(index))

    def addPlaylist(self):
        name, ok = self.parser.inputData(self.treePlaylists,
                                         "Choice name", "Enter name of new playlist")
        if ok:
            name = str(self.root.rowCount() + 1) + ': ' + name
            self.root.appendRow(
                StandardItem(text=name))
            self.playlists[name] = []
            self.treePlaylists.expandAll()

    def changeTextColorItem(self, index):
        color = self.parser.choiceColor()

        if color.isValid():
            self.model.itemFromIndex(index).setForeground(color)

    def changeBackColorPlaylist(self, index):
        color = self.parser.choiceColor()

        if color.isValid():
            self.model.itemFromIndex(index).setBackground(color)

    def openMenuChild(self, index, menu):
        menu.addAction('Set playlist').triggered.connect(lambda: self.loadNewPlaylist(index))
        menu.addAction('Add playlist').triggered.connect(lambda: self.loadDopPlaylist(index))
        menu.addAction('Add song').triggered.connect(lambda: self.loadDopSong(index))
        menu.addSeparator()
        menu.addAction('Rename').triggered.connect(lambda: self.renamePlaylist(index))
        menu.addAction('Recolor Text').triggered.connect(lambda: self.changeTextColorItem(index))
        menu.addAction('Recolor Background').triggered.connect(lambda: self.changeBackColorPlaylist(index))
        menu.addSeparator()
        menu.addAction('Clear').triggered.connect(lambda: self.clearPlaylist(index))
        menu.addAction('Remove').triggered.connect(lambda: self.removePlaylist(index))

    def loadNewPlaylist(self, index):
        directory = self.parser.choiceDirectory(self.treePlaylists)
        if directory:
            self.playlists[index.data()] = self.parser.seekAudio(directory, Playlists.AVAILABLE_FORMAT, [])
            self.setCurrentPlaylist(index.data())

    def loadDopPlaylist(self, index):
        directory = self.parser.choiceDirectory(self.treePlaylists)
        if directory:
            self.playlists[index.data()] += self.parser.seekAudio(directory, Playlists.AVAILABLE_FORMAT, [])
            self.deleteRepeat(index.data())
            self.setCurrentPlaylist(index.data())

    def loadDopSong(self, index):
        song = self.parser.openSong(self.treePlaylists)
        if song:
            self.playlists[index.data()].append(song)
            self.deleteRepeat(index.data())
            self.setCurrentPlaylist(index.data())

    def deleteRepeat(self, key):
        oldList = self.playlists[key]
        self.playlists[key] = []
        for it in oldList:
            if self.playlists[key].count(it) == 0:
                self.playlists[key].append(it)

    def clearPlaylist(self, index):
        self.playlists[index.data()] = []
        self.setCurrentPlaylist(index.data())

    def renamePlaylist(self, index):
        name, ok = self.parser.inputData(self.treePlaylists,
                                         "Choice name", "Enter name of the playlist",
                                         startText=re.search(r'[^:]*$', index.data()).group(0))
        if ok and name != "":
            newName = str(index.row() + 1) + ': ' + name
            oldName = self.model.itemFromIndex(index).text()
            self.renamePlaylistInList(newName, oldName)
            self.model.itemFromIndex(index).setText(newName)

    def removePlaylist(self, index):
        __playlist = index.data()
        if self.lCurrentPlaylistName.text() == __playlist:
            self.setUpperPlaylist(index)
        self.removePlaylistInTree(index, __playlist)

    def setUpperPlaylist(self, index):
        self.player.removePlaylist()
        if index.row() != 0:
            __currentIndex = self.treePlaylists.indexAbove(index)
            __playlist = __currentIndex.data()
            self.setCurrentPlaylist(__playlist)

    def removePlaylistInTree(self, index, playlist):
        self.playlists.pop(playlist)
        self.root.removeRow(index.row())
        self.reEnumeratePlaylists()

    def reEnumeratePlaylists(self):
        for i in range(self.root.rowCount()):
            newName = str(i + 1) + ':' + re.search(r'[^:]*$', self.root.child(i).text()).group(0)
            oldName = self.root.child(i).text()
            self.renamePlaylistInList(newName, oldName)
            self.root.child(i).setText(newName)

    def renamePlaylistInList(self, newName, oldName):
        if self.lCurrentPlaylistName.text() == oldName:
            self.lCurrentPlaylistName.setText(newName)
        self.playlists[newName] = self.playlists.pop(oldName)
