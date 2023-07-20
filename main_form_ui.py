# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_formlUwrwN.ui'
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
        MainWindow.resize(1351, 710)
        MainWindow.setMinimumSize(QSize(1200, 600))
        MainWindow.setStyleSheet(
            u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.840909, y2:0.881, stop:0 rgba(47, 58, 86, 255), stop:1 rgba(64, 109, 150, 255));\n"
            "font-family: Comic Sans MS;\n"
            "")
        self.simple_filtration = QAction(MainWindow)
        self.simple_filtration.setObjectName(u"simple_filtration")
        self.advanced_filtration = QAction(MainWindow)
        self.advanced_filtration.setObjectName(u"advanced_filtration")
        self.logout_action = QAction(MainWindow)
        self.logout_action.setObjectName(u"logout_action")
        self.about_as_action = QAction(MainWindow)
        self.about_as_action.setObjectName(u"about_as_action")
        self.simple_filtration_2 = QAction(MainWindow)
        self.simple_filtration_2.setObjectName(u"simple_filtration_2")
        self.advanced_filtration_2 = QAction(MainWindow)
        self.advanced_filtration_2.setObjectName(u"advanced_filtration_2")
        self.add_user_panel = QAction(MainWindow)
        self.add_user_panel.setObjectName(u"add_user_panel")
        self.delete_user_panel = QAction(MainWindow)
        self.delete_user_panel.setObjectName(u"delete_user_panel")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_7 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setStyleSheet(u"background-color: rgba(255,255,255, 30);\n"
                                   "border: 1px solid rgba(255,255,255,40);\n"
                                   "border-radius: 7px;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(10)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: white;\n"
                                   "font-weight: bold;\n"
                                   "font-size: 20pt;\n"
                                   "background-color: none;\n"
                                   "border: none;")

        self.verticalLayout_3.addWidget(self.label_3)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")

        self.verticalLayout_3.addLayout(self.verticalLayout_10)

        self.verticalLayout_9.addLayout(self.verticalLayout_3)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.id_lineEdit = QLineEdit(self.frame_3)
        self.id_lineEdit.setObjectName(u"id_lineEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.id_lineEdit.sizePolicy().hasHeightForWidth())
        self.id_lineEdit.setSizePolicy(sizePolicy1)
        self.id_lineEdit.setMinimumSize(QSize(300, 0))
        self.id_lineEdit.setStyleSheet(u"color: white;\n"
                                       "font-size: 16pt;")
        self.id_lineEdit.setPlaceholderText(
            u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 id \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f")

        self.horizontalLayout_6.addWidget(self.id_lineEdit)

        self.find_user_btn = QPushButton(self.frame_3)
        self.find_user_btn.setObjectName(u"find_user_btn")
        self.find_user_btn.setMinimumSize(QSize(110, 0))
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

        self.horizontalLayout_6.addWidget(self.find_user_btn)

        self.verticalLayout_9.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(10)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.select_all_btn_ = QPushButton(self.frame_3)
        self.select_all_btn_.setObjectName(u"select_all_btn_")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.select_all_btn_.sizePolicy().hasHeightForWidth())
        self.select_all_btn_.setSizePolicy(sizePolicy2)
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
        sizePolicy2.setHeightForWidth(self.reset_select_btn_.sizePolicy().hasHeightForWidth())
        self.reset_select_btn_.setSizePolicy(sizePolicy2)
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
        sizePolicy.setHeightForWidth(self.tableView_users.sizePolicy().hasHeightForWidth())
        self.tableView_users.setSizePolicy(sizePolicy)
        self.tableView_users.setMinimumSize(QSize(500, 0))
        self.tableView_users.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableView_users.setStyleSheet(u"QTableView{\n"
                                           "color: white;\n"
                                           "background-color: rgb(69, 91, 133);\n"
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

        self.horizontalLayout_5.addLayout(self.verticalLayout_9)

        self.horizontalLayout_4.addWidget(self.frame_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.filtrationFrame = QFrame(self.centralwidget)
        self.filtrationFrame.setObjectName(u"filtrationFrame")
        self.filtrationFrame.setStyleSheet(u"background-color: rgba(255,255,255, 30);\n"
                                           "border: 1px solid rgba(255,255,255,40);\n"
                                           "border-radius: 7px;")
        self.verticalLayout_4 = QVBoxLayout(self.filtrationFrame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label = QLabel(self.filtrationFrame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: white;\n"
                                 "font-weight: bold;\n"
                                 "font-size: 20pt;\n"
                                 "background-color: none;\n"
                                 "border: none;")

        self.verticalLayout_8.addWidget(self.label)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setSpacing(10)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(10)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.status_comboBox = QComboBox(self.filtrationFrame)
        self.status_comboBox.addItem("")
        self.status_comboBox.addItem("")
        self.status_comboBox.addItem("")
        self.status_comboBox.addItem("")
        self.status_comboBox.setObjectName(u"status_comboBox")
        self.status_comboBox.setEnabled(True)
        self.status_comboBox.setStyleSheet(u"color: white;\n"
                                           "font-size: 15pt;")

        self.horizontalLayout_7.addWidget(self.status_comboBox)

        self.responsible_comboBox = QComboBox(self.filtrationFrame)
        self.responsible_comboBox.setObjectName(u"responsible_comboBox")
        self.responsible_comboBox.setEnabled(True)
        self.responsible_comboBox.setStyleSheet(u"color: white;\n"
                                                "font-size: 15pt;")

        self.horizontalLayout_7.addWidget(self.responsible_comboBox)

        self.verticalLayout_12.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(10)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.region_comboBox = QComboBox(self.filtrationFrame)
        self.region_comboBox.setObjectName(u"region_comboBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.region_comboBox.sizePolicy().hasHeightForWidth())
        self.region_comboBox.setSizePolicy(sizePolicy3)
        self.region_comboBox.setStyleSheet(u"color: white;\n"
                                           "font-size: 15pt;")

        self.horizontalLayout_8.addWidget(self.region_comboBox)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.city_radioButton = QRadioButton(self.filtrationFrame)
        self.city_radioButton.setObjectName(u"city_radioButton")
        sizePolicy1.setHeightForWidth(self.city_radioButton.sizePolicy().hasHeightForWidth())
        self.city_radioButton.setSizePolicy(sizePolicy1)
        self.city_radioButton.setStyleSheet(u"font-size: 15pt;\n"
                                            "color: white;\n"
                                            "background-color: none;\n"
                                            "border: none;")
        self.city_radioButton.setChecked(True)

        self.horizontalLayout_10.addWidget(self.city_radioButton)

        self.locality_radioButton = QRadioButton(self.filtrationFrame)
        self.locality_radioButton.setObjectName(u"locality_radioButton")
        sizePolicy1.setHeightForWidth(self.locality_radioButton.sizePolicy().hasHeightForWidth())
        self.locality_radioButton.setSizePolicy(sizePolicy1)
        self.locality_radioButton.setStyleSheet(u"font-size: 15pt;\n"
                                                "color: white;\n"
                                                "background-color: none;\n"
                                                "border: none;")

        self.horizontalLayout_10.addWidget(self.locality_radioButton)

        self.horizontalLayout_8.addLayout(self.horizontalLayout_10)

        self.city_comboBox = QComboBox(self.filtrationFrame)
        self.city_comboBox.setObjectName(u"city_comboBox")
        sizePolicy3.setHeightForWidth(self.city_comboBox.sizePolicy().hasHeightForWidth())
        self.city_comboBox.setSizePolicy(sizePolicy3)
        self.city_comboBox.setStyleSheet(u"color: white;\n"
                                         "font-size: 15pt;")

        self.horizontalLayout_8.addWidget(self.city_comboBox)

        self.street_comboBox = QComboBox(self.filtrationFrame)
        self.street_comboBox.setObjectName(u"street_comboBox")
        sizePolicy3.setHeightForWidth(self.street_comboBox.sizePolicy().hasHeightForWidth())
        self.street_comboBox.setSizePolicy(sizePolicy3)
        self.street_comboBox.setStyleSheet(u"color: white;\n"
                                           "font-size: 15pt;")

        self.horizontalLayout_8.addWidget(self.street_comboBox)

        self.verticalLayout_12.addLayout(self.horizontalLayout_8)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setSpacing(10)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(10)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_4 = QLabel(self.filtrationFrame)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)
        self.label_4.setStyleSheet(u"color: white;\n"
                                   "font-size: 15pt;")

        self.horizontalLayout_13.addWidget(self.label_4)

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

        self.horizontalLayout_13.addWidget(self.line_date_of_creation_after)

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

        self.horizontalLayout_13.addWidget(self.line_date_of_creation_before)

        self.horizontalLayout_12.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_5 = QLabel(self.filtrationFrame)
        self.label_5.setObjectName(u"label_5")
        sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy2)
        self.label_5.setStyleSheet(u"color: white;\n"
                                   "font-size: 15pt;")

        self.horizontalLayout_14.addWidget(self.label_5)

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

        self.horizontalLayout_14.addWidget(self.line_closing_date_after)

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

        self.horizontalLayout_14.addWidget(self.line_cloxing_date_before)

        self.horizontalLayout_12.addLayout(self.horizontalLayout_14)

        self.verticalLayout_13.addLayout(self.horizontalLayout_12)

        self.verticalLayout_12.addLayout(self.verticalLayout_13)

        self.verticalLayout_11.addLayout(self.verticalLayout_12)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setSpacing(10)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.filtrationBtn = QPushButton(self.filtrationFrame)
        self.filtrationBtn.setObjectName(u"filtrationBtn")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.filtrationBtn.sizePolicy().hasHeightForWidth())
        self.filtrationBtn.setSizePolicy(sizePolicy4)
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

        self.horizontalLayout_15.addWidget(self.filtrationBtn)

        self.reset_filtrationBtn = QPushButton(self.filtrationFrame)
        self.reset_filtrationBtn.setObjectName(u"reset_filtrationBtn")
        sizePolicy4.setHeightForWidth(self.reset_filtrationBtn.sizePolicy().hasHeightForWidth())
        self.reset_filtrationBtn.setSizePolicy(sizePolicy4)
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

        self.horizontalLayout_15.addWidget(self.reset_filtrationBtn)

        self.verticalLayout_11.addLayout(self.horizontalLayout_15)

        self.verticalLayout_8.addLayout(self.verticalLayout_11)

        self.verticalLayout_4.addLayout(self.verticalLayout_8)

        self.verticalLayout_2.addWidget(self.filtrationFrame)

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
                                                  "background-color: rgb(69, 91, 133);\n"
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

        self.verticalLayout_2.addWidget(self.frame_4)

        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

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
        self.createAppButton = QPushButton(self.frame_5)
        self.createAppButton.setObjectName(u"createAppButton")
        self.createAppButton.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout.addWidget(self.createAppButton)

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
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1351, 23))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_4 = QMenu(self.menu)
        self.menu_4.setObjectName(u"menu_4")
        self.menu_3 = QMenu(self.menu)
        self.menu_3.setObjectName(u"menu_3")
        self.menu_5 = QMenu(self.menu)
        self.menu_5.setObjectName(u"menu_5")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.menu_3.menuAction())
        self.menu.addAction(self.menu_5.menuAction())
        self.menu.addAction(self.menu_4.menuAction())
        self.menu_4.addAction(self.about_as_action)
        self.menu_3.addAction(self.simple_filtration_2)
        self.menu_3.addAction(self.advanced_filtration_2)
        self.menu_5.addAction(self.add_user_panel)
        self.menu_5.addAction(self.delete_user_panel)
        self.menu_2.addAction(self.logout_action)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.simple_filtration.setText(
            QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0441\u0442\u0430\u044f", None))
        self.advanced_filtration.setText(QCoreApplication.translate("MainWindow",
                                                                    u"\u0420\u0430\u0441\u0448\u0438\u0440\u0435\u043d\u043d\u0430\u044f",
                                                                    None))
        self.logout_action.setText(QCoreApplication.translate("MainWindow",
                                                              u"\u0412\u044b\u0439\u0442\u0438 \u0438\u0437 \u0443\u0447\u0435\u0442\u043d\u043e\u0439 \u0437\u0430\u043f\u0438\u0441\u0438",
                                                              None))
        self.about_as_action.setText(
            QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435",
                                       None))
        self.simple_filtration_2.setText(
            QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0441\u0442\u0430\u044f", None))
        self.advanced_filtration_2.setText(QCoreApplication.translate("MainWindow",
                                                                      u"\u0420\u0430\u0441\u0448\u0438\u0440\u0435\u043d\u043d\u0430\u044f",
                                                                      None))
        self.add_user_panel.setText(
            QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.delete_user_panel.setText(
            QCoreApplication.translate("MainWindow", u"\u0423\u0431\u0440\u0430\u0442\u044c", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow",
                                                        u"\u041f\u043e\u0438\u0441\u043a \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f",
                                                        None))
        self.find_user_btn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.select_all_btn_.setText(QCoreApplication.translate("MainWindow",
                                                                u"\u0412\u044b\u0434\u0435\u043b\u0438\u0442\u044c \u0432\u0441\u0435\u0445",
                                                                None))
        self.reset_select_btn_.setText(
            QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c", None))
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
        self.processingUserButton.setText(QCoreApplication.translate("MainWindow",
                                                                     u"\u041e\u0431\u0440\u0430\u0431\u043e\u0442\u0430\u0442\u044c \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f",
                                                                     None))
        self.createAppButton.setText(QCoreApplication.translate("MainWindow",
                                                                u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0437\u0430\u044f\u0432\u043a\u0443",
                                                                None))
        self.processingAppButton.setText(QCoreApplication.translate("MainWindow",
                                                                    u"\u041e\u0431\u0440\u0430\u0431\u043e\u0442\u0430\u0442\u044c \u0437\u0430\u044f\u0432\u043a\u0443",
                                                                    None))
        self.reportsAppsButton.setText(
            QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0435\u0442\u043d\u043e\u0441\u0442\u044c",
                                       None))
        self.menu.setTitle(
            QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430", None))
        self.menu_4.setTitle(
            QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0440\u0430\u0432\u043a\u0430", None))
        self.menu_3.setTitle(
            QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043b\u044c\u0442\u0440\u0430\u0446\u0438\u044f",
                                       None))
        self.menu_5.setTitle(QCoreApplication.translate("MainWindow",
                                                        u"\u041f\u0430\u043d\u0435\u043b\u044c \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0435\u0439",
                                                        None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow",
                                                        u"\u0423\u0447\u0435\u0442\u043d\u0430\u044f \u0437\u0430\u043f\u0438\u0441\u044c",
                                                        None))
    # retranslateUi
