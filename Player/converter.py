from pydub import AudioSegment
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from .Parser.parser import Parser
from abc import ABC, abstractmethod
import re


class Converter:
    def __init__(self):
        self.parser = Parser()

    def convertTo(self, media, format):
        directory = self.parser.choiceDirectory(None)
        if directory:
            mediaFormat = self.checkFormat(media)
            mediaName = re.search(r'[^/]*$', media).group(0)[:-(len(mediaFormat) + 1)]
            song = Fabric.getSong(mediaFormat, media, mediaName)
            song.convertTo(format, directory)

    @staticmethod
    def checkFormat(media):
        return re.search(r'[^\.]*$', media).group(0)


class Fabric:
    FORMAT = ['mp3', 'wav']

    @staticmethod
    def getSong(format, path, name):
        if format == Fabric.FORMAT[1]:
            return WaveFormat(path, name)

        elif format == Fabric.FORMAT[0]:
            return MP3Format(path, name)


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
