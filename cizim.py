import sys,os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Drawer(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setAttribute(Qt.WA_StaticContents)

        #çizim alanının boyutları
        h = 200
        w = 800

        #kalemin özellikleri
        self.myPenWidth = 10
        self.myPenColor = Qt.black
        self.image = QImage(w, h, QImage.Format_RGB32)
        self.path = QPainterPath()
        self.clearImage()
	
	
	#Tahtayı temizleme fonksiyonu
    def clearImage(self):
        self.path = QPainterPath()
        self.image.fill(Qt.white)
        self.update()
	
	
	#Resmi kaydetme fonksiyonu
    def saveImage(self, fileName, fileFormat):
        self.image.save(fileName, fileFormat)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawImage(event.rect(), self.image, self.rect())

    def mousePressEvent(self, event):
        self.path.moveTo(event.pos())

    def mouseMoveEvent(self, event):
        self.path.lineTo(event.pos())
        p = QPainter(self.image)
        p.setPen(QPen(self.myPenColor,self.myPenWidth, Qt.SolidLine, Qt.RoundCap,Qt.RoundJoin))
        p.drawPath(self.path)
        p.end()
        self.update()
	
	
	#Pencere boyutları
    def sizeHint(self):
        return QSize(800, 300)


#Resmi kaydettikten sonra ana programa geçme
def save_pic():
    drawer.saveImage("image.png", "PNG")
    os.startfile('mainprog.exe')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    btnSave = QPushButton("Görüntüyü Kaydet")
    btnClear = QPushButton("Tahtayı Temizle")
    drawer = Drawer()

    w.setLayout(QVBoxLayout())
    w.layout().addWidget(btnSave)
    w.layout().addWidget(btnClear)
    w.layout().addWidget(drawer)
    

    btnSave.clicked.connect(save_pic)
    btnClear.clicked.connect(drawer.clearImage)

    w.show()
    sys.exit(app.exec_())
