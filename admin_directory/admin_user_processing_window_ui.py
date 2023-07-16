# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admin-user-processing-windowSSrhbo.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QLabel,
                               QLineEdit, QMainWindow, QPushButton, QSizePolicy,
                               QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.ApplicationModal)
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
        self.processingButton = QPushButton(self.frame)
        self.processingButton.setObjectName(u"processingButton")
        self.processingButton.setGeometry(QRect(240, 390, 181, 71))
        self.processingButton.setStyleSheet(u"QPushButton {\n"
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
        self.processingButton.setAutoDefault(False)
        self.processingButton.setFlat(False)
        self.line_login = QLineEdit(self.frame)
        self.line_login.setObjectName(u"line_login")
        self.line_login.setGeometry(QRect(10, 200, 410, 60))
        self.line_login.setStyleSheet(u"color: white;\n"
                                      "font-size: 18pt;")
        self.line_login.setReadOnly(False)
        self.line_login.setClearButtonEnabled(False)
        self.line_password = QLineEdit(self.frame)
        self.line_password.setObjectName(u"line_password")
        self.line_password.setGeometry(QRect(10, 280, 410, 60))
        self.line_password.setStyleSheet(u"color: white;\n"
                                         "font-size: 18pt;")
        self.line_password.setReadOnly(False)
        self.line_password.setClearButtonEnabled(False)
        self.roleComboBox = QComboBox(self.frame)
        self.roleComboBox.addItem("")
        self.roleComboBox.addItem("")
        self.roleComboBox.setObjectName(u"roleComboBox")
        self.roleComboBox.setGeometry(QRect(10, 120, 410, 60))
        self.roleComboBox.setStyleSheet(u"color: white;\n"
                                        "font-size: 18pt;")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 20, 361, 61))
        self.label.setStyleSheet(u"color: white;\n"
                                 "font-weight: bold;\n"
                                 "font-size: 21pt;\n"
                                 "background-color: none;\n"
                                 "border: none;")
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

        self.processingButton.setDefault(False)
        self.canselButton.setDefault(False)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"User processing window", None))
        self.processingButton.setText(
            QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.line_login.setInputMask("")
        self.line_login.setText("")
        self.line_login.setPlaceholderText(QCoreApplication.translate("MainWindow",
                                                                      u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u043b\u043e\u0433\u0438\u043d",
                                                                      None))
        self.line_password.setInputMask("")
        self.line_password.setText("")
        self.line_password.setPlaceholderText(QCoreApplication.translate("MainWindow",
                                                                         u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u043f\u0430\u0440\u043e\u043b\u044c",
                                                                         None))
        self.roleComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"admin", None))
        self.roleComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"dispatcher", None))

        self.roleComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow",
                                                                        u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0440\u043e\u043b\u044c",
                                                                        None))
        self.label.setText(QCoreApplication.translate("MainWindow",
                                                      u"\u041e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0430 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f",
                                                      None))
        self.canselButton.setText(
            QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c", None))
    # retranslateUi
