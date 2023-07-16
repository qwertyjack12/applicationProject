# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'incomeuHFOye.ui'
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
                               QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
                               QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(450, 500)
        MainWindow.setMinimumSize(QSize(450, 500))
        MainWindow.setMaximumSize(QSize(450, 500))
        MainWindow.setStyleSheet(
            u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.840909, y2:0.881, stop:0 rgba(47, 58, 86, 255), stop:1 rgba(64, 109, 150, 255));\n"
            "font-family: Comic Sans MS;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgba(255,255,255, 30);\n"
                                 "border: 1px solid rgba(255,255,255,40);\n"
                                 "border-radius: 7px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.incomeButton = QPushButton(self.frame)
        self.incomeButton.setObjectName(u"incomeButton")
        self.incomeButton.setGeometry(QRect(10, 390, 181, 71))
        self.incomeButton.setMaximumSize(QSize(500, 105))
        self.incomeButton.setStyleSheet(u"QPushButton {\n"
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
        self.line_login = QLineEdit(self.frame)
        self.line_login.setObjectName(u"line_login")
        self.line_login.setGeometry(QRect(10, 160, 411, 60))
        self.line_login.setStyleSheet(u"color: white;\n"
                                      "font-weight: bold;\n"
                                      "font-size: 18pt;")
        self.line_login.setReadOnly(False)
        self.line_login.setClearButtonEnabled(False)
        self.line_password = QLineEdit(self.frame)
        self.line_password.setObjectName(u"line_password")
        self.line_password.setGeometry(QRect(10, 240, 411, 60))
        self.line_password.setStyleSheet(u"color: white;\n"
                                         "font-weight: bold;\n"
                                         "font-size: 18pt;")
        self.line_password.setEchoMode(QLineEdit.Password)
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

        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Authorization", None))
        self.incomeButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.registrationButton.setText(QCoreApplication.translate("MainWindow",
                                                                   u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f",
                                                                   None))
        self.line_login.setInputMask("")
        self.line_login.setPlaceholderText(QCoreApplication.translate("MainWindow",
                                                                      u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043b\u043e\u0433\u0438\u043d",
                                                                      None))
        self.line_password.setInputMask("")
        self.line_password.setPlaceholderText(QCoreApplication.translate("MainWindow",
                                                                         u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c",
                                                                         None))
        self.label.setText(QCoreApplication.translate("MainWindow",
                                                      u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f",
                                                      None))
    # retranslateUi
