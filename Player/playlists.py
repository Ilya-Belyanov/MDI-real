import re

from PyQt5 import QtWidgets

from TreeItem.variationItem import StandardItem
from TreeItem.standartTree import StandardTree
from .Support.parser import Parser
from .player import Player
from .DataPlaylist import PlaylistsData


class Playlists(StandardTree):
    AVAILABLE_FORMAT = ['mp3', 'wav']

    def __init__(self, tree, treePlaylist, label):
        super().__init__(tree)
        self.lCurrentPlaylistName = label
        self.parser = Parser()
        self.dataAudio = PlaylistsData()

        self.root = StandardItem(text="Playlists")
        self.rootNode.appendRow(self.root)

        self.player = Player(treePlaylist)
        self.player.signaler.deleteSongSignal.connect(self.deleteSong)

    def deleteSong(self, id):
        self.dataAudio.deleteSong(self.lCurrentPlaylistName.text(), id)

    def oneClickedEvent(self):
        __index = self.tree.selectionModel().currentIndex()
        __playlist = __index.data()
        if __index.parent().isValid() and self.lCurrentPlaylistName.text() != __playlist:
            self.setCurrentPlaylist(__playlist)

    def setCurrentPlaylist(self, playlist):
        self.lCurrentPlaylistName.setText(playlist)
        self.player.setPlaylist(self.dataAudio.returnAudios(playlist))

    def checkMenu(self, index, menu):
        if index.parent().isValid():
            self.openMenuChild(index, menu)
        else:
            self.openMenuFather(index, menu)

    def openMenuFather(self, index, menu):
        menu.addAction('Add Playlist').triggered.connect(self.addPlaylist)
        menu.addSeparator()
        menu.addAction('Recolor Text').triggered.connect(lambda: self.changeTextColorItem(index))
        menu.addAction('Recolor Background').triggered.connect(lambda: self.changeBackColorPlaylist(index))
        menu.addSeparator()
        menu.addAction('Clear').triggered.connect(self.removeAllTree)

    def addPlaylist(self):
        name, ok = QtWidgets.QInputDialog.getText(self.tree,
                                                  "Choice name", "Enter name of the playlist",
                                                  text='')

        if ok:
            name = str(self.root.rowCount() + 1) + ': ' + name
            self.root.appendRow(
                StandardItem(text=name))
            self.dataAudio.createClearPlaylist(name)
            self.tree.expandAll()

    def changeTextColorItem(self, index):
        color = QtWidgets.QColorDialog.getColor()

        if color.isValid():
            self.model.itemFromIndex(index).setForeground(color)

    def changeBackColorPlaylist(self, index):
        color = QtWidgets.QColorDialog.getColor()

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
        directory = QtWidgets.QFileDialog.getExistingDirectory(None, "Выбрать папку с музыкой")
        if directory:
            self.dataAudio.createPlaylist(index.data(),
                                          self.parser.seekAudio(directory, Playlists.AVAILABLE_FORMAT))
            self.setCurrentPlaylist(index.data())

    def loadDopPlaylist(self, index):
        directory = QtWidgets.QFileDialog.getExistingDirectory(None, "Выбрать папку с музыкой")
        if directory:
            self.dataAudio.expandPlaylists(index.data(),
                                           self.parser.seekAudio(directory, Playlists.AVAILABLE_FORMAT))
            self.deleteRepeat(index.data())
            self.setCurrentPlaylist(index.data())

    def loadDopSong(self, index):
        song = QtWidgets.QFileDialog.getOpenFileUrl(parent=None,
                                                    caption="Choose song",
                                                    filter="Available Sound (*.mp3 *.wav)")[0]
        song = song.toString().replace('file:///', '')
        if song:
            self.dataAudio.expandPlaylists(index.data(), [song])
            self.deleteRepeat(index.data())
            self.setCurrentPlaylist(index.data())

    def deleteRepeat(self, playlist):
        oldList = self.dataAudio.returnAudios(playlist)
        self.dataAudio.createClearPlaylist(playlist)
        for audio in oldList:
            if self.dataAudio.returnAudios(playlist).count(audio) == 0:
                self.dataAudio.expandPlaylists(playlist, [audio])

    def clearPlaylist(self, index):
        self.dataAudio.createClearPlaylist(index.data())
        self.setCurrentPlaylist(index.data())

    def renamePlaylist(self, index):
        name, ok = QtWidgets.QInputDialog.getText(self.tree,
                                                  "Choice name", "Enter name of the playlist",
                                                  text=re.search(r'[^: ]*$', index.data()).group(0))

        if ok and name != "":
            newName = str(index.row() + 1) + ': ' + name
            oldName = self.model.itemFromIndex(index).text()
            self.renamePlaylistInData(newName, oldName)
            self.model.itemFromIndex(index).setText(newName)

    def removePlaylist(self, index):
        if self.lCurrentPlaylistName.text() == index.data():
            self.setUpperPlaylist(index)
        self.removePlaylistInTree(index, index.data())

    def setUpperPlaylist(self, index):
        self.deleteCurrentPlaylist()
        if index.row() != 0:
            __currentIndex = self.tree.indexAbove(index)
            self.setCurrentPlaylist(__currentIndex.data())

    def removePlaylistInTree(self, index, playlist):
        self.dataAudio.deletePlaylist(playlist)
        self.root.removeRow(index.row())
        self.reEnumeratePlaylists()

    def reEnumeratePlaylists(self):
        for i in range(self.root.rowCount()):
            newName = str(i + 1) + ':' + re.search(r'[^:]*$', self.root.child(i).text()).group(0)
            oldName = self.root.child(i).text()
            self.renameCurrentPlaylist(newName, oldName)
            self.renamePlaylistInData(newName, oldName)
            self.root.child(i).setText(newName)

    def renameCurrentPlaylist(self, newName, oldName):
        if self.lCurrentPlaylistName.text() == oldName:
            self.lCurrentPlaylistName.setText(newName)

    def renamePlaylistInData(self, newName, oldName):
        if newName != oldName:
            self.dataAudio.renamePlaylist(newName, oldName)

    def dataPlaylist(self):
        return self.dataAudio.playlists

    def loadPlaylists(self, playlists: dict):
        if playlists:
            self.removeAllTree()
            self.createNewPlaylists(playlists)

    def removeAllTree(self):
        self.deleteCurrentPlaylist()
        self.dataAudio.clear()
        for i in range(self.root.rowCount() - 1, -1, -1):
            self.root.removeRow(i)

    def deleteCurrentPlaylist(self):
        self.player.removePlaylist()
        self.lCurrentPlaylistName.setText(" ")

    def createNewPlaylists(self, playlists):
        self.dataAudio.playlist = playlists
        for name in playlists.keys():
            self.root.appendRow(StandardItem(text=name))
        self.tree.expandAll()
