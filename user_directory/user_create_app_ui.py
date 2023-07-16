# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user-create-appELVSIp.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGroupBox,
                               QHBoxLayout, QLabel, QLineEdit, QMainWindow,
                               QPushButton, QRadioButton, QSizePolicy, QTextEdit,
                               QVBoxLayout, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.ApplicationModal)
        MainWindow.resize(450, 840)
        MainWindow.setMinimumSize(QSize(450, 840))
        MainWindow.setMaximumSize(QSize(450, 840))
        MainWindow.setStyleSheet(
            u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.840909, y2:0.881, stop:0 rgba(47, 58, 86, 255), stop:1 rgba(64, 109, 150, 255));\n"
            "font-family: Comic Sans MS;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 431, 821))
        self.frame.setStyleSheet(u"background-color: rgba(255,255,255, 30);\n"
                                 "border: 1px solid rgba(255,255,255,40);\n"
                                 "border-radius: 7px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.create_button = QPushButton(self.frame)
        self.create_button.setObjectName(u"create_button")
        self.create_button.setGeometry(QRect(240, 730, 181, 71))
        self.create_button.setStyleSheet(u"QPushButton {\n"
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
        self.text_app = QTextEdit(self.frame)
        self.text_app.setObjectName(u"text_app")
        self.text_app.setGeometry(QRect(10, 110, 411, 150))
        self.text_app.setStyleSheet(u"color: white;\n"
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
        self.canselButton.setGeometry(QRect(10, 730, 181, 71))
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
        self.region_comboBox = QComboBox(self.frame)
        self.region_comboBox.setObjectName(u"region_comboBox")
        self.region_comboBox.setGeometry(QRect(10, 350, 411, 51))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.region_comboBox.sizePolicy().hasHeightForWidth())
        self.region_comboBox.setSizePolicy(sizePolicy)
        self.region_comboBox.setStyleSheet(u"color: white;\n"
                                           "font-size: 18pt;")
        self.city_comboBox = QComboBox(self.frame)
        self.city_comboBox.setObjectName(u"city_comboBox")
        self.city_comboBox.setGeometry(QRect(10, 490, 411, 51))
        sizePolicy.setHeightForWidth(self.city_comboBox.sizePolicy().hasHeightForWidth())
        self.city_comboBox.setSizePolicy(sizePolicy)
        self.city_comboBox.setStyleSheet(u"color: white;\n"
                                         "font-size: 18pt;")
        self.street_comboBox = QComboBox(self.frame)
        self.street_comboBox.setObjectName(u"street_comboBox")
        self.street_comboBox.setGeometry(QRect(10, 560, 411, 51))
        sizePolicy.setHeightForWidth(self.street_comboBox.sizePolicy().hasHeightForWidth())
        self.street_comboBox.setSizePolicy(sizePolicy)
        self.street_comboBox.setStyleSheet(u"color: white;\n"
                                           "font-size: 18pt;")
        self.line_fio = QLineEdit(self.frame)
        self.line_fio.setObjectName(u"line_fio")
        self.line_fio.setGeometry(QRect(10, 280, 410, 51))
        self.line_fio.setStyleSheet(u"color: white;\n"
                                    "font-size: 18pt;")
        self.line_fio.setReadOnly(False)
        self.line_fio.setClearButtonEnabled(False)
        self.line_number_room = QLineEdit(self.frame)
        self.line_number_room.setObjectName(u"line_number_room")
        self.line_number_room.setGeometry(QRect(240, 630, 181, 51))
        sizePolicy.setHeightForWidth(self.line_number_room.sizePolicy().hasHeightForWidth())
        self.line_number_room.setSizePolicy(sizePolicy)
        self.line_number_room.setMinimumSize(QSize(0, 0))
        self.line_number_room.setMaximumSize(QSize(111111, 16777215))
        self.line_number_room.setStyleSheet(u"color: white;\n"
                                            "font-size: 18pt;")
        self.line_number_room.setMaxLength(6)
        self.line_number_house = QLineEdit(self.frame)
        self.line_number_house.setObjectName(u"line_number_house")
        self.line_number_house.setGeometry(QRect(10, 630, 181, 51))
        sizePolicy.setHeightForWidth(self.line_number_house.sizePolicy().hasHeightForWidth())
        self.line_number_house.setSizePolicy(sizePolicy)
        self.line_number_house.setMinimumSize(QSize(0, 0))
        self.line_number_house.setMaximumSize(QSize(111111, 16777215))
        self.line_number_house.setStyleSheet(u"color: white;\n"
                                             "font-size: 18pt;")
        self.line_number_house.setMaxLength(6)
        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 420, 411, 50))
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.city_radioButton = QRadioButton(self.groupBox)
        self.city_radioButton.setObjectName(u"city_radioButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.city_radioButton.sizePolicy().hasHeightForWidth())
        self.city_radioButton.setSizePolicy(sizePolicy1)
        self.city_radioButton.setStyleSheet(u"font-size: 18pt;\n"
                                            "color: white;\n"
                                            "background-color: none;\n"
                                            "border: none;")
        self.city_radioButton.setChecked(True)

        self.horizontalLayout.addWidget(self.city_radioButton)

        self.locality_radioButton = QRadioButton(self.groupBox)
        self.locality_radioButton.setObjectName(u"locality_radioButton")
        sizePolicy1.setHeightForWidth(self.locality_radioButton.sizePolicy().hasHeightForWidth())
        self.locality_radioButton.setSizePolicy(sizePolicy1)
        self.locality_radioButton.setStyleSheet(u"font-size: 18pt;\n"
                                                "color: white;\n"
                                                "background-color: none;\n"
                                                "border: none;")

        self.horizontalLayout.addWidget(self.locality_radioButton)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.canselButton.setDefault(False)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Create application", None))
        self.create_button.setText(
            QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.text_app.setPlaceholderText(QCoreApplication.translate("MainWindow",
                                                                    u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0437\u0430\u044f\u043a\u0438",
                                                                    None))
        self.label.setText(QCoreApplication.translate("MainWindow",
                                                      u"\u041e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0430 \u0437\u0430\u044f\u0432\u043a\u0438",
                                                      None))
        self.canselButton.setText(
            QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.region_comboBox.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0433\u0438\u043e\u043d", None))
        self.city_comboBox.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0440\u043e\u0434", None))
        self.street_comboBox.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"\u0423\u043b\u0438\u0446\u0430", None))
        self.line_fio.setInputMask("")
        self.line_fio.setText("")
        self.line_fio.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e", None))
        self.line_number_room.setText("")
        self.line_number_room.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"\u2116 \u043a\u0432\u0430\u0440\u0442\u0438\u0440\u044b", None))
        self.line_number_house.setText("")
        self.line_number_house.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"\u2116 \u0434\u043e\u043c\u0430", None))
        self.groupBox.setTitle("")
        self.city_radioButton.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0440\u043e\u0434", None))
        self.locality_radioButton.setText(QCoreApplication.translate("MainWindow",
                                                                     u"\u041d\u0430\u0441\u0435\u043b\u0435\u043d\u043d\u044b\u0439 \u043f\u0443\u043d\u043a\u0442",
                                                                     None))
    # retranslateUi
