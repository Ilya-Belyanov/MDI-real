from PyQt5.Qt import QStandardItem
from PyQt5.QtGui import QColor, QFont
from PyQt5 import QtCore


class StandardItem(QStandardItem):
    def __init__(self, text='', font_size=12, edit=False, bold=False, color_text=QColor(255, 255, 255),
                 color_back=QColor(126, 7, 169)):
        super().__init__()
        font = QFont('Open Sans', font_size)
        font.setBold(bold)
        self.setEditable(edit)
        self.setForeground(color_text)
        self.setBackground(color_back)
        self.setText(text)
        self.setFont(font)


class AudioItem(StandardItem):
    def __init__(self, text='', font_size=9, edit=False, bold=False, color_text=QColor(255, 255, 255),
                 color_back=QColor(49, 54, 59)):
        super().__init__(text, font_size, edit, bold, color_text,
                         color_back)
        self.setSizeHint(QtCore.QSize(0, 50))

    def setStandardColor(self):
        self.setForeground(QColor(255, 255, 255))
        self.setBackground(QColor(49, 54, 59))

    def setActiveColor(self):
        self.setForeground(QColor(255, 214, 1))
        self.setBackground(QColor(129, 6, 168))