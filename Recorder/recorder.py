from PyQt5 import QtCore
from PyQt5.QtMultimedia import *


class Recorder:
    def __init__(self):
        self.format = QAudioFormat()
        self.format.setSampleRate(8000)
        self.format.setChannelCount(1)
        self.format.setSampleSize(16)
        self.format.setCodec("audio/pcm")
        self.format.setByteOrder(QAudioFormat.LittleEndian)
        self.format.setSampleType(QAudioFormat.UnSignedInt)

        self._audioIn = QAudioInput(self.format)
        self._audioOut = []

    def record(self, buffer):
        if buffer.isOpen():
            bytes = QtCore.QByteArray()
            buffer.setBuffer(bytes)
        buffer.open(QtCore.QIODevice.WriteOnly | QtCore.QIODevice.Truncate)
        self._audioIn.start(buffer)

    def stopRecord(self):
        self._audioIn.stop()

    def playAll(self, buffers):
        self._audioOut.clear()
        for buffer in buffers.keys():
            audioOut = QAudioOutput(self.format)
            self._audioOut.append(audioOut)
            buffers[buffer].open(QtCore.QIODevice.ReadOnly)
            self._audioOut[-1].start(buffers[buffer])

    def stopPlayAll(self):
        for i in range(len(self._audioOut)):
            self._audioOut[i].stop()


