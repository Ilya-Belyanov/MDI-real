from PyQt5.QtCore import pyqtSignal, QObject


class PlayerSignaller(QObject):
    nameSignal = pyqtSignal(str)
    clear = pyqtSignal()
    playPause = pyqtSignal()
    deleteSongSignal = pyqtSignal(int)

    def nameTrigger(self, name):
        self.nameSignal.emit(name)

    def clearPanel(self):
        self.clear.emit()

    def playPauseEmit(self):
        self.playPause.emit()

    def deleteSong(self, id):
        self.deleteSongSignal.emit(id)


class TreeSignaller(QObject):
    song = pyqtSignal(int)
    deleteSongSignal = pyqtSignal(int)

    def changeSong(self, id):
        self.song.emit(id)

    def deleteSong(self, id):
        self.deleteSongSignal.emit(id)

