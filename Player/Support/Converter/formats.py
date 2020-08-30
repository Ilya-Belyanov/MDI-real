from abc import ABC, abstractmethod
from pydub import AudioSegment

from PyQt5 import QtWidgets


class AbstractFormat(ABC):

    def __init__(self, path, name) -> None:
        self.path = path
        self.name = name

    @abstractmethod
    def convertTo(self, format, path) -> None:
        pass

    @abstractmethod
    def format(self) -> str:
        pass

    @staticmethod
    def showMessage(message, title):
        dialog = QtWidgets.QMessageBox(text=message)
        dialog.setWindowTitle(title)
        dialog.exec()


class MP3Format(AbstractFormat):

    def convertTo(self, format, path) -> None:
        if format != self.format():
            sound = AudioSegment.from_mp3(self.path)
            sound.export(path + '/' + self.name + '.' + format, format=format)
            self.showMessage(message="Conversion was successful in directory  <strong>" + path + '</strong>',
                             title='Convert to ' + format)
        else:
            self.showMessage(message='Error: convert <strong>' + format + ' to ' + format + '</strong>',
                             title='Convert to ' + format)

    def format(self) -> str:
        return "mp3"


class WaveFormat(AbstractFormat):

    def convertTo(self, format, path) -> None:
        if format != self.format():
            sound = AudioSegment.from_wav(self.path)
            sound.export(path + '/' + self.name + '.' + format, format=format)
            self.showMessage(message="Conversion was successful in directory  <strong>" + path + '</strong>',
                             title='Convert to ' + format)
        else:
            self.showMessage(message='Error: convert <strong>' + format + ' to ' + format + '</strong>',
                             title='Convert to ' + format)

    def format(self) -> str:
        return "wav"
