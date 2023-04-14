from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QLabel
from PyQt6.QtGui import QPixmap, QImage, QAction, QIcon
from PyQt6.QtCore import Qt

# Only needed for access to command line arguments
import sys

import snipping

# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.



class Menu(QMainWindow):


    default_title = "SnapGPT"

    def __init__(self, numpy_image = None, start_position =(300,300,350,250)):

        super().__init__()
        self.centralWidget = QLabel()
        self.centralWidget.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(self.centralWidget)

        self.setWindowIcon(QIcon('background.png'))
        
        self.title = Menu.default_title
        new_snip_action = QAction('New', self)
        new_snip_action.setShortcut('Ctrl+N')
        new_snip_action.setStatusTip('Snip!')
        new_snip_action.triggered.connect(self.new_image_window)


             # Save
        save_action = QAction('Save', self)
        save_action.setShortcut('Ctrl+S')
        save_action.setStatusTip('Save')
        save_action.triggered.connect(self.save_file)

        # Exit
        exit_window = QAction('Exit', self)
        exit_window.setShortcut('Ctrl+Q')
        exit_window.setStatusTip('Exit application')
        exit_window.triggered.connect(self.close)
        

        #add toolbar with actions
        self.toolbar = self.addToolBar('Toolbar')
        self.toolbar.addAction(new_snip_action)
        self.toolbar.addAction(save_action)
        self.toolbar.addAction(exit_window)

        if numpy_image is not None:
            
            self.image = self.convert_numpy_img_to_qpixmap(numpy_image)
            self.centralWidget.setPixmap(self.image)
        else:
            self.image = QPixmap("patrick.png")
            self.centralWidget.setPixmap(self.image)
             
        

        


        # self.snippingTool = snipping.SnippingWidget()
        self.setGeometry(*start_position)


        
        self.setWindowTitle(self.title)
        self.resize(self.image.width(), self.image.height() + self.toolbar.height())

    
        



        
        self.show()

    
    def save_file(self):
        file_path, name = QFileDialog.getSaveFileName(self, "Save file", self.title, "PNG Image file (*.png)")
        if file_path:
            self.image.save(file_path)

    
    
    
    def convert_numpy_img_to_qpixmap(np_img):
        height, width, channel = np_img.shape
        bytesPerLine = 3 * width
        return QPixmap(QImage(np_img.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped())
            

    def new_image_window(self):
            if self.snippingTool.background:
                 self.close()
            
            self.snippingTool.start()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainMenu = Menu()
    sys.exit(app.exec())
