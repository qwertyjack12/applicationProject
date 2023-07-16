# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'program_infoNUHPGs.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
                               QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import res_rs


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(450, 330)
        MainWindow.setMinimumSize(QSize(450, 330))
        MainWindow.setMaximumSize(QSize(450, 330))
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
        self.exit_btm = QPushButton(self.frame)
        self.exit_btm.setObjectName(u"exit_btm")
        self.exit_btm.setGeometry(QRect(160, 270, 101, 30))
        self.exit_btm.setStyleSheet(u"QPushButton {\n"
                                    "color: white;\n"
                                    "border-radius: 7px;\n"
                                    "font-weight: bold;\n"
                                    "font-size: 14pt;\n"
                                    "}\n"
                                    "QPushButton:hover{\n"
                                    "color: rgb(141, 170, 255);\n"
                                    "}\n"
                                    "QPushButton:pressed{\n"
                                    "background-color: rgdargba(255, 255, 255, 70);\n"
                                    "}")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 10, 411, 241))
        self.frame_2.setStyleSheet(u"background-color: rgba(255,255,255, 30);\n"
                                   "border: 1px solid rgba(255,255,255,40);\n"
                                   "border-radius: 7px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 120, 200))
        self.label.setStyleSheet(u"background-color: none;\n"
                                 "border: none;")
        self.label.setPixmap(QPixmap(u":/ico/resources/icons/cat.png"))
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(150, 40, 241, 21))
        self.label_2.setStyleSheet(u"color: white;\n"
                                   "font-size: 12pt;\n"
                                   "background-color: none;\n"
                                   "border: none;")
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(150, 80, 121, 21))
        self.label_3.setStyleSheet(u"color: white;\n"
                                   "font-size: 12pt;\n"
                                   "background-color: none;\n"
                                   "border: none;")
        self.link_label = QLabel(self.frame_2)
        self.link_label.setObjectName(u"link_label")
        self.link_label.setGeometry(QRect(210, 120, 191, 21))
        self.link_label.setStyleSheet(u"color: white;\n"
                                      "font-size: 12pt;\n"
                                      "background-color: none;\n"
                                      "border: none;")
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(150, 120, 61, 21))
        self.label_5.setStyleSheet(u"color: white;\n"
                                   "font-size: 12pt;\n"
                                   "background-color: none;\n"
                                   "border: none;")
        self.label_gif = QLabel(self.frame_2)
        self.label_gif.setObjectName(u"label_gif")
        self.label_gif.setGeometry(QRect(200, 150, 150, 80))
        self.label_gif.setStyleSheet(u"background-color: none;\n"
                                     "border: none;")

        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435",
                                       None))
        self.exit_btm.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow",
                                                        u"\u041f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0438 \u0437\u0430\u044f\u0432\u043e\u043a",
                                                        None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Version: 0.0.0.1", None))
        self.link_label.setText(QCoreApplication.translate("MainWindow",
                                                           u"<html><head/><body><p><a href=\"https://github.com/qwertyjack12\"><span style=\" color:#ffffff;\">github.com/qwertyjack12</span></a></p></body></html>",
                                                           None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"GitHub:", None))
        self.label_gif.setText("")
    # retranslateUi
