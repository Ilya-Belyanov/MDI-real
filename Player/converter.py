from pydub import AudioSegment
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from abc import ABC, abstractmethod


class Converter:
    def convertTo(self, media, format):
        pass


class Fabric:
    MP3 = 'MPEG Audio Layer-3 (MP3)'
    WAV = 'Uncompressed PCM Audio'

    def getSong(self, metaData):
        if metaData.format == self.WAV:
            return WaveFormat(metaData.path, metaData.name)

        elif metaData.format == self.MP3:
            return MP3Format(metaData.path, metaData.name)


class AbstractFormat(ABC):

    def __init__(self, path, name) -> None:
        self.path = path
        self.name = name

    @abstractmethod
    def convertTo(self, format, path) -> None:
        pass

    @abstractmethod
    def format(self) -> None:
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
            sound.export(path + self.name + '.' + format, format=format)
            self.showMessage(message="Conversion was successful in directory  <strong>" + path + '</strong>',
                             title='Convert to ' + format)
        else:
            self.showMessage(message='Error: convert <strong>' + format + ' to ' + format + '</strong>',
                             title='Convert to ' + format)

    def format(self) -> str:
        return "mp3"


class WaveFormat(AbstractFormat):

    def convertTo(self, format, path) -> None:
        self.showMessage(message='Error: convert <strong>' + format + ' to ' + format + '</strong>',
                         title='Convert to Wav')

    def format(self) -> str:
        return "wav"

