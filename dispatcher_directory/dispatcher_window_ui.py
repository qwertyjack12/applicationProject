# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'despatcher-windowRyESyM.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
                           QCursor, QFont, QFontDatabase, QGradient,
                           QIcon, QImage, QKeySequence, QLinearGradient,
                           QPainter, QPalette, QPixmap, QRadialGradient,
                           QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox,
                               QFrame, QHBoxLayout, QHeaderView, QLabel,
                               QLineEdit, QMainWindow, QMenu, QMenuBar,
                               QPushButton, QRadioButton, QSizePolicy, QTableView,
                               QVBoxLayout, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1600, 744)
        MainWindow.setMinimumSize(QSize(850, 600))
        MainWindow.setStyleSheet(
            u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.840909, y2:0.881, stop:0 rgba(47, 58, 86, 255), stop:1 rgba(64, 109, 150, 255));\n"
            "font-family: Comic Sans MS;")
        self.about_as_action = QAction(MainWindow)
        self.about_as_action.setObjectName(u"about_as_action")
        self.logout_action = QAction(MainWindow)
        self.logout_action.setObjectName(u"logout_action")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tableFrame = QFrame(self.centralwidget)
        self.tableFrame.setObjectName(u"tableFrame")
        self.tableFrame.setStyleSheet(u"background-color: rgba(255,255,255, 30);\n"
                                      "border: 1px solid rgba(255,255,255,40);\n"
                                      "border-radius: 7px;")
        self.verticalLayout_2 = QVBoxLayout(self.tableFrame)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.filtrationFrame = QFrame(self.tableFrame)
        self.filtrationFrame.setObjectName(u"filtrationFrame")
        self.filtrationFrame.setStyleSheet(u"background-color: rgba(255,255,255, 30);\n"
                                           "border: 1px solid rgba(255,255,255,40);\n"
                                           "border-radius: 7px;")
        self.verticalLayout = QVBoxLayout(self.filtrationFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label = QLabel(self.filtrationFrame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: white;\n"
                                 "font-weight: bold;\n"
                                 "font-size: 20pt;\n"
                                 "background-color: none;\n"
                                 "border: none;")

        self.verticalLayout_6.addWidget(self.label)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.status_comboBox = QComboBox(self.filtrationFrame)
        self.status_comboBox.addItem("")
        self.status_comboBox.addItem("")
        self.status_comboBox.addItem("")
        self.status_comboBox.addItem("")
        self.status_comboBox.setObjectName(u"status_comboBox")
        self.status_comboBox.setEnabled(True)
        self.status_comboBox.setStyleSheet(u"color: white;\n"
                                           "font-size: 15pt;")

        self.horizontalLayout_6.addWidget(self.status_comboBox)

        self.responsible_comboBox = QComboBox(self.filtrationFrame)
        self.responsible_comboBox.setObjectName(u"responsible_comboBox")
        self.responsible_comboBox.setEnabled(True)
        self.responsible_comboBox.setStyleSheet(u"color: white;\n"
                                                "font-size: 15pt;")

        self.horizontalLayout_6.addWidget(self.responsible_comboBox)

        self.verticalLayout_7.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.region_comboBox = QComboBox(self.filtrationFrame)
        self.region_comboBox.setObjectName(u"region_comboBox")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.region_comboBox.sizePolicy().hasHeightForWidth())
        self.region_comboBox.setSizePolicy(sizePolicy)
        self.region_comboBox.setStyleSheet(u"color: white;\n"
                                           "font-size: 15pt;")

        self.horizontalLayout_3.addWidget(self.region_comboBox)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.city_radioButton = QRadioButton(self.filtrationFrame)
        self.city_radioButton.setObjectName(u"city_radioButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.city_radioButton.sizePolicy().hasHeightForWidth())
        self.city_radioButton.setSizePolicy(sizePolicy1)
        self.city_radioButton.setStyleSheet(u"font-size: 15pt;\n"
                                            "color: white;\n"
                                            "background-color: none;\n"
                                            "border: none;")
        self.city_radioButton.setChecked(True)

        self.horizontalLayout_2.addWidget(self.city_radioButton)

        self.locality_radioButton = QRadioButton(self.filtrationFrame)
        self.locality_radioButton.setObjectName(u"locality_radioButton")
        sizePolicy1.setHeightForWidth(self.locality_radioButton.sizePolicy().hasHeightForWidth())
        self.locality_radioButton.setSizePolicy(sizePolicy1)
        self.locality_radioButton.setStyleSheet(u"font-size: 15pt;\n"
                                                "color: white;\n"
                                                "background-color: none;\n"
                                                "border: none;")

        self.horizontalLayout_2.addWidget(self.locality_radioButton)

        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)

        self.city_comboBox = QComboBox(self.filtrationFrame)
        self.city_comboBox.setObjectName(u"city_comboBox")
        sizePolicy.setHeightForWidth(self.city_comboBox.sizePolicy().hasHeightForWidth())
        self.city_comboBox.setSizePolicy(sizePolicy)
        self.city_comboBox.setStyleSheet(u"color: white;\n"
                                         "font-size: 15pt;")

        self.horizontalLayout_3.addWidget(self.city_comboBox)

        self.street_comboBox = QComboBox(self.filtrationFrame)
        self.street_comboBox.setObjectName(u"street_comboBox")
        sizePolicy.setHeightForWidth(self.street_comboBox.sizePolicy().hasHeightForWidth())
        self.street_comboBox.setSizePolicy(sizePolicy)
        self.street_comboBox.setStyleSheet(u"color: white;\n"
                                           "font-size: 15pt;")

        self.horizontalLayout_3.addWidget(self.street_comboBox)

        self.verticalLayout_7.addLayout(self.horizontalLayout_3)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_4 = QLabel(self.filtrationFrame)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)
        self.label_4.setStyleSheet(u"color: white;\n"
                                   "font-size: 15pt;")

        self.horizontalLayout_8.addWidget(self.label_4)

        self.line_date_of_creation_after = QLineEdit(self.filtrationFrame)
        self.line_date_of_creation_after.setObjectName(u"line_date_of_creation_after")
        self.line_date_of_creation_after.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.line_date_of_creation_after.sizePolicy().hasHeightForWidth())
        self.line_date_of_creation_after.setSizePolicy(sizePolicy2)
        self.line_date_of_creation_after.setCursor(QCursor(Qt.ArrowCursor))
        self.line_date_of_creation_after.setStyleSheet(u"QLineEdit {\n"
                                                       "    font-size: 15pt;\n"
                                                       "    color: white;\n"
                                                       "}")
        self.line_date_of_creation_after.setReadOnly(False)
        self.line_date_of_creation_after.setClearButtonEnabled(False)

        self.horizontalLayout_8.addWidget(self.line_date_of_creation_after)

        self.line_date_of_creation_before = QLineEdit(self.filtrationFrame)
        self.line_date_of_creation_before.setObjectName(u"line_date_of_creation_before")
        self.line_date_of_creation_before.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.line_date_of_creation_before.sizePolicy().hasHeightForWidth())
        self.line_date_of_creation_before.setSizePolicy(sizePolicy2)
        self.line_date_of_creation_before.setCursor(QCursor(Qt.ArrowCursor))
        self.line_date_of_creation_before.setStyleSheet(u"color: white;\n"
                                                        "font-size: 15pt;")
        self.line_date_of_creation_before.setReadOnly(False)
        self.line_date_of_creation_before.setClearButtonEnabled(False)

        self.horizontalLayout_8.addWidget(self.line_date_of_creation_before)

        self.horizontalLayout_10.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_5 = QLabel(self.filtrationFrame)
        self.label_5.setObjectName(u"label_5")
        sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy2)
        self.label_5.setStyleSheet(u"color: white;\n"
                                   "font-size: 15pt;")

        self.horizontalLayout_9.addWidget(self.label_5)

        self.line_closing_date_after = QLineEdit(self.filtrationFrame)
        self.line_closing_date_after.setObjectName(u"line_closing_date_after")
        self.line_closing_date_after.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.line_closing_date_after.sizePolicy().hasHeightForWidth())
        self.line_closing_date_after.setSizePolicy(sizePolicy2)
        self.line_closing_date_after.setCursor(QCursor(Qt.ArrowCursor))
        self.line_closing_date_after.setStyleSheet(u"color: white;\n"
                                                   "font-size: 15pt;")
        self.line_closing_date_after.setReadOnly(False)
        self.line_closing_date_after.setClearButtonEnabled(False)

        self.horizontalLayout_9.addWidget(self.line_closing_date_after)

        self.line_cloxing_date_before = QLineEdit(self.filtrationFrame)
        self.line_cloxing_date_before.setObjectName(u"line_cloxing_date_before")
        self.line_cloxing_date_before.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.line_cloxing_date_before.sizePolicy().hasHeightForWidth())
        self.line_cloxing_date_before.setSizePolicy(sizePolicy2)
        self.line_cloxing_date_before.setCursor(QCursor(Qt.ArrowCursor))
        self.line_cloxing_date_before.setStyleSheet(u"color: white;\n"
                                                    "font-size: 15pt;")
        self.line_cloxing_date_before.setReadOnly(False)
        self.line_cloxing_date_before.setClearButtonEnabled(False)

        self.horizontalLayout_9.addWidget(self.line_cloxing_date_before)

        self.horizontalLayout_10.addLayout(self.horizontalLayout_9)

        self.verticalLayout_8.addLayout(self.horizontalLayout_10)

        self.verticalLayout_7.addLayout(self.verticalLayout_8)

        self.verticalLayout_5.addLayout(self.verticalLayout_7)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(10)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.filtrationBtn = QPushButton(self.filtrationFrame)
        self.filtrationBtn.setObjectName(u"filtrationBtn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.filtrationBtn.sizePolicy().hasHeightForWidth())
        self.filtrationBtn.setSizePolicy(sizePolicy3)
        self.filtrationBtn.setStyleSheet(u"QPushButton {\n"
                                         "color: white;\n"
                                         "border-radius: 7px;\n"
                                         "font-weight: bold;\n"
                                         "border-color: white;\n"
                                         "font-size: 15pt;\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         "color: rgb(141, 170, 255);\n"
                                         "}\n"
                                         "QPushButton:pressed{\n"
                                         "background-color: rgdargba(255, 255, 255, 70);\n"
                                         "}")

        self.horizontalLayout_11.addWidget(self.filtrationBtn)

        self.reset_filtrationBtn = QPushButton(self.filtrationFrame)
        self.reset_filtrationBtn.setObjectName(u"reset_filtrationBtn")
        sizePolicy3.setHeightForWidth(self.reset_filtrationBtn.sizePolicy().hasHeightForWidth())
        self.reset_filtrationBtn.setSizePolicy(sizePolicy3)
        self.reset_filtrationBtn.setStyleSheet(u"QPushButton {\n"
                                               "color: white;\n"
                                               "border-radius: 7px;\n"
                                               "font-weight: bold;\n"
                                               "border-color: white;\n"
                                               "font-size: 15pt;\n"
                                               "}\n"
                                               "QPushButton:hover{\n"
                                               "color: rgb(141, 170, 255);\n"
                                               "}\n"
                                               "QPushButton:pressed{\n"
                                               "background-color: rgdargba(255, 255, 255, 70);\n"
                                               "}")

        self.horizontalLayout_11.addWidget(self.reset_filtrationBtn)

        self.verticalLayout_5.addLayout(self.horizontalLayout_11)

        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.verticalLayout.addLayout(self.verticalLayout_6)

        self.verticalLayout_2.addWidget(self.filtrationFrame)

        self.tableView = QTableView(self.tableFrame)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableView.setStyleSheet(u"QTableView{\n"
                                     "color: white;\n"
                                     "border-bottom-right-radius: 7px;\n"
                                     "border-bottom-left-radius: 7px;\n"
                                     "gridline-color:white;\n"
                                     "border: 2px solid white;\n"
                                     "font-family: Arial;\n"
                                     "font-size: 14pt;\n"
                                     "}\n"
                                     "\n"
                                     "QHeaderView {\n"
                                     "background-color: lightgray;\n"
                                     "color: black;\n"
                                     "font-size: 16px;\n"
                                     "font-family: Arial;\n"
                                     "}\n"
                                     "\n"
                                     "QTableView::item:selected{\n"
                                     "border: none;\n"
                                     "color: rgda(255,255,255);\n"
                                     "background-color: rgda(255,255,255,50);\n"
                                     "}")
        self.tableView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableView.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableView.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableView.setShowGrid(True)
        self.tableView.setSortingEnabled(True)
        self.tableView.horizontalHeader().setCascadingSectionResizes(True)
        self.tableView.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableView.verticalHeader().setCascadingSectionResizes(False)

        self.verticalLayout_2.addWidget(self.tableView)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.editApplicationButton = QPushButton(self.tableFrame)
        self.editApplicationButton.setObjectName(u"editApplicationButton")
        self.editApplicationButton.setStyleSheet(u"QPushButton {\n"
                                                 "color: white;\n"
                                                 "border-radius: 7px;\n"
                                                 "font-weight: bold;\n"
                                                 "border-color: white;\n"
                                                 "font-size: 15pt;\n"
                                                 "}\n"
                                                 "QPushButton:hover{\n"
                                                 "color: rgb(141, 170, 255);\n"
                                                 "}\n"
                                                 "QPushButton:pressed{\n"
                                                 "background-color: rgdargba(255, 255, 255, 70);\n"
                                                 "}")

        self.horizontalLayout.addWidget(self.editApplicationButton)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout_3.addWidget(self.tableFrame)

        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1600, 23))
        self.program_menu = QMenu(self.menuBar)
        self.program_menu.setObjectName(u"program_menu")
        self.help_menu = QMenu(self.program_menu)
        self.help_menu.setObjectName(u"help_menu")
        self.menu = QMenu(self.menuBar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.program_menu.menuAction())
        self.menuBar.addAction(self.menu.menuAction())
        self.program_menu.addAction(self.help_menu.menuAction())
        self.help_menu.addAction(self.about_as_action)
        self.menu.addAction(self.logout_action)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Application dispatcher window", None))
        self.about_as_action.setText(
            QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435",
                                       None))
        self.logout_action.setText(QCoreApplication.translate("MainWindow",
                                                              u"\u0412\u044b\u0439\u0442\u0438 \u0438\u0437 \u0443\u0447\u0435\u0442\u043d\u043e\u0439 \u0437\u0430\u043f\u0438\u0441\u0438",
                                                              None))
        self.label.setText(QCoreApplication.translate("MainWindow",
                                                      u"\u0424\u0438\u043b\u044c\u0442\u0440\u0430\u0446\u0438\u044f \u0437\u0430\u044f\u0432\u043e\u043a",
                                                      None))
        self.status_comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u0430\u044f",
                                                                       None))
        self.status_comboBox.setItemText(1, QCoreApplication.translate("MainWindow",
                                                                       u"\u0412 \u0440\u0430\u0431\u043e\u0442\u0435",
                                                                       None))
        self.status_comboBox.setItemText(2, QCoreApplication.translate("MainWindow",
                                                                       u"\u0412\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0430",
                                                                       None))
        self.status_comboBox.setItemText(3, QCoreApplication.translate("MainWindow",
                                                                       u"\u0417\u0430\u043a\u0440\u044b\u0442\u0430",
                                                                       None))

        self.status_comboBox.setPlaceholderText(QCoreApplication.translate("MainWindow",
                                                                           u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0441\u0442\u0430\u0442\u0443\u0441",
                                                                           None))
        self.responsible_comboBox.setPlaceholderText(QCoreApplication.translate("MainWindow",
                                                                                u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0435\u043d\u043d\u043e\u0433\u043e",
                                                                                None))
        self.region_comboBox.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0433\u0438\u043e\u043d", None))
        self.city_radioButton.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0440\u043e\u0434", None))
        self.locality_radioButton.setText(QCoreApplication.translate("MainWindow",
                                                                     u"\u041d\u0430\u0441\u0435\u043b\u0435\u043d\u043d\u044b\u0439 \u043f\u0443\u043d\u043a\u0442",
                                                                     None))
        self.city_comboBox.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0440\u043e\u0434", None))
        self.street_comboBox.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"\u0423\u043b\u0438\u0446\u0430", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow",
                                                        u"\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f",
                                                        None))
        self.line_date_of_creation_after.setInputMask("")
        self.line_date_of_creation_after.setText("")
        self.line_date_of_creation_after.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"\u043e\u0442", None))
        self.line_date_of_creation_before.setInputMask("")
        self.line_date_of_creation_before.setText("")
        self.line_date_of_creation_before.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"\u0434\u043e", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow",
                                                        u"\u0414\u0430\u0442\u0430 \u0437\u0430\u043a\u0440\u044b\u0442\u0438\u044f",
                                                        None))
        self.line_closing_date_after.setInputMask("")
        self.line_closing_date_after.setText("")
        self.line_closing_date_after.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u043e\u0442", None))
        self.line_cloxing_date_before.setInputMask("")
        self.line_cloxing_date_before.setText("")
        self.line_cloxing_date_before.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"\u0434\u043e", None))
        self.filtrationBtn.setText(QCoreApplication.translate("MainWindow",
                                                              u"\u0424\u0438\u043b\u044c\u0442\u0440\u043e\u0432\u0430\u0442\u044c",
                                                              None))
        self.reset_filtrationBtn.setText(QCoreApplication.translate("MainWindow",
                                                                    u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c \u0444\u0438\u043b\u044c\u0442\u0440",
                                                                    None))
        self.editApplicationButton.setText(QCoreApplication.translate("MainWindow",
                                                                      u"\u041e\u0431\u0440\u0430\u0431\u043e\u0442\u0430\u0442\u044c \u0437\u0430\u044f\u0432\u043a\u0443",
                                                                      None))
        self.program_menu.setTitle(
            QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430", None))
        self.help_menu.setTitle(
            QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0440\u0430\u0432\u043a\u0430", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow",
                                                      u"\u0423\u0447\u0435\u0442\u043d\u0430\u044f \u0437\u0430\u043f\u0438\u0441\u044c",
                                                      None))
    # retranslateUi
