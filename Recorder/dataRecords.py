from PyQt5 import QtCore


class Data:
    def __init__(self):
        self.__data = dict()

    def createClearParent(self, parent: str):
        self.__data[parent] = dict()

    def createParent(self, parent, items):
        self.__data[parent] = items

    def deleteItem(self, parent, id):
        self.__data[parent].pop(id)

    def deleteParent(self, parent):
        return self.__data.pop(parent, None)

    def returnItems(self, parent) -> dict:
        return self.__data[parent]

    def addItems(self, parent, item):
        buffer = QtCore.QBuffer()
        self.__data[parent][item] = buffer

    def renameParent(self, newName, oldName):
        save = self.__data.copy()
        self.clear()
        for key in save.keys():
            if key == oldName:
                self.__data[newName] = save[oldName].copy()
            else:
                self.__data[key] = save[key].copy()

    def clear(self):
        self.__data.clear()

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, json):
        self.__data = json