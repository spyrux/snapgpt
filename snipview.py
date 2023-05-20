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
        self.orignalWidth = pixmap.width()
        self.orignalHeight = pixmap.height()
        self.pixmap = pixmap
        self.setPixmap(pixmap)
        self.setScaledContents(True)
        self.title = "Untitled"
        
        self.expanded_window = None


    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.expand()

    def save_file(self):

        file_path, name = QtWidgets.QFileDialog.getSaveFileName(self, "Save file", self.title, "PNG Image file (*.png)")
        if file_path:
            image = QPixmap(self.pixmap)
            image.save(file_path)

    def expand(self):
        if self.expanded_window is None:
            self.expanded_window = QtWidgets.QMainWindow()
            self.expanded_window.setWindowTitle("Expanded Pixmap")
            self.expanded_window.resize(self.orignalWidth, self.orignalHeight)
            save_action = QtGui.QAction('Save', self)
            save_action.setShortcut('Ctrl+S')
            save_action.setStatusTip('Save')
            save_action.triggered.connect(self.save_file)

            self.expanded_window.toolbar = self.expanded_window.addToolBar('Toolbar')
            
            self.expanded_window.toolbar.addAction(save_action)

            central_widget = QtWidgets.QWidget()
            layout = QtWidgets.QVBoxLayout(central_widget)
            expanded_pixmap = QtWidgets.QLabel()
            expanded_pixmap.setPixmap(self.pixmap)
            expanded_pixmap.setScaledContents(True)
            layout.addWidget(expanded_pixmap)

            self.expanded_window.setCentralWidget(central_widget)

        self.expanded_window.show()






class ViewWidget(QtWidgets.QWidget):
    
    def __init__(self, pixmaps):
        super().__init__()
        self.pixmaps = pixmaps
        self.layout = QtWidgets.QGridLayout()
        for i, pixmap in enumerate(pixmaps):
                row = i // 3  # Adjust the number of columns as per your requirement
                col = i % 3  # Adjust the number of columns as per your requirement

                label = ClickablePixMap(200, pixmap)
                label.setScaledContents(True)

                self.layout.addWidget(label, row, col)
        self.setLayout(self.layout)
        
        

    def update_labels(self):
        # Clear the existing labels
        while self.layout.count():
            label = self.layout.takeAt(0).widget()
            label.deleteLater()


    def addlabel(self, pixmap):
        label = ClickablePixMap(200, pixmap)
        label.setScaledContents(True)
        number = len(self.pixmaps)
        row = (number - 1) // 3  
        col = (number -1) % 3 
        self.layout.addWidget(label, row, col)

    

        self.setLayout(self.layout)
    








