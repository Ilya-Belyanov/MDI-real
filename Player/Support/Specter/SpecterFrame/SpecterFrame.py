from PyQt5 import QtCore, QtGui, QtWidgets
from .analysisWav import WaveAnalyzer
from .counter import CounterParameters


class SpecterFrame(QtWidgets.QFrame):

    def __init__(self, parent):
        super().__init__(parent)
        self.countPar = CounterParameters()

        self.wavExist = False
        self.modes = {1: self.drawAllChannels, 2: self.drawRunChannels}
        self.currentMode = 1
        self.pos = 0

    def resizeEvent(self, event):
        if self.wavExist:
            self.setRunSpecterParameters()
            self.setAllSpecterParameters()

    def newWav(self, directory):
        self.wav = WaveAnalyzer(directory)
        self.pos = 0
        self.setRunSpecterParameters()
        self.setAllSpecterParameters()

    def changeMode(self, mode):
        self.currentMode = mode
        self.showWav()
        self.update()

    def setRunSpecterParameters(self):
        self.runPer = self.countPar.getPerRunSpecter(self.wav.sampleRate, self.getWidth())
        self.runMashX = self.countPar.getXMashRunWave(self.getWidth(), self.wav.sampleRate)
        self.runStart = self.countPar.startLineRunWave(self.pos, self.wav.sampleRate)
        self.runEnd = self.countPar.endLineRunWave(self.pos, self.wav.sampleRate, self.wav.nSamples)
        self.runMashY = self.countPar.getYMash()

    def setAllSpecterParameters(self):
        self.allPer = self.countPar.getPerAllSpecter(self.wav.nSamples, self.getWidth())
        self.allMashX = self.countPar.getXMash(self.getWidth(), self.wav.nSamples)
        self.allMashY = self.countPar.getYMash()

    def showWav(self):
        self.wavExist = True

    def removeWav(self):
        self.wavExist = False
        self.update()

    def changeRunDetail(self, x):
        self.countPar.runDetail = x
        self.runPer = self.countPar.getPerRunSpecter(self.wav.sampleRate, self.getWidth())

    def changeAllDetail(self, x):
        self.countPar.allDetail = x
        self.allPer = self.countPar.getPerAllSpecter(self.wav.nSamples, self.getWidth())

    def changePos(self, duration):
        if self.wavExist:
            self.pos = self.countPar.durationToSample(duration, self.wav.sampleRate)
            self.update()

    def paintEvent(self, event):
        qp = QtGui.QPainter()
        qp.begin(self)
        if self.wavExist:
            self.modes[self.currentMode](qp)
        qp.end()

    def drawAllChannels(self, qp):
        color = QtGui.QColor.fromRgb(255, 214, 1, 255)
        qp.setPen(QtGui.QPen(color, 0.2, QtCore.Qt.SolidLine))
        for ch in range(self.wav.nChannels):
            qp.drawPolyline(self.checkFullCh(ch))
        self.drawLimitLine(qp)

    def drawRunChannels(self, qp):
        color = QtGui.QColor.fromRgb(255, 214, 1, 255)
        qp.setPen(QtGui.QPen(color, 0.5, QtCore.Qt.SolidLine))
        for ch in range(self.wav.nChannels):
            qp.drawPolyline(self.checkPartCh(ch))

    def checkFullCh(self, ch):
        __levelChannel = self.getLevelChannel(ch)
        points = [QtCore.QPoint(i * self.allMashX, - self.wav.getChannel(ch)[i] // self.allMashY + __levelChannel) for i in
                  range(0, self.pos, self.allPer)]
        return QtGui.QPolygon(points)

    def checkPartCh(self, ch):
        self.setRunSpecterParameters()
        __levelChannel = self.getLevelChannel(ch)
        points = []
        x = 0
        for i in range(self.runStart, self.runEnd, self.runPer):
            points.append(QtCore.QPoint(x * self.runMashX, -self.wav.getChannel(ch)[i] // self.runMashY + __levelChannel))
            x += self.runPer
        return QtGui.QPolygon(points)

    def getLevelChannel(self, ch):
        return self.getHeight() * (ch + 1) / (1 + self.wav.nChannels)

    def drawLimitLine(self, qp):
        color = QtGui.QColor.fromRgb(126, 7, 169, 255)
        qp.setPen(QtGui.QPen(color, 1, QtCore.Qt.SolidLine))
        qp.drawLine(self.pos * self.allMashX + 1, 0, self.pos * self.allMashX + 1, self.getWidth())

    def getHeight(self):
        return self.size().height()

    def getWidth(self):
        return self.size().width()