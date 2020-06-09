

class CounterParameters:

    def __init__(self):
        self.lengthRunChannel = 1  # сек
        self.__runDetail = 1
        self.__allDetail = 1

    def getPerAllSpecter(self, rate, width):
        return int(rate / (width * self.allDetail))

    def getPerRunSpecter(self, rate, width):
        return int(rate / (width * self.runDetail)) * 4

    def startLineRunWave(self, pos, rate):
        start = int(pos - (self.lengthRunChannel / 2) * rate)
        if start < 0: return 0
        return start

    def endLineRunWave(self, pos, rate, max):
        end = int(pos + (self.lengthRunChannel / 2) * rate)
        if end >= max: return max - 1
        return end

    @property
    def runDetail(self):
        return self.__runDetail

    @runDetail.setter
    def runDetail(self, x):
        self.__runDetail = x + 1

    @property
    def allDetail(self):
        return self.__allDetail

    @allDetail.setter
    def allDetail(self, x):
        self.__allDetail = x + 1

    @staticmethod
    def getXMash(width, amountSamples):
        return width / amountSamples

    def getXMashRunWave(self, width, amountSamples):
        return width / amountSamples * self.lengthRunChannel

    @staticmethod
    def getYMash():
        return 600

    @staticmethod
    def durationToSample(duration, rate):
        return int((duration / 1000) * rate)