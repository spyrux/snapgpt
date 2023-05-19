import tkinter as tk
import numpy as np
import cv2
from PIL import ImageGrab
from PyQt6 import QtWidgets, QtCore, QtGui
import menu
from PyQt6.QtGui import QPixmap, QMouseEvent

from PyQt6.QtCore import Qt


class ClickablePixMap(QtWidgets.QLabel):
    def __init__(self, size, pixmap):
        super().__init__()
        self.setPixmap(pixmap)
        self.setScaledContents(True)
        self.setFixedSize(size)

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.expand()

    def expand(self):
        expanded_window = QtWidgets.QMainWindow()
        expanded_window.setWindowTitle("Expanded Pixmap")
        expanded_window.resize(800, 600)

        central_widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(central_widget)
        expanded_pixmap = QtWidgets.QLabel()
        expanded_pixmap.setPixmap(self.pixmap())
        expanded_pixmap.setScaledContents(True)
        layout.addWidget(expanded_pixmap)

        expanded_window.setCentralWidget(central_widget)
        expanded_window.show()

class ViewWidget(QtWidgets.QWidget):

    def __init__(self, pixmaps, parent = None):
        super(ViewWidget, self).__init__()
        parent = parent
        self.pixmaps = pixmaps


    
    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        for i, pixmap in enumerate(self.pixmaps):
            y = i//3
            x = i%3
            height = 200
            width = 200
            border = 10
            p = QtGui.QPixmap(pixmap).scaled(width,height, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
            painter.drawPixmap(x*width + border, y*height + border, p)



