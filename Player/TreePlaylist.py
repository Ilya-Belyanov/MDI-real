import re

from TreeItem.variationItem import AudioItem
from TreeItem.standartTree import StandardTree
from .Support.signallers import TreeSignaller


class TreePlaylist(StandardTree):

    def __init__(self, tree):
        super().__init__(tree)
        self.signaler = TreeSignaller()
        self.backlightID = 0

    def checkMenu(self, index, menu):
        if self.rootNode.rowCount() != 0:
            menu.addAction('Delete').triggered.connect(lambda: self.deleteSong(index))

    def deleteSong(self, index):
        self.rootNode.removeRow(index.row())
        self.setUpperAudio(index)
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

    def oneClickedEvent(self):
        __index = self.tree.selectionModel().currentIndex()
        self.signaler.changeSong(__index.row())

    def clearRoot(self):
        self.model.clear()
        self.rootNode = self.model.invisibleRootItem()
        self.backlightID = 0

    def backlightCurrent(self, id):
        if self.backlightID < self.rootNode.rowCount():
            self.rootNode.child(self.backlightID).setStandardColor()
        self.rootNode.child(id).setActiveColor()
        self.backlightID = id
        self.tree.scrollTo(self.model.indexFromItem(self.rootNode.child(self.backlightID)))


