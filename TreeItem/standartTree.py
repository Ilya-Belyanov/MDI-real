from abc import ABC, abstractmethod

from PyQt5.Qt import QStandardItemModel
from PyQt5 import QtWidgets, QtCore


class StandardTree(ABC):
    def __init__(self, tree):
        self.tree = tree

        self.model = QStandardItemModel()
        self.rootNode = self.model.invisibleRootItem()

        self.tree.setModel(self.model)
        self.tree.setHeaderHidden(True)
        self.tree.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)

        self.tree.clicked.connect(lambda: self.oneClickedEvent())
        self.tree.customContextMenuRequested.connect(self.openTreeMenu)

    @abstractmethod
    def oneClickedEvent(self):
        pass

    def openTreeMenu(self, point):
        __index = self.tree.selectionModel().currentIndex()
        menu = QtWidgets.QMenu()
        with open("static/qcss/styleMenu.css", "r") as f:
            menu.setStyleSheet(f.read())
        self.checkMenu(__index, menu)
        menu.exec(self.tree.viewport().mapToGlobal(point))

    @abstractmethod
    def checkMenu(self, index, menu):
        pass

