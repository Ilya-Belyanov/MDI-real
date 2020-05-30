from PyQt5 import QtWidgets
import os


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
    def openSong(widget):
        song = QtWidgets.QFileDialog.getOpenFileUrl(parent=widget,
                                                         caption="Choose song",
                                                         filter="Available Sound (*.mp3 *.wav)")[0]
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
    def showMessage(message, title):
        dialog = QtWidgets.QMessageBox(text=message)
        dialog.setWindowTitle(title)
        dialog.exec()