from PyQt5 import QtCore, QtGui, QtWidgets #Arayüz kütüphanesi
import pytesseract #Resimden yazıya aktarma kütüphanesi
from PIL import Image #Resimden yazıya akatarmaya yardımcı kütüphane
from googletrans import Translator #Çeviri kütüphanesi
from gtts import gTTS #Google Text to Speech(Yazıdan sese) kütüphanesi
import playsound #Ses çalma kütüphanesi
import os
class Ui_MainWindow(object):
    #Ana menüdeki buton,metin gibi nesnelerin tanımlanması
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(635, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #büyük font
        bigfont = QtGui.QFont()
        bigfont.setPointSize(16)

        #kalın font
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)

        self.ac = QtWidgets.QPushButton(self.centralwidget)
        self.ac.setGeometry(QtCore.QRect(50, 20, 141, 28))
        self.ac.setObjectName("ac")
        self.resim_yazi = QtWidgets.QLabel(self.centralwidget)
        self.resim_yazi.setGeometry(QtCore.QRect(50, 70, 531, 151))
        self.resim_yazi.setText("")
        self.resim_yazi.setObjectName("resim_yazi")
        self.resim_yazi.setFont(bigfont)
        self.ceviri_yazi = QtWidgets.QLabel(self.centralwidget)
        self.ceviri_yazi.setGeometry(QtCore.QRect(50, 320, 531, 141))
        self.ceviri_yazi.setText("")
        self.ceviri_yazi.setFont(bigfont)
        self.ceviri_yazi.setObjectName("ceviri_yazi")
        self.ceviri = QtWidgets.QLabel(self.centralwidget)
        self.ceviri.setGeometry(QtCore.QRect(60, 270, 55, 28))
        self.ceviri.setFont(font)
        self.ceviri.setObjectName("ceviri")
        self.diller = QtWidgets.QComboBox(self.centralwidget)
        self.diller.setGeometry(QtCore.QRect(270, 270, 181, 28))
        self.diller.setObjectName("diller")
        self.dil = QtWidgets.QLabel(self.centralwidget)
        self.dil.setGeometry(QtCore.QRect(240, 270, 21, 28))
        self.dil.setObjectName("dil")
        self.cevir = QtWidgets.QPushButton(self.centralwidget)
        self.cevir.setGeometry(QtCore.QRect(460, 270, 93, 28))
        self.cevir.setObjectName("cevir")
        self.res_oku = QtWidgets.QPushButton(self.centralwidget)
        self.res_oku.setGeometry(QtCore.QRect(500, 220, 93, 28))
        self.res_oku.setObjectName("res_oku")
        self.cev_oku = QtWidgets.QPushButton(self.centralwidget)
        self.cev_oku.setGeometry(QtCore.QRect(500, 500, 93, 28))
        self.cev_oku.setObjectName("cev_oku")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        #dillerin combobox'a eklenmesi
        self.diller.addItem("English")
        self.diller.addItem("Français")
        self.diller.addItem("Deutsch")
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #butonlara basınca gidilecek fonksiyonlar
        self.ac.clicked.connect(self.resim_ac)
        self.cevir.clicked.connect(self.translate)
        self.cev_oku.clicked.connect(self.ceviri_oku)
        self.res_oku.clicked.connect(self.resim_oku)

        self.sayi = 0 #dosya adlandırmada kullanılacak değişken

        if os.path.isfile("image.png"):
            self.autostart()


        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ana Pencere"))
        self.ac.setText(_translate("MainWindow", "Resim Aç"))
        self.ceviri.setText(_translate("MainWindow", "Çeviri"))
        self.dil.setText(_translate("MainWindow", "Dil:"))
        self.cevir.setText(_translate("MainWindow", "Çevir"))
        self.res_oku.setText(_translate("MainWindow", "Resmi Oku"))
        self.cev_oku.setText(_translate("MainWindow", "Çeviriyi Oku"))


    def autostart(self):
        dosya="image.png"
        img = Image.open(dosya)
        pytesseract.pytesseract.tesseract_cmd = "D:/Programlar/Tesseract/tesseract.exe"
        res_yaz = pytesseract.image_to_string(img, lang="tur")
        self.resim_yazi.setText(res_yaz)
        if res_yaz == "":
            self.resim_yazi.setText("Metin okunamadı!")
        else:
            self.resim_oku()  # Seçimden hemen sonra metni okuyor

    def resim_ac(self):  #Resimi şeçerek yazıya akatarıyor
        dosya = QtWidgets.QFileDialog.getOpenFileName()
        img = Image.open(dosya[0])
        pytesseract.pytesseract.tesseract_cmd = "D:/Programlar/Tesseract/tesseract.exe"
        res_yaz = pytesseract.image_to_string(img, lang="tur")
        self.resim_yazi.setText(res_yaz)
        if res_yaz == "":
            self.resim_yazi.setText("Metin okunamadı!")
        else:
            self.resim_oku()  # Seçimden hemen sonra metni okuyor




    def translate(self): #Diğer dillere çeviri
        global lang
        if len(self.resim_yazi.text())!=0:
            res_yaz = self.resim_yazi.text()
            translator = Translator()
            #Seçtiğimiz dile göre çeviri yapıyor
            if self.diller.currentText() == "English":
                lang="en"
                translated = translator.translate(res_yaz, src="tr", dest="en")
            elif self.diller.currentText() == "Français":
                lang="fr"
                translated = translator.translate(res_yaz, src="tr", dest="fr")
            elif self.diller.currentText() == "Deutsch":
                lang="de"
                translated = translator.translate(res_yaz, src="tr", dest="de")
            self.ceviri_yazi.setText(translated.text)
            self.ceviri_oku()#Seçimden hemen sonra metni okuyor

    def resim_oku(self): #Resim yazıya çevrilmiş metni seslendirme

        if self.resim_yazi.text() != "Metin okunamadı!":
            self.sayi += 1
            text = self.resim_yazi.text()
            tts = gTTS(text=text,lang="tr")
            tts.save("res"+str(self.sayi)+".mp3")
            playsound.playsound("res"+str(self.sayi)+".mp3", True)


    def ceviri_oku(self): #Yabancı dile çevirilmiş metni sesledirme

        if self.ceviri_yazi.text() !="Metin okunamadı!":
            self.sayi += 1
            text = self.ceviri_yazi.text()
            tts = gTTS(text=text,lang=lang)
            tts.save("cev"+str(self.sayi)+".mp3")
            playsound.playsound("cev"+str(self.sayi)+".mp3", True)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

