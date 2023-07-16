# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'despatcher-filtration-app-windowjmFDNA.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QLineEdit,
                               QMainWindow, QPushButton, QSizePolicy, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 740)
        MainWindow.setMinimumSize(QSize(640, 660))
        MainWindow.setMaximumSize(QSize(640, 740))
        MainWindow.setStyleSheet(
            u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.840909, y2:0.881, stop:0 rgba(47, 58, 86, 255), stop:1 rgba(64, 109, 150, 255));\n"
            "font-family: Comic Sans MS;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 621, 721))
        self.frame.setStyleSheet(u"background-color: rgba(255,255,255, 30);\n"
                                 "border: 1px solid rgba(255,255,255,40);\n"
                                 "border-radius: 7px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.filtrationButton = QPushButton(self.frame)
        self.filtrationButton.setObjectName(u"filtrationButton")
        self.filtrationButton.setGeometry(QRect(60, 630, 500, 71))
        self.filtrationButton.setStyleSheet(u"QPushButton {\n"
                                            "color: white;\n"
                                            "border-radius: 7px;\n"
                                            "font-weight: bold;\n"
                                            "font-size: 20pt;\n"
                                            "}\n"
                                            "QPushButton:hover{\n"
                                            "color: rgb(141, 170, 255);\n"
                                            "}\n"
                                            "QPushButton:pressed{\n"
                                            "background-color: rgdargba(255, 255, 255, 70);\n"
                                            "}")
        self.line_address = QLineEdit(self.frame)
        self.line_address.setObjectName(u"line_address")
        self.line_address.setGeometry(QRect(10, 20, 601, 95))
        self.line_address.setStyleSheet(u"color: white;\n"
                                        "font-weight: bold;\n"
                                        "font-size: 25pt;")
        self.line_address.setReadOnly(False)
        self.line_address.setClearButtonEnabled(False)
        self.line_responsible = QLineEdit(self.frame)
        self.line_responsible.setObjectName(u"line_responsible")
        self.line_responsible.setGeometry(QRect(10, 130, 600, 95))
        self.line_responsible.setStyleSheet(u"color: white;\n"
                                            "font-weight: bold;\n"
                                            "font-size: 25pt;")
        self.line_responsible.setReadOnly(False)
        self.line_responsible.setClearButtonEnabled(False)
        self.line_date_of_creation = QLineEdit(self.frame)
        self.line_date_of_creation.setObjectName(u"line_date_of_creation")
        self.line_date_of_creation.setGeometry(QRect(10, 310, 600, 95))
        self.line_date_of_creation.setStyleSheet(u"color: white;\n"
                                                 "font-weight: bold;\n"
                                                 "font-size: 25pt;")
        self.line_date_of_creation.setReadOnly(False)
        self.line_date_of_creation.setClearButtonEnabled(False)
        self.line_date_of_adoption = QLineEdit(self.frame)
        self.line_date_of_adoption.setObjectName(u"line_date_of_adoption")
        self.line_date_of_adoption.setGeometry(QRect(10, 420, 600, 95))
        self.line_date_of_adoption.setStyleSheet(u"color: white;\n"
                                                 "font-weight: bold;\n"
                                                 "font-size: 25pt;")
        self.line_date_of_adoption.setReadOnly(False)
        self.line_date_of_adoption.setClearButtonEnabled(False)
        self.statusComboBox = QComboBox(self.frame)
        self.statusComboBox.addItem("")
        self.statusComboBox.addItem("")
        self.statusComboBox.addItem("")
        self.statusComboBox.addItem("")
        self.statusComboBox.addItem("")
        self.statusComboBox.setObjectName(u"statusComboBox")
        self.statusComboBox.setGeometry(QRect(10, 240, 601, 51))
        self.statusComboBox.setStyleSheet(u"color: white;\n"
                                          "font-size: 15pt;")
        self.reset_filtrButton = QPushButton(self.frame)
        self.reset_filtrButton.setObjectName(u"reset_filtrButton")
        self.reset_filtrButton.setGeometry(QRect(60, 540, 500, 71))
        self.reset_filtrButton.setStyleSheet(u"QPushButton {\n"
                                             "color: white;\n"
                                             "border-radius: 7px;\n"
                                             "font-weight: bold;\n"
                                             "font-size: 20pt;\n"
                                             "}\n"
                                             "QPushButton:hover{\n"
                                             "color: rgb(141, 170, 255);\n"
                                             "}\n"
                                             "QPushButton:pressed{\n"
                                             "background-color: rgdargba(255, 255, 255, 70);\n"
                                             "}")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Filtration window", None))
        self.filtrationButton.setText(QCoreApplication.translate("MainWindow",
                                                                 u"\u0424\u0438\u043b\u044c\u0442\u0440\u043e\u0432\u0430\u0442\u044c",
                                                                 None))
        self.line_address.setInputMask("")
        self.line_address.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"\u0410\u0434\u0440\u0435\u0441", None))
        self.line_responsible.setInputMask("")
        self.line_responsible.setPlaceholderText(QCoreApplication.translate("MainWindow",
                                                                            u"\u041e\u0442\u0432\u0435\u0442\u0441\u0432\u0435\u043d\u043d\u044b\u0439",
                                                                            None))
        self.line_date_of_creation.setInputMask("")
        self.line_date_of_creation.setPlaceholderText(QCoreApplication.translate("MainWindow",
                                                                                 u"\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f",
                                                                                 None))
        self.line_date_of_adoption.setInputMask("")
        self.line_date_of_adoption.setPlaceholderText(QCoreApplication.translate("MainWindow",
                                                                                 u"\u0414\u0430\u0442\u0430 \u043d\u0430\u0447\u0430\u043b\u0430 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0438",
                                                                                 None))
        self.statusComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u0430\u044f",
                                                                      None))
        self.statusComboBox.setItemText(1, QCoreApplication.translate("MainWindow",
                                                                      u"\u0412 \u0440\u0430\u0431\u043e\u0442\u0435",
                                                                      None))
        self.statusComboBox.setItemText(2, QCoreApplication.translate("MainWindow",
                                                                      u"\u0412\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0430",
                                                                      None))
        self.statusComboBox.setItemText(3, QCoreApplication.translate("MainWindow",
                                                                      u"\u0417\u0430\u043a\u0440\u044b\u0442\u0430",
                                                                      None))
        self.statusComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435", None))

        self.statusComboBox.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0443\u0441", None))
        self.reset_filtrButton.setText(QCoreApplication.translate("MainWindow",
                                                                  u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c \u0444\u0438\u043b\u044c\u0442\u0440\u044b",
                                                                  None))
    # retranslateUi
