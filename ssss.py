# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'arayuz.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(635, 611)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ac = QtWidgets.QPushButton(self.centralwidget)
        self.ac.setGeometry(QtCore.QRect(50, 20, 141, 28))
        self.ac.setObjectName("ac")
        self.resim_yazi = QtWidgets.QLabel(self.centralwidget)
        self.resim_yazi.setGeometry(QtCore.QRect(50, 70, 531, 141))
        self.resim_yazi.setText("")
        self.resim_yazi.setObjectName("resim_yazi")
        self.ceviri_yazi = QtWidgets.QLabel(self.centralwidget)
        self.ceviri_yazi.setGeometry(QtCore.QRect(50, 320, 531, 151))
        self.ceviri_yazi.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ceviri_yazi.setText("")
        self.ceviri_yazi.setObjectName("ceviri_yazi")
        self.ceviri = QtWidgets.QLabel(self.centralwidget)
        self.ceviri.setGeometry(QtCore.QRect(60, 270, 55, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
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

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ac.setText(_translate("MainWindow", "Resim Aç(.png)"))
        self.ceviri.setText(_translate("MainWindow", "Çeviri"))
        self.dil.setText(_translate("MainWindow", "Dil:"))
        self.cevir.setText(_translate("MainWindow", "Çevir"))
        self.res_oku.setText(_translate("MainWindow", "Resmi Oku"))
        self.cev_oku.setText(_translate("MainWindow", "Çeviriyi Oku"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

