import os

from PyQt5 import QtCore, QtWidgets


class Parser:

    @staticmethod
    def inputData(widget, title, text, startText=''):
        name, ok = QtWidgets.QInputDialog.getText(widget,
                                                  title, text,
                                                  text=startText)
        return name, ok

    @staticmethod
    def choiceColor():
        return QtWidgets.QColorDialog.getColor()

    @staticmethod
    def choiceDirectory(widget):
        directory = QtWidgets.QFileDialog.getExistingDirectory(
            widget,
            "Выбрать папку с музыкой"
            #os.getcwd(),
            #QtWidgets.QFileDialog.ShowDirsOnly
        )
        return directory

    @staticmethod
    def saveFile():
        fileName = QtWidgets.QFileDialog.getSaveFileName(parent=None, caption="Save playlist",
                                               directory=os.getcwd()+"/untitled",)[0]

        return fileName

    @staticmethod
    def openFile(filt):
        song = QtWidgets.QFileDialog.getOpenFileUrl(parent=None,
                                                         caption="Choose song",
                                                         filter=filt)[0]
        return song.toString().replace('file:///', '')

    def seekAudio(self, directory, formats: list, audio: list):
        for name in os.listdir(directory):
            if os.path.isdir(directory + '/' + name):
                self.seekAudio(directory + '/' + name, formats, audio)
            for form in formats:
                if form == name[-len(form):]:
                    audio.append(directory + '/' + name)
        return audio

    @staticmethod
    def existFile(file):
        dir = QtCore.QDir()
        return dir.exists(file)

    @staticmethod
    def showQuestionMessage(message, title):
        ok = QtWidgets.QMessageBox(text=message)
        ok.setWindowTitle(title)
        ok.setStandardButtons(QtWidgets.QMessageBox.Save | QtWidgets.QMessageBox.Cancel)
        ok.setDefaultButton(QtWidgets.QMessageBox.Save)
        result = ok.exec()
        if result == QtWidgets.QMessageBox.Save:
            return True
        else:
            return False

    @staticmethod
    def showMessage(message, title):
        dialog = QtWidgets.QMessageBox(text=message)
        dialog.setWindowTitle(title)
        dialog.exec()