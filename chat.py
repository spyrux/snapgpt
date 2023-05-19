import tkinter as tk
import numpy as np
import cv2
from PIL import ImageGrab
from PyQt6 import QtWidgets, QtCore, QtGui
import menu

from PyQt6.QtCore import Qt



class ChatWidget(QtWidgets.QWidget):

    def __init__(self, parent = None):
        super(ChatWidget, self).__init__()
        parent = parent