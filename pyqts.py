import sys,os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

current_pen = "pen"

class Drawer(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setAttribute(Qt.WA_StaticContents)
        #çizim alanının boyutları
        h = 200
        w = 960

        #kalemin özellikleri
        self.myPenWidth = 10
        self.myPenColor = Qt.black

        self.image = QImage(w, h, QImage.Format_RGB32)
        self.path = QPainterPath()
        self.clearImage()
        self.eraser_but = QPushButton("Silgi")
        self.pencil_but = QPushButton("Kalem")
        self.eraser_but.clicked.connect(self.select_eraser)
        self.pencil_but.clicked.connect(self.select_pencil)

        self.btnSave = QPushButton("Görüntüyü Kaydet")
        self.btnClear = QPushButton("Tahtayı Temizle")
        self.drawer = Drawer()

        w.setLayout(QVBoxLayout())
        w.layout().addWidget(self.eraser)
        w.layout().addWidget(self.pencil)
        w.layout().addWidget(self.btnSave)
        w.layout().addWidget(self.btnClear)
        w.layout().addWidget(self.drawer)
        self.btnSave.clicked.connect(self.kayit)
        self.btnClear.clicked.connect(self.drawer.clearImage)



    def select_eraser(self):
        self.myPenColor=Qt.white
    def select_pencil(self):
        self.myPenColor=Qt.black

    def clearImage(self):#Tahtayı temizliyor
        self.path = QPainterPath()
        self.image.fill(Qt.white)
        self.update()

    def saveImage(self, fileName, fileFormat):
        self.image.save(fileName, fileFormat)

    def mousePressEvent(self, event):
        self.path.moveTo(event.pos())

    def mouseMoveEvent(self, event):
        self.path.lineTo(event.pos())
        p = QPainter(self.image)
        p.setPen(QPen(self.myPenColor,self.myPenWidth, Qt.SolidLine, Qt.RoundCap,Qt.RoundJoin))
        p.drawPath(self.path)
        p.end()
        self.update()

    def sizeHint(self):
        return QSize(960, 540)

#Kaydederek ana programa geçiş
    def kayit(self):
        self.drawer.saveImage("image.png", "PNG")
        os.system('python arayuz.pyw')




if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QMainWindow()
    w.show()
    sys.exit(app.exec_())
