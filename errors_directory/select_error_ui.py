# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'select_errorNwQueT.ui'
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
                               QPushButton, QSizePolicy, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(320, 150)
        MainWindow.setMinimumSize(QSize(320, 150))
        MainWindow.setMaximumSize(QSize(320, 150))
        MainWindow.setStyleSheet(
            u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.840909, y2:0.881, stop:0 rgba(47, 58, 86, 255), stop:1 rgba(64, 109, 150, 255));\n"
            "font-family: Comic Sans MS;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(9, 9, 302, 132))
        self.frame.setStyleSheet(u"background-color: rgba(255,255,255, 30);\n"
                                 "border: 1px solid rgba(255,255,255,40);\n"
                                 "border-radius: 7px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.exit_btm_2 = QPushButton(self.frame)
        self.exit_btm_2.setObjectName(u"exit_btm_2")
        self.exit_btm_2.setGeometry(QRect(210, 100, 75, 24))
        self.exit_btm_2.setStyleSheet(u"QPushButton {\n"
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
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(50, 10, 211, 20))
        self.label_6.setStyleSheet(u"color: white;\n"
                                   "border-color: transparent;\n"
                                   "background-color: transparent;\n"
                                   "font-size: 10pt;")
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setEnabled(True)
        self.label_7.setGeometry(QRect(50, 40, 251, 31))
        self.label_7.setStyleSheet(u"color: white;\n"
                                   "border-color: transparent;\n"
                                   "background-color: transparent;\n"
                                   "font-size: 10pt;")
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(50, 60, 251, 21))
        self.label_8.setStyleSheet(u"color: white;\n"
                                   "border-color: transparent;\n"
                                   "background-color: transparent;\n"
                                   "font-size: 10pt;")
        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(0, 20, 51, 51))
        self.label_9.setStyleSheet(u"border-color: transparent;\n"
                                   "background-color: transparent;")
        self.label_9.setPixmap(QPixmap(u":/ico/resources/icons/close.png"))
        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(50, 80, 141, 20))
        self.label_10.setStyleSheet(u"color: white;\n"
                                    "border-color: transparent;\n"
                                    "background-color: transparent;\n"
                                    "font-size: 10pt;")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow",
                                                             u"\u041e\u0448\u0438\u0431\u043a\u0430 \u0432\u044b\u0431\u043e\u0440\u0430",
                                                             None))
        self.exit_btm_2.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow",
                                                        u"\u041e\u0448\u0438\u0431\u043a\u0430 \u0432\u044b\u0431\u043e\u0440\u0430",
                                                        None))
        # if QT_CONFIG(tooltip)
        self.label_7.setToolTip(
            QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(whatsthis)
        self.label_7.setWhatsThis(
            QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        # endif // QT_CONFIG(whatsthis)
        self.label_7.setText(QCoreApplication.translate("MainWindow",
                                                        u"\u0412\u044b \u043d\u0438\u0447\u0435\u0433\u043e \u043d\u0435 \u0432\u044b\u0431\u0440\u0430\u043b\u0438",
                                                        None))
        self.label_8.setText(QCoreApplication.translate("MainWindow",
                                                        u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0447\u0442\u043e-\u043d\u0438\u0431\u0443\u0434\u044c \u0434\u043b\u044f \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u0438",
                                                        None))
        self.label_9.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow",
                                                         u"\u041f\u043e\u043f\u0440\u043e\u0431\u0443\u0439\u0442\u0435 \u0435\u0449\u0435 \u0440\u0430\u0437!",
                                                         None))
    # retranslateUi
