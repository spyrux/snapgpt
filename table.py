import tkinter as tk
import numpy as np
import cv2
from PIL import ImageGrab
from PyQt6 import QtWidgets, QtCore, QtGui
import menu

from PyQt6.QtCore import Qt

import snipview
import chat


class TableWidget(QtWidgets.QWidget):


    def __init__(self, viewWidget, parent = None):
        super(QtWidgets.QWidget, self).__init__()
        self.layout = QtWidgets.QVBoxLayout(self)
        self.parent = parent

        self.tabs = QtWidgets.QTabWidget()
        self.tab1 = chat.ChatWidget()
        self.tab2 = QtWidgets.QScrollArea()
        self.tab2.setWidget(viewWidget)
        self.tab2.setWidgetResizable(True)
        viewWidget.show()
        
        self.tabs.addTab(self.tab1, "GPT Chat")
        self.tabs.addTab(self.tab2, "View Snips")
        layout1 = QtWidgets.QVBoxLayout()
        layout2 = QtWidgets.QVBoxLayout()
        self.tab1.setLayout(layout1)
        self.tab2.setLayout(layout2)
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)