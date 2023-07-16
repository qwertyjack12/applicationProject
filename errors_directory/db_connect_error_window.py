# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'db_connect_error_windowoiGrwY.ui'
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
import res_rs

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(360, 151)
        MainWindow.setMinimumSize(QSize(360, 151))
        MainWindow.setMaximumSize(QSize(360, 151))
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.840909, y2:0.881, stop:0 rgba(47, 58, 86, 255), stop:1 rgba(64, 109, 150, 255));\n"
"font-family: Comic Sans MS;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 341, 133))
        self.frame.setStyleSheet(u"background-color: rgba(255,255,255, 30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.exit_btm = QPushButton(self.frame)
        self.exit_btm.setObjectName(u"exit_btm")
        self.exit_btm.setGeometry(QRect(260, 100, 75, 24))
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
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 20, 171, 20))
        self.label.setStyleSheet(u"color: white;\n"
"border-color: transparent;\n"
"background-color: transparent;\n"
"font-size: 10pt;")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QRect(50, 50, 291, 31))
        self.label_2.setStyleSheet(u"color: white;\n"
"border-color: transparent;\n"
"background-color: transparent;\n"
"font-size: 10pt;")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 70, 141, 21))
        self.label_3.setStyleSheet(u"color: white;\n"
"border-color: transparent;\n"
"background-color: transparent;\n"
"font-size: 10pt;")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 20, 51, 51))
        self.label_4.setStyleSheet(u"border-color: transparent;\n"
"background-color: transparent;")
        self.label_4.setPixmap(QPixmap(u":/ico/resources/icons/bd_error.png"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041e\u0448\u0438\u0431\u043a\u0430 \u0441\u043e\u0435\u0434\u0438\u043d\u0435\u043d\u0438\u044f \u0441 \u0411\u0414", None))
        self.exit_btm.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0448\u0438\u0431\u043a\u0430 \u0441\u043e\u0435\u0434\u0438\u043d\u0435\u043d\u0438\u044f \u0441 \u0411\u0414", None))
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.label_2.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u044c\u0442\u0435 \u043f\u0440\u0430\u0432\u0438\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u0443\u043a\u0430\u0437\u0430\u043d\u043d\u044b\u0445 \u0434\u0430\u043d\u043d\u044b\u0445.", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043f\u0440\u043e\u0431\u0443\u0439\u0442\u0435 \u0435\u0449\u0435 \u0440\u0430\u0437!", None))
        self.label_4.setText("")
    # retranslateUi