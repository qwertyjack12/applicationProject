# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user-windowHfUPrd.ui'
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
                               QLayout, QMainWindow, QMenu, QMenuBar,
                               QPushButton, QSizePolicy, QTableView, QVBoxLayout,
                               QWidget)
import res_rs


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1650, 600)
        MainWindow.setMinimumSize(QSize(850, 600))
        MainWindow.setCursor(QCursor(Qt.ArrowCursor))
        MainWindow.setStyleSheet(
            u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.840909, y2:0.881, stop:0 rgba(47, 58, 86, 255), stop:1 rgba(64, 109, 150, 255));\n"
            "font-family: Comic Sans MS;")
        self.about_as_action = QAction(MainWindow)
        self.about_as_action.setObjectName(u"about_as_action")
        self.logout_action = QAction(MainWindow)
        self.logout_action.setObjectName(u"logout_action")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.filtrationFrame = QFrame(self.centralwidget)
        self.filtrationFrame.setObjectName(u"filtrationFrame")
        self.filtrationFrame.setStyleSheet(u"background-color: rgba(255,255,255, 30);\n"
                                           "border: 1px solid rgba(255,255,255,40);\n"
                                           "border-radius: 7px;")
        self.verticalLayout = QVBoxLayout(self.filtrationFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.filtrationFrame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: white;\n"
                                 "font-weight: bold;\n"
                                 "font-size: 20pt;\n"
                                 "background-color: none;\n"
                                 "border: none;")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.filtrationComboBox = QComboBox(self.filtrationFrame)
        self.filtrationComboBox.addItem("")
        self.filtrationComboBox.addItem("")
        self.filtrationComboBox.addItem("")
        self.filtrationComboBox.addItem("")
        self.filtrationComboBox.addItem("")
        self.filtrationComboBox.setObjectName(u"filtrationComboBox")
        self.filtrationComboBox.setStyleSheet(u"color: white;\n"
                                              "font-size: 15pt;")

        self.horizontalLayout_2.addWidget(self.filtrationComboBox)

        self.filtrationButton = QPushButton(self.filtrationFrame)
        self.filtrationButton.setObjectName(u"filtrationButton")
        self.filtrationButton.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_2.addWidget(self.filtrationButton)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalLayout_3.addWidget(self.filtrationFrame)

        self.tableFrame = QFrame(self.centralwidget)
        self.tableFrame.setObjectName(u"tableFrame")
        self.tableFrame.setStyleSheet(u"background-color: rgba(255,255,255, 30);\n"
                                      "border: 1px solid rgba(255,255,255,40);\n"
                                      "border-radius: 7px;")
        self.verticalLayout_2 = QVBoxLayout(self.tableFrame)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tableView = QTableView(self.tableFrame)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableView.setStyleSheet(u"QTableView{\n"
                                     "color: white;\n"
                                     "border: 2px solid rgda(255, 255, 255, 30);\n"
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
        self.tableView.verticalHeader().setCascadingSectionResizes(False)

        self.verticalLayout_2.addWidget(self.tableView)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.createApplicationButton = QPushButton(self.tableFrame)
        self.createApplicationButton.setObjectName(u"createApplicationButton")
        self.createApplicationButton.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout.addWidget(self.createApplicationButton)

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

        self.workReportButton = QPushButton(self.tableFrame)
        self.workReportButton.setObjectName(u"workReportButton")
        self.workReportButton.setStyleSheet(u"QPushButton {\n"
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
        self.workReportButton.setAutoDefault(False)

        self.horizontalLayout.addWidget(self.workReportButton)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout_3.addWidget(self.tableFrame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1650, 23))
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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Application project", None))
        self.about_as_action.setText(
            QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435",
                                       None))
        self.logout_action.setText(QCoreApplication.translate("MainWindow",
                                                              u"\u0412\u044b\u0439\u0442\u0438 \u0438\u0437 \u0443\u0447\u0435\u0442\u043d\u043e\u0439 \u0437\u0430\u043f\u0438\u0441\u0438",
                                                              None))
        self.label.setText(QCoreApplication.translate("MainWindow",
                                                      u"\u0424\u0438\u043b\u044c\u0442\u0440\u0430\u0446\u0438\u044f \u0437\u0430\u044f\u0432\u043a\u0438",
                                                      None))
        self.filtrationComboBox.setItemText(0,
                                            QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u0430\u044f",
                                                                       None))
        self.filtrationComboBox.setItemText(1, QCoreApplication.translate("MainWindow",
                                                                          u"\u0412 \u0440\u0430\u0431\u043e\u0442\u0435",
                                                                          None))
        self.filtrationComboBox.setItemText(2, QCoreApplication.translate("MainWindow",
                                                                          u"\u0412\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0430",
                                                                          None))
        self.filtrationComboBox.setItemText(3, QCoreApplication.translate("MainWindow",
                                                                          u"\u0417\u0430\u043a\u0440\u044b\u0442\u0430",
                                                                          None))
        self.filtrationComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435", None))

        self.filtrationComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow",
                                                                              u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0441\u0442\u0430\u0442\u0443\u0441",
                                                                              None))
        self.filtrationButton.setText(QCoreApplication.translate("MainWindow",
                                                                 u"\u0424\u0438\u043b\u044c\u0442\u0440\u043e\u0432\u0430\u0442\u044c",
                                                                 None))
        self.createApplicationButton.setText(QCoreApplication.translate("MainWindow",
                                                                        u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0437\u0430\u044f\u0432\u043a\u0443",
                                                                        None))
        self.editApplicationButton.setText(QCoreApplication.translate("MainWindow",
                                                                      u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0437\u0430\u044f\u0432\u043a\u0443",
                                                                      None))
        self.workReportButton.setText(QCoreApplication.translate("MainWindow",
                                                                 u"\u0410\u043a\u0442 \u043e \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u043e\u0439 \u0437\u0430\u044f\u0432\u043a\u0435",
                                                                 None))
        self.program_menu.setTitle(
            QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430", None))
        self.help_menu.setTitle(
            QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0440\u0430\u0432\u043a\u0430", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow",
                                                      u"\u0423\u0447\u0435\u0442\u043d\u0430\u044f \u0437\u0430\u043f\u0438\u0441\u044c",
                                                      None))
    # retranslateUi
