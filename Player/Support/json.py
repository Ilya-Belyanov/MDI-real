import json
import copy
import os

from PyQt5 import QtCore, QtWidgets


class Json:

    FORMAT = ".json"

    def savePlaylist(self, playlist):
        fileName = QtWidgets.QFileDialog.getSaveFileName(parent=None, caption="Save playlist",
                                                         directory=os.getcwd() + "/untitled", )[0]
        if fileName:
            if fileName[-(len(Json.FORMAT)):] == Json.FORMAT:
                self.save(fileName, playlist)
            else:
                self.checkFormat(fileName, playlist)

    def checkFormat(self, fileName, playlist):
        if self.exist(fileName + Json.FORMAT):
            self.overWrite(fileName + Json.FORMAT, playlist)
        else:
            self.save(fileName + Json.FORMAT, playlist)

    def overWrite(self, fileName, playlist):
        ok = self.showQuestionMessage(message='File already exist. Overwrite it?',
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
        fileName = QtWidgets.QFileDialog.getOpenFileUrl(parent=None,
                                                        caption="Choose song",
                                                        filter="Available Playlists (*" + Json.FORMAT + ")")[0]
        fileName = fileName.toString().replace('file:///', '')
        if fileName:
            playlist = self.load(fileName)
            return self.checkDeleted(playlist)

    def checkDeleted(self, playlist):
        copyPlaylist = copy.deepcopy(playlist)
        for name in playlist.keys():
            for audio in playlist[name]:
                if not self.exist(audio):
                    copyPlaylist[name].remove(audio)
        return copyPlaylist

    @staticmethod
    def load(fileName):
        with open(fileName) as f:
            return json.load(f)

    @staticmethod
    def exist(file):
        direct = QtCore.QDir()
        return direct.exists(file)

    @staticmethod
    def showQuestionMessage(message, title):
        ok = QtWidgets.QMessageBox(text=message)
        ok.setWindowTitle(title)
        ok.setStandardButtons(QtWidgets.QMessageBox.Save | QtWidgets.QMessageBox.Cancel)
        ok.setDefaultButton(QtWidgets.QMessageBox.Save)
        result = ok.exec()
        return result == QtWidgets.QMessageBox.Save
