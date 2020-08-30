from PyQt5.QtCore import pyqtSignal, QObject


class AbstractSignaler(QObject):
    deleteSongSignal = pyqtSignal(int)

    def deleteSong(self, id):
        self.deleteSongSignal.emit(id)


class PlayerSignaller(AbstractSignaler):
    nameSignal = pyqtSignal(str)
    clear = pyqtSignal()
    playPause = pyqtSignal()

    def nameTrigger(self, name):
        self.nameSignal.emit(name)

    def clearPanel(self):
        self.clear.emit()

    def playPauseEmit(self):
        self.playPause.emit()


class TreeSignaller(AbstractSignaler):
    song = pyqtSignal(int)

    def changeSong(self, id):
        self.song.emit(id)


