from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QLabel
from PyQt6.QtGui import QPixmap, QImage, QAction, QIcon
from PyQt6.QtCore import Qt

# Only needed for access to command line arguments
import sys
import pdb
import snipping
import snipview
import table

#todo get ocr connect to openai, display chatbox, be able to type in chatbox and send request to api

class Menu(QMainWindow):


    default_title = "SnapGPT"

    def __init__(self,  numpy_image=None, start_position=(200, 200, 800, 600)):

        super().__init__()
        self.pixmaps = []
        self.viewWidget = snipview.ViewWidget(self.pixmaps)
        self.centralWidget = table.TableWidget(self.viewWidget)
        self.setCentralWidget(self.centralWidget)

        self.setWindowIcon(QIcon('background.png'))
        
        self.title = Menu.default_title
        self.setWindowTitle(self.title)

        
        
        new_snip_action = QAction('New', self)
        new_snip_action.setShortcut('Ctrl+N')
        new_snip_action.setStatusTip('Snip!')
        new_snip_action.triggered.connect(self.new_image_window)


        # Save
        save_action = QAction('Save', self)
        save_action.setShortcut('Ctrl+S')
        save_action.setStatusTip('Save')
        save_action.triggered.connect(self.save_file)
        # snips window 





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

    
             
        

        


        self.snippingTool = snipping.SnippingWidget()
        self.setGeometry(*start_position)
        


    #set image in background to reference for prompt
        if numpy_image is not None:
            self.image = self.convert_numpy_img_to_qpixmap(numpy_image)
            
            
        else:
            self.image = QPixmap("patrick.png")
            
        
        
        

        
        self.show()

    
    

    def save_file(self):
        file_path, name = QFileDialog.getSaveFileName(self, "Save file", self.title, "PNG Image file (*.png)")
        if file_path:
            self.image.save(file_path)



    def closeEvent(self, event):
        event.accept()

    
    def set_and_convert_img(self, np_img):
        image = self.convert_numpy_img_to_qpixmap(np_img)
        self.pixmaps.append(image)
        self.viewWidget.addlabel(image)
        self.viewWidget.repaint()
        
       



    def convert_numpy_img_to_qpixmap(self, np_img):
        height, width, channel = np_img.shape
        bytesPerLine = 3 * width
        return QPixmap(QImage(np_img.data, width, height, bytesPerLine, QImage.Format.Format_RGB888).rgbSwapped())
            

    def new_image_window(self):
        try:self.snippingTool.image_captured.disconnect()      
        except Exception: pass
        self.snippingTool.image_captured.connect(self.set_and_convert_img)
        
        self.snippingTool.widget_closed.connect(self.snippingTool.close)
        self.snippingTool.start()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainMenu = Menu()
    
    sys.exit(app.exec())
