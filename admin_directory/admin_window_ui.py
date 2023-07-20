# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admin-windowbJiNhG.ui'
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
                               QPushButton, QSizePolicy, QTableView, QVBoxLayout,
                               QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1600, 680)
        MainWindow.setMinimumSize(QSize(1100, 600))
        MainWindow.setStyleSheet(
            u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.840909, y2:0.881, stop:0 rgba(47, 58, 86, 255), stop:1 rgba(64, 109, 150, 255));\n"
            "font-family: Comic Sans MS;\n"
            "")
        self.about_as_action = QAction(MainWindow)
        self.about_as_action.setObjectName(u"about_as_action")
        self.logout_action = QAction(MainWindow)
        self.logout_action.setObjectName(u"logout_action")
        self.action_3 = QAction(MainWindow)
        self.action_3.setObjectName(u"action_3")
        self.action_4 = QAction(MainWindow)
        self.action_4.setObjectName(u"action_4")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_7 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(520, 0))
        self.frame.setStyleSheet(u"background-color: rgba(255,255,255, 30);\n"
                                 "border: 1px solid rgba(255,255,255,40);\n"
                                 "border-radius: 7px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: white;\n"
                                   "font-weight: bold;\n"
                                   "font-size: 20pt;\n"
                                   "background-color: none;\n"
                                   "border: none;")

        self.verticalLayout_2.addWidget(self.label_3)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.id_lineEdit = QLineEdit(self.frame)
        self.id_lineEdit.setObjectName(u"id_lineEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.id_lineEdit.sizePolicy().hasHeightForWidth())
        self.id_lineEdit.setSizePolicy(sizePolicy1)
        self.id_lineEdit.setMinimumSize(QSize(365, 0))
        self.id_lineEdit.setStyleSheet(u"color: white;\n"
                                       "font-size: 16pt;")
        self.id_lineEdit.setPlaceholderText(
            u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 id \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f")

        self.horizontalLayout_5.addWidget(self.id_lineEdit)

        self.find_user_btn = QPushButton(self.frame)
        self.find_user_btn.setObjectName(u"find_user_btn")
        self.find_user_btn.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_5.addWidget(self.find_user_btn)

        self.verticalLayout_8.addLayout(self.horizontalLayout_5)

        self.verticalLayout_2.addLayout(self.verticalLayout_8)

        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.horizontalLayout_7.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy2)
        self.frame_2.setStyleSheet(u"background-color: rgba(255,255,255, 30);\n"
                                   "border: 1px solid rgba(255,255,255,40);\n"
                                   "border-radius: 7px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"color: white;\n"
                                   "font-weight: bold;\n"
                                   "font-size: 20pt;\n"
                                   "background-color: none;\n"
                                   "border: none;")

        self.verticalLayout_4.addWidget(self.label_4)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(10)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.filtrationComboBox = QComboBox(self.frame_2)
        self.filtrationComboBox.addItem("")
        self.filtrationComboBox.addItem("")
        self.filtrationComboBox.addItem("")
        self.filtrationComboBox.addItem("")
        self.filtrationComboBox.setObjectName(u"filtrationComboBox")
        self.filtrationComboBox.setStyleSheet(u"color: white;\n"
                                              "font-size: 15pt;")

        self.horizontalLayout_8.addWidget(self.filtrationComboBox)

        self.filtrationButton = QPushButton(self.frame_2)
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

        self.horizontalLayout_8.addWidget(self.filtrationButton)

        self.verticalLayout_4.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_6.addLayout(self.verticalLayout_4)

        self.horizontalLayout_7.addWidget(self.frame_2)

        self.verticalLayout_5.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy3)
        self.frame_3.setStyleSheet(u"background-color: rgba(255,255,255, 30);\n"
                                   "border: 1px solid rgba(255,255,255,40);\n"
                                   "border-radius: 7px;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(10)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(10)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.select_all_btn_ = QPushButton(self.frame_3)
        self.select_all_btn_.setObjectName(u"select_all_btn_")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.select_all_btn_.sizePolicy().hasHeightForWidth())
        self.select_all_btn_.setSizePolicy(sizePolicy4)
        self.select_all_btn_.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_11.addWidget(self.select_all_btn_)

        self.reset_select_btn_ = QPushButton(self.frame_3)
        self.reset_select_btn_.setObjectName(u"reset_select_btn_")
        sizePolicy4.setHeightForWidth(self.reset_select_btn_.sizePolicy().hasHeightForWidth())
        self.reset_select_btn_.setSizePolicy(sizePolicy4)
        self.reset_select_btn_.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_11.addWidget(self.reset_select_btn_)

        self.verticalLayout_9.addLayout(self.horizontalLayout_11)

        self.tableView_users = QTableView(self.frame_3)
        self.tableView_users.setObjectName(u"tableView_users")
        self.tableView_users.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.tableView_users.sizePolicy().hasHeightForWidth())
        self.tableView_users.setSizePolicy(sizePolicy3)
        self.tableView_users.setMinimumSize(QSize(500, 0))
        self.tableView_users.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableView_users.setStyleSheet(u"QTableView{\n"
                                           "color: white;\n"
                                           "background-color: rgb(127, 131, 132);\n"
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
        self.tableView_users.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableView_users.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableView_users.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableView_users.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView_users.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableView_users.setSortingEnabled(True)
        self.tableView_users.horizontalHeader().setCascadingSectionResizes(True)

        self.verticalLayout_9.addWidget(self.tableView_users)

        self.horizontalLayout_4.addLayout(self.verticalLayout_9)

        self.horizontalLayout_9.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy5)
        self.frame_4.setStyleSheet(u"background-color: rgba(255,255,255, 30);\n"
                                   "border: 1px solid rgba(255,255,255,40);\n"
                                   "border-radius: 7px;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableView_applications = QTableView(self.frame_4)
        self.tableView_applications.setObjectName(u"tableView_applications")
        sizePolicy5.setHeightForWidth(self.tableView_applications.sizePolicy().hasHeightForWidth())
        self.tableView_applications.setSizePolicy(sizePolicy5)
        self.tableView_applications.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableView_applications.setStyleSheet(u"QTableView{\n"
                                                  "color: white;\n"
                                                  "background-color: rgb(127, 131, 132);\n"
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
        self.tableView_applications.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableView_applications.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableView_applications.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableView_applications.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView_applications.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableView_applications.setShowGrid(True)
        self.tableView_applications.setSortingEnabled(True)
        self.tableView_applications.horizontalHeader().setCascadingSectionResizes(True)
        self.tableView_applications.verticalHeader().setCascadingSectionResizes(False)

        self.verticalLayout.addWidget(self.tableView_applications)

        self.horizontalLayout_9.addWidget(self.frame_4)

        self.verticalLayout_5.addLayout(self.horizontalLayout_9)

        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background-color: rgba(255,255,255, 30);\n"
                                   "border: 1px solid rgba(255,255,255,40);\n"
                                   "border-radius: 7px;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.processingUserButton = QPushButton(self.frame_5)
        self.processingUserButton.setObjectName(u"processingUserButton")
        sizePolicy1.setHeightForWidth(self.processingUserButton.sizePolicy().hasHeightForWidth())
        self.processingUserButton.setSizePolicy(sizePolicy1)
        self.processingUserButton.setMinimumSize(QSize(510, 0))
        self.processingUserButton.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_3.addWidget(self.processingUserButton)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.processingAppButton = QPushButton(self.frame_5)
        self.processingAppButton.setObjectName(u"processingAppButton")
        self.processingAppButton.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout.addWidget(self.processingAppButton)

        self.reportsAppsButton = QPushButton(self.frame_5)
        self.reportsAppsButton.setObjectName(u"reportsAppsButton")
        self.reportsAppsButton.setStyleSheet(u"QPushButton {\n"
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
        self.reportsAppsButton.setAutoDefault(False)

        self.horizontalLayout.addWidget(self.reportsAppsButton)

        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)

        self.verticalLayout_6.addWidget(self.frame_5)

        self.verticalLayout_7.addLayout(self.verticalLayout_6)

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
        self.menu_2 = QMenu(self.menuBar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_3 = QMenu(self.menu_2)
        self.menu_3.setObjectName(u"menu_3")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.program_menu.menuAction())
        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menu_2.menuAction())
        self.program_menu.addAction(self.help_menu.menuAction())
        self.help_menu.addAction(self.about_as_action)
        self.menu.addAction(self.logout_action)
        self.menu_2.addAction(self.menu_3.menuAction())
        self.menu_3.addAction(self.action_3)
        self.menu_3.addAction(self.action_4)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Application admin window", None))
        self.about_as_action.setText(
            QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435",
                                       None))
        self.logout_action.setText(QCoreApplication.translate("MainWindow",
                                                              u"\u0412\u044b\u0439\u0442\u0438 \u0438\u0437 \u0443\u0447\u0435\u0442\u043d\u043e\u0439 \u0437\u0430\u043f\u0438\u0441\u0438",
                                                              None))
        self.action_3.setText(
            QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.action_4.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0431\u0440\u0430\u0442\u044c", None))
        # if QT_CONFIG(whatsthis)
        self.frame.setWhatsThis(
            QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        # endif // QT_CONFIG(whatsthis)
        self.label_3.setText(QCoreApplication.translate("MainWindow",
                                                        u"\u041f\u043e\u0438\u0441\u043a \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f",
                                                        None))
        self.find_user_btn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        # if QT_CONFIG(whatsthis)
        self.frame_2.setWhatsThis(
            QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        # endif // QT_CONFIG(whatsthis)
        self.label_4.setText(QCoreApplication.translate("MainWindow",
                                                        u"\u0424\u0438\u043b\u044c\u0442\u0440\u0430\u0446\u0438\u044f \u0437\u0430\u044f\u0432\u043a\u0438",
                                                        None))
        self.filtrationComboBox.setItemText(0, QCoreApplication.translate("MainWindow",
                                                                          u"\u0412 \u0440\u0430\u0431\u043e\u0442\u0435",
                                                                          None))
        self.filtrationComboBox.setItemText(1, QCoreApplication.translate("MainWindow",
                                                                          u"\u0412\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u0430",
                                                                          None))
        self.filtrationComboBox.setItemText(2, QCoreApplication.translate("MainWindow",
                                                                          u"\u0417\u0430\u043a\u0440\u044b\u0442\u0430",
                                                                          None))
        self.filtrationComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435", None))

        self.filtrationComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow",
                                                                              u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0441\u0442\u0430\u0442\u0443\u0441",
                                                                              None))
        self.filtrationButton.setText(QCoreApplication.translate("MainWindow",
                                                                 u"\u0424\u0438\u043b\u044c\u0442\u0440\u043e\u0432\u0430\u0442\u044c",
                                                                 None))
        self.select_all_btn_.setText(QCoreApplication.translate("MainWindow",
                                                                u"\u0412\u044b\u0434\u0435\u043b\u0438\u0442\u044c \u0432\u0441\u0435\u0445",
                                                                None))
        self.reset_select_btn_.setText(
            QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c", None))
        self.processingUserButton.setText(QCoreApplication.translate("MainWindow",
                                                                     u"\u041e\u0431\u0440\u0430\u0431\u043e\u0442\u0430\u0442\u044c \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f",
                                                                     None))
        self.processingAppButton.setText(QCoreApplication.translate("MainWindow",
                                                                    u"\u041e\u0431\u0440\u0430\u0431\u043e\u0442\u0430\u0442\u044c \u0437\u0430\u044f\u0432\u043a\u0443",
                                                                    None))
        self.reportsAppsButton.setText(
            QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0435\u0442\u043d\u043e\u0441\u0442\u044c",
                                       None))
        self.program_menu.setTitle(
            QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430", None))
        self.help_menu.setTitle(
            QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0440\u0430\u0432\u043a\u0430", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow",
                                                      u"\u0423\u0447\u0435\u0442\u043d\u0430\u044f \u0437\u0430\u043f\u0438\u0441\u044c",
                                                      None))
        self.menu_2.setTitle(
            QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043b\u044c\u0442\u0440\u0430\u0446\u0438\u044f",
                                       None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow",
                                                        u"\u041f\u0430\u043d\u0435\u043b\u044c \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0435\u0439",
                                                        None))
    # retranslateUi
