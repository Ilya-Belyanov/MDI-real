

class PlaylistsData:
    def __init__(self):
        self.__playlists = dict()

    def deleteSong(self, playlist, id):
        self.__playlists[playlist].pop(id)

    def deletePlaylist(self, playlist):
        return self.__playlists.pop(playlist, None)

    def returnAudios(self, playlist):
        return self.__playlists[playlist]

    def createClearPlaylist(self, playlist):
        self.__playlists[playlist] = []

    def createPlaylist(self, playlist, audios: list):
        self.__playlists[playlist] = audios

    def expandPlaylists(self, playlist, audios: list):
        self.__playlists[playlist] += audios

    def renamePlaylist(self, newName, oldName):
        save = self.__playlists.copy()
        self.clear()
        for key in save.keys():
            if key == oldName:
                self.__playlists[newName] = save[oldName].copy()
            else:
                self.__playlists[key] = save[key].copy()

    def clear(self):
        self.__playlists.clear()

    @property
    def playlists(self):
        return self.__playlists

    @playlists.setter
    def playlist(self, json):
        self.__playlists = json