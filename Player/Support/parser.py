import os


class Parser:

    def seekAudio(self, directory, formats: list, audio=None):
        if audio is None:
            audio = []
        for name in os.listdir(directory):
            if os.path.isdir(directory + '/' + name):
                self.seekAudio(directory + '/' + name, formats, audio)
            for form in formats:
                if form == name[-len(form):]:
                    audio.append(directory + '/' + name)
        return audio

