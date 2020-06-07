import json

from Player.Parser.parser import Parser


class Js:
    def __init__(self):
        self.parser = Parser()

    def savePlaylist(self, playlist):
        fileName = self.parser.saveFile()
        if fileName:
            fileName += ".json"
            if self.parser.existFile(fileName):
                self.overWrite(fileName, playlist)
            else:
                self.save(fileName, playlist)

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
            with open(fileName) as f:
                return json.load(f)
        return None
