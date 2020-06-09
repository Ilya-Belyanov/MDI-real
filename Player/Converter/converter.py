import re

from PyQt5.QtCore import *
from PyQt5 import QtWidgets

from .formats import WaveFormat, MP3Format


class Converter:

    def convertTo(self, media, format):
        directory = QtWidgets.QFileDialog.getExistingDirectory(None, "Выбрать папку с музыкой")

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



