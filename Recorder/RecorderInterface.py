from PyQt5 import QtWidgets

from .records import Records
from .tracks import Tracks


class RecorderInterface(QtWidgets.QMainWindow):
    def __init__(self, ui, parent=None):
        super().__init__(parent)
        self.ui = ui
        self.tracks = Tracks(self.ui.treeRecordParts)
        self.records = Records(self.ui, self.tracks)

        self.recordButtons = QtWidgets.QButtonGroup()
        self.connectDownPanel()

    def connectDownPanel(self):
        self.ui.btPlayAll.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_MediaPlay))
        self.ui.btStop.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_MediaStop))

        self.recordButtons.addButton(self.ui.btRecord, id=0)
        self.recordButtons.addButton(self.ui.btStopRecord, id=1)
        self.recordButtons.addButton(self.ui.btPlayAll, id=2)
        self.recordButtons.addButton(self.ui.btStop, id=3)
        self.recordButtons.buttonClicked.connect(self.setState)

    def setState(self, button):
        if self.tracks.isReady():
            self.tracks.setState(self.recordButtons.id(button))
            self.enable(self.recordButtons.id(button))

    def enable(self, id):
        for bt in self.recordButtons.buttons():
            if self.recordButtons.id(bt) == id:
                bt.setEnabled(False)
            else:
                bt.setEnabled(True)


