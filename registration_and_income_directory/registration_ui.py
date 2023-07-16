# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registrationbkLTuD.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
                               QMainWindow, QPushButton, QSizePolicy, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(450, 500)
        MainWindow.setMinimumSize(QSize(450, 500))
        MainWindow.setMaximumSize(QSize(450, 500))
        MainWindow.setStyleSheet(
            u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.840909, y2:0.881, stop:0 rgba(47, 58, 86, 255), stop:1 rgba(64, 109, 150, 255));\n"
            "font-family: Comic Sans MS;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 431, 481))
        self.frame.setStyleSheet(u"background-color: rgba(255,255,255, 30);\n"
                                 "border: 1px solid rgba(255,255,255,40);\n"
                                 "border-radius: 7px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.registrationButton = QPushButton(self.frame)
        self.registrationButton.setObjectName(u"registrationButton")
        self.registrationButton.setGeometry(QRect(240, 390, 181, 71))
        self.registrationButton.setStyleSheet(u"QPushButton {\n"
                                              "color: white;\n"
                                              "border-radius: 7px;\n"
                                              "border-color: white;\n"
                                              "font-weight: bold;\n"
                                              "font-size: 20pt;\n"
                                              "}\n"
                                              "QPushButton:hover{\n"
                                              "color: rgb(141, 170, 255);\n"
                                              "}\n"
                                              "QPushButton:pressed{\n"
                                              "background-color: rgdargba(255, 255, 255, 70);\n"
                                              "}")
        self.registrationButton.setAutoDefault(False)
        self.registrationButton.setFlat(False)
        self.line_full_name = QLineEdit(self.frame)
        self.line_full_name.setObjectName(u"line_full_name")
        self.line_full_name.setGeometry(QRect(10, 120, 411, 60))
        self.line_full_name.setStyleSheet(u"color: white;\n"
                                          "font-weight: bold;\n"
                                          "font-size: 18pt;")
        self.line_full_name.setReadOnly(False)
        self.line_full_name.setClearButtonEnabled(False)
        self.line_login = QLineEdit(self.frame)
        self.line_login.setObjectName(u"line_login")
        self.line_login.setGeometry(QRect(10, 200, 411, 60))
        self.line_login.setStyleSheet(u"color: white;\n"
                                      "font-weight: bold;\n"
                                      "font-size: 18pt;")
        self.line_login.setReadOnly(False)
        self.line_login.setClearButtonEnabled(False)
        self.line_password = QLineEdit(self.frame)
        self.line_password.setObjectName(u"line_password")
        self.line_password.setGeometry(QRect(10, 280, 411, 60))
        self.line_password.setStyleSheet(u"color: white;\n"
                                         "font-weight: bold;\n"
                                         "font-size: 18pt;")
        self.line_password.setReadOnly(False)
        self.line_password.setClearButtonEnabled(False)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 20, 191, 61))
        self.label.setStyleSheet(u"color: white;\n"
                                 "font-weight: bold;\n"
                                 "font-size: 21pt;\n"
                                 "background-color: none;\n"
                                 "border: none;")
        self.label.setFrameShape(QFrame.NoFrame)
        self.canselButton = QPushButton(self.frame)
        self.canselButton.setObjectName(u"canselButton")
        self.canselButton.setGeometry(QRect(10, 390, 181, 71))
        self.canselButton.setStyleSheet(u"QPushButton {\n"
                                        "color: white;\n"
                                        "border-radius: 7px;\n"
                                        "border-color: white;\n"
                                        "font-weight: bold;\n"
                                        "font-size: 20pt;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "color: rgb(141, 170, 255);\n"
                                        "}\n"
                                        "QPushButton:pressed{\n"
                                        "background-color: rgdargba(255, 255, 255, 70);\n"
                                        "}")
        self.canselButton.setAutoDefault(False)
        self.canselButton.setFlat(False)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.registrationButton.setDefault(False)
        self.canselButton.setDefault(False)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Registration", None))
        self.registrationButton.setText(
            QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.line_full_name.setInputMask("")
        self.line_full_name.setText("")
        self.line_full_name.setPlaceholderText(QCoreApplication.translate("MainWindow",
                                                                          u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0438\u043c\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f",
                                                                          None))
        self.line_login.setInputMask("")
        self.line_login.setText("")
        self.line_login.setPlaceholderText(QCoreApplication.translate("MainWindow",
                                                                      u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043b\u043e\u0433\u0438\u043d",
                                                                      None))
        self.line_password.setInputMask("")
        self.line_password.setText("")
        self.line_password.setPlaceholderText(QCoreApplication.translate("MainWindow",
                                                                         u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c",
                                                                         None))
        self.label.setText(QCoreApplication.translate("MainWindow",
                                                      u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f",
                                                      None))
        self.canselButton.setText(
            QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c", None))
    # retranslateUi
