import re

from PyQt5 import QtWidgets

from TreeItem.variationItem import StandardItem
from TreeItem.standartTree import StandardTree
from .dataRecords import Data


class Records(StandardTree):
    def __init__(self, ui, tracks):
        super().__init__(ui.treeRecords)
        self.lbCurrentRecord = ui.lbCurrentRecord
        self.tracks = tracks
        self.data = Data()

        self.root = StandardItem(text="Records")
        self.rootNode.appendRow(self.root)

    def oneClickedEvent(self):
        __index = self.tree.selectionModel().currentIndex()
        __record = __index.data()
        if __index.parent().isValid() and self.lbCurrentRecord.text() != __record:
            self.setCurrentRecord(__record)

    def setCurrentRecord(self, record):
        self.lbCurrentRecord.setText(record)
        self.tracks.changeTree(self.data.returnItems(record))

    def checkMenu(self, index, menu):
        if index.parent().isValid():
            self.openMenuChild(index, menu)
        else:
            self.openMenuFather(index, menu)

    def openMenuFather(self, index, menu):
        menu.addAction('Add Record').triggered.connect(self.addRecord)

    def addRecord(self):
        name, ok = QtWidgets.QInputDialog.getText(self.tree,
                                                  "Choice name", "Enter name of the playlist",
                                                  text='')
        if ok:
            name = str(self.root.rowCount() + 1) + ': ' + name
            self.data.createClearParent(name)
            self.root.appendRow(
                StandardItem(text=name))
            self.tree.expandAll()

    def openMenuChild(self, index, menu):
        menu.addAction('Add track').triggered.connect(lambda: self.addTrack(index))
        menu.addAction('Rename').triggered.connect(lambda: self.renamePlaylist(index))

    def addTrack(self, index):
        name, ok = QtWidgets.QInputDialog.getText(self.tree,
                                                  "Choice name", "Enter name of the playlist",
                                                  text='')
        if ok:
            name = str(len(self.tracks) + 1) + ': ' + name
            self.data.addItems(index.data(), name)
            self.tracks.addTrack(name)

    def renamePlaylist(self, index):
        name, ok = QtWidgets.QInputDialog.getText(self.tree,
                                                  "Choice name", "Enter name of the playlist",
                                                  text=re.search(r'[^: ]*$', index.data()).group(0))

        if ok and name != "":
            newName = str(index.row() + 1) + ': ' + name
            oldName = self.model.itemFromIndex(index).text()
            self.renameCurrentRecord(newName, oldName)
            self.renamePlaylistInData(newName, oldName)
            self.model.itemFromIndex(index).setText(newName)

    def renameCurrentRecord(self, newName, oldName):
        if self.tree.selectionModel().currentIndex().data() == oldName:
            self.lbCurrentRecord.setText(newName)

    def renamePlaylistInData(self, newName, oldName):
        if newName != oldName:
            self.data.renameParent(newName, oldName)