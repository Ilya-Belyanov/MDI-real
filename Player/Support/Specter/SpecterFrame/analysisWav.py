import wave
import numpy as np


class WaveAnalyzer:

    def __init__(self, directory):
        self.newWav(directory)

    def newWav(self, directory):
        self.wav = wave.open(directory, mode="r")
        self.__channels = dict()
        self.__nChannels, self.__sampByte, self.__sampleRate, self.__nSamples, \
        self.__compType, self.__compName = self.wav.getparams()

        self.__samples = np.frombuffer(self.wav.readframes(self.__nSamples),
                                     dtype=self.getTypeByte(self.__sampByte))
        self.__saveCh()

    @staticmethod
    def getTypeByte(sampByte):
        types = {
            1: np.int8,
            2: np.int16,
            4: np.int32
        }
        return types[sampByte]

    def __saveCh(self):
        for ch in range(self.__nChannels):
            self.__channels[ch] = self.__samples[ch:: self.__nChannels]

    def lenChannel(self, ch):
        if ch >= self.__nChannels:
            return None
        return len(self.__channels[ch])

    def getChannel(self, ch):
        if ch >= self.__nChannels:
            return None
        return self.__channels[ch]

    def getSample(self, id):
        return self.__samples[id]

    @property
    def nChannels(self):
        return self.__nChannels

    @property
    def nSamples(self):
        return self.__nSamples

    @property
    def sampByte(self):
        return self.__sampByte

    @property
    def sampleRate(self):
        return self.__sampleRate

    @property
    def compType(self):
        return self.__compType

    @property
    def compName(self):
        return self.__compName
