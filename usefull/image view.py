import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QFileDialog
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QPixmap

class ImageViewer(QMainWindow):
    def __init__(self):
        super(ImageViewer, self).__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Image Viewer')
        self.setGeometry(100, 100, 800, 600)

        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.label)

        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        file_path = event.mimeData().urls()[0].toLocalFile()
        self.loadImage(file_path)

    def loadImage(self, file_path):
        pixmap = QPixmap(file_path)
        self.label.setPixmap(pixmap)
        self.label.adjustSize()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ImageViewer()
    window.show()
    sys.exit(app.exec_())
