import re

from TreeItem.variationItem import AudioItem
from .Support.signallers import TreeSignaller

from PyQt5.Qt import QStandardItemModel
from PyQt5 import QtWidgets, QtCore


class TreePlaylist:

    def __init__(self, tree):
        self.tree = tree
        self.model = QStandardItemModel()
        self.rootNode = self.model.invisibleRootItem()
        self.signaler = TreeSignaller()

        self.tree.setModel(self.model)
        self.tree.setHeaderHidden(True)
        self.tree.clicked.connect(lambda: self.setCurrentAudio())
        self.tree.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tree.customContextMenuRequested.connect(self.openTreeMenu)
        self.backlightID = 0

    def openTreeMenu(self, point):
        __index = self.tree.selectionModel().currentIndex()
        if self.rootNode.rowCount() != 0:
            menu = QtWidgets.QMenu()
            menu.addAction('Delete').triggered.connect(lambda: self.deleteSong(__index))
            menu.exec(self.tree.viewport().mapToGlobal(point))

    def deleteSong(self, index):
        self.setUpperAudio(index)
        self.rootNode.removeRow(index.row())
        self.reEnumeratePlaylist(index.row())
        self.signaler.deleteSong(index.row())

    def setUpperAudio(self, index):
        if index.row() < self.backlightID:
            self.backlightID -= 1

    def reEnumeratePlaylist(self, row):
        for i in range(self.rootNode.rowCount()):
            if i >= row:
                newName = str(i + 1) + ':' + re.search(r'[^:]*$', self.rootNode.child(i).text()).group(0)
                self.rootNode.child(i).setText(newName)

    def setPlaylist(self, audio):
        for song in audio:
            name = str(self.rootNode.rowCount() + 1) + ': ' + re.search(r'[^/]*$', song).group(0)
            item = AudioItem(text=name)
            self.rootNode.appendRow(item)

    def setCurrentAudio(self):
        __index = self.tree.selectionModel().currentIndex()
        self.signaler.changeSong(__index.row())

    def clearRoot(self):
        self.backlightID = 0
        self.model.clear()
        self.rootNode = self.model.invisibleRootItem()

    def backlightCurrent(self, id):
        self.rootNode.child(self.backlightID).setStandardColor()
        self.rootNode.child(id).setActiveColor()
        self.backlightID = id
        self.tree.scrollTo(self.model.indexFromItem(self.rootNode.child(self.backlightID)))


