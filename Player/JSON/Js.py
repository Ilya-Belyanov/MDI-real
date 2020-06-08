import json
import copy

from Player.Parser.parser import Parser


class Js:
    def __init__(self):
        self.parser = Parser()

    def savePlaylist(self, playlist):
        fileName = self.parser.saveFile()
        if fileName:
            if self.parser.existFile(fileName):
                self.save(fileName, playlist)
            elif self.parser.existFile(fileName + ".json"):
                self.overWrite(fileName + ".json", playlist)
            else:
                self.save(fileName + ".json", playlist)

    def overWrite(self, fileName, playlist):
        ok = self.parser.showQuestionMessage(message='File already exist. Overwrite it?',
                                             title='Save Playlists')
        if ok:
            self.save(fileName, playlist)
        else:
            self.savePlaylist(playlist)

    @staticmethod
    def save(file, playlist):
        with open(file, 'w') as f:
            json.dump(playlist, f)

    def loadPlaylist(self):
        fileName = self.parser.openFile(filt="Available Playlists (*.json)")
        if fileName:
            playlist = self.load(fileName)
            return self.checkDeleted(playlist)
        return None

    def checkDeleted(self, playlist):
        copyPlaylist = copy.deepcopy(playlist)
        for name in playlist.keys():
            for audio in playlist[name]:
                if not self.parser.existFile(audio):
                    copyPlaylist[name].remove(audio)
        return copyPlaylist

    @staticmethod
    def load(fileName):
        with open(fileName) as f:
            return json.load(f)
