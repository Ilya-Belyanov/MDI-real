import re

from PyQt5 import QtWidgets

from TreeItem.variationItem import AudioItem
from TreeItem.standartTree import StandardTree

from .recorder import Recorder


class Tracks(StandardTree):
    RECORD_STATE = 0
    NOT_RECORD_STATE = 1
    PLAY_ALL_STATE = 2
    STOP_PLAY_ALL_STATE = 3

    def __init__(self, tree):
        super().__init__(tree)
        self.recorder = Recorder()
        self.tracks = dict()
        self.currentTrack = -1

    def __len__(self):
        return len(self.tracks)

    def addTrack(self, name):
        print(self.tracks)
        self.rootNode.appendRow(
            AudioItem(text=name))

    def oneClickedEvent(self):
        __index = self.tree.selectionModel().currentIndex()
        self.currentTrack = __index.data()

    def changeTree(self, records):
        self.clearRoot()
        self.tracks = records
        for track in self.tracks.keys():
            item = AudioItem(text=track)
            self.rootNode.appendRow(item)

    def checkMenu(self, index, menu):
        if self.rootNode.rowCount() != 0:
            menu.addAction('Rename').triggered.connect(lambda: self.renameTrack(index))
            menu.addAction('Save').triggered.connect(lambda: self.saveTrack(index))
            menu.addAction('Delete').triggered.connect(lambda: self.deleteTrack(index))

    def renameTrack(self, index):
        name, ok = QtWidgets.QInputDialog.getText(self.tree,
                                                  "Choice name", "Enter name of the playlist",
                                                  text=re.search(r'[^: ]*$', index.data()).group(0))

        if ok and name != "":
            newName = str(index.row() + 1) + ': ' + name
            oldName = self.model.itemFromIndex(index).text()
            self.changeData(newName, oldName)
            self.model.itemFromIndex(index).setText(newName)

    def changeData(self, newName, oldName):
        save = self.tracks.copy()
        self.tracks.clear()
        for key in save.keys():
            if key == oldName:
                self.tracks[newName] = save[oldName]
            else:
                self.tracks[key] = save[key]

    def saveTrack(self, index):
        pass

    def deleteTrack(self, index):
        pass

    def clearRoot(self):
        self.model.clear()
        self.rootNode = self.model.invisibleRootItem()
        self.currentTrack = -1

    def setState(self, state):
        if state == self.RECORD_STATE and self.currentTrack != -1:
            self.recorder.record(self.tracks[self.currentTrack])
        elif state == self.NOT_RECORD_STATE:
            self.recorder.stopRecord()
        elif state == self.PLAY_ALL_STATE:
            self.recorder.playAll(self.tracks)
        elif state == self.STOP_PLAY_ALL_STATE:
            self.recorder.stopPlayAll()

    def isReady(self):
        return self.currentTrack != -1
