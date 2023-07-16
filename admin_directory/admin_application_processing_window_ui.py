# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admin-application-processing-windowgahaah.ui'
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
        self.line_dispatcher = QLineEdit(self.frame)
        self.line_dispatcher.setObjectName(u"line_dispatcher")
        self.line_dispatcher.setGeometry(QRect(10, 280, 410, 60))
        self.line_dispatcher.setStyleSheet(u"color: white;\n"
                                           "font-size: 18pt;")
        self.line_dispatcher.setReadOnly(False)
        self.line_dispatcher.setClearButtonEnabled(False)
        self.statusComboBox = QComboBox(self.frame)
        self.statusComboBox.addItem("")
        self.statusComboBox.addItem("")
        self.statusComboBox.setObjectName(u"statusComboBox")
        self.statusComboBox.setGeometry(QRect(10, 120, 410, 60))
        self.statusComboBox.setStyleSheet(u"color: white;\n"
                                          "font-size: 18pt;")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 20, 261, 61))
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
        self.responsibleComboBox = QComboBox(self.frame)
        self.responsibleComboBox.setObjectName(u"responsibleComboBox")
        self.responsibleComboBox.setGeometry(QRect(10, 200, 410, 60))
        self.responsibleComboBox.setStyleSheet(u"color: white;\n"
                                               "font-size: 18pt;")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.processingButton.setDefault(False)
        self.canselButton.setDefault(False)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Application processing window", None))
        self.processingButton.setText(
            QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.line_dispatcher.setInputMask("")
        self.line_dispatcher.setText("")
        self.line_dispatcher.setPlaceholderText(QCoreApplication.translate("MainWindow",
                                                                           u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0434\u0438\u0441\u043f\u0435\u0442\u0447\u0435\u0440\u0430",
                                                                           None))
        self.statusComboBox.setItemText(0, QCoreApplication.translate("MainWindow",
                                                                      u"\u0412 \u0440\u0430\u0431\u043e\u0442\u0435",
                                                                      None))
        self.statusComboBox.setItemText(1, QCoreApplication.translate("MainWindow",
                                                                      u"\u0417\u0430\u043a\u0440\u044b\u0442\u0430",
                                                                      None))

        self.statusComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow",
                                                                          u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0441\u0442\u0430\u0442\u0443\u0441 \u0437\u0430\u044f\u0432\u043a\u0438",
                                                                          None))
        self.label.setText(QCoreApplication.translate("MainWindow",
                                                      u"\u041e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0430 \u0437\u0430\u044f\u0432\u043a\u0438",
                                                      None))
        self.canselButton.setText(
            QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.responsibleComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow",
                                                                               u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0435\u043d\u043d\u043e\u0433\u043e",
                                                                               None))
    # retranslateUi
