import datetime
import sys
from datetime import date

from PySide6 import QtWidgets, QtCore
from PySide6.QtGui import QColor, QDesktopServices, QMovie
from PySide6.QtWidgets import QCalendarWidget
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt, QUrl

from registration_and_income_directory.registration_ui import Ui_MainWindow as reg_MainWindow
from registration_and_income_directory.income_ui import Ui_MainWindow as income_MainWindow
from errors_directory.income_error_window_ui import Ui_MainWindow as income_error_MainWindow

from user_directory.user_window_ui import Ui_MainWindow as user_MainWindow
from user_directory.user_create_app_ui import Ui_MainWindow as create_app_MainWindow

from dispatcher_directory.dispatcher_window_ui import Ui_MainWindow as dispatcher_MainWindow
from dispatcher_directory.dispatcher_processing_app_ui import Ui_MainWindow as dispatcher_app_processing_MainWindow

from admin_directory.admin_window_ui import Ui_MainWindow as admin_MainWindow
from admin_directory.admin_user_processing_window_ui import Ui_MainWindow as admin_user_processing_MainWindow
from admin_directory.admin_application_processing_window_ui import \
    Ui_MainWindow as admin_application_processing_MainWindow

from program_info_ui import Ui_MainWindow as program_info_MainWindow

from main_form_ui import Ui_MainWindow as main_form_MainWindow

from errors_directory.date_filtration_error_ui import Ui_MainWindow as date_filtration_error_MainWindow
from errors_directory.padding_error_ui import Ui_MainWindow as padding_error_MainWindow
from errors_directory.select_error_ui import Ui_MainWindow as select_error_MainWindow
from errors_directory.permission_error_ui import Ui_MainWindow as permission_error_MainWindow

from errors_directory.db_connect_error_window import Ui_MainWindow as db_connect_error_MainWindow
from db.connection_db import Data

from documents import Reports
from table_model import TableModel, TableModel_with_CheckBox

USER_ROLES = ['admin', 'dispatcher', 'user']
CITY_TYPE = {"Город": "г.", "Населенный пункт": "н.п."}


class ApplicationProject(QMainWindow):
    def __init__(self):
        super(ApplicationProject, self).__init__()

        self.conn = Data()
        self.doc = Reports()

        if not self.conn.flag_connection:
            self.open_db_connect_error_window()
            return

        self.open_income_window()

    def view_admin_data_of_applications(self, params=None):
        cursor = self.conn.cursor

        apps_table_view = self.ui_admin_window.tableView_applications

        if params is not None:
            string_query_dict = ' and '.join([f"{k}='{v}'" for k, v in params.items()])
            sql_query = f"SELECT application_id, creator, responsible_mngr, status, responsible, description, address FROM applications WHERE " + string_query_dict
        else:
            sql_query = f"SELECT application_id, creator, responsible_mngr, status, responsible, description, address FROM applications"

        cursor.execute(sql_query)
        rows = cursor.fetchall()

        result = [[el if el is not None else '' for el in row] for row in rows]

        headers = ['№ заявки', 'Пользователь', 'Диспетчер', 'Статус', 'Ответственный', 'Описание', 'Адрес']

        self.admin_app_model = TableModel(result, headers)

        header = apps_table_view.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        header.setStretchLastSection(True)
        header.setOffsetToLastSection()
        header.setSectionsMovable(True)
        header.setFirstSectionMovable(False)
        header.sectionClicked.connect(
            lambda f: self.set_color(self.admin_app_model)
        )

        apps_table_view.verticalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        apps_table_view.setTextElideMode(Qt.TextElideMode.ElideMiddle)
        apps_table_view.setWordWrap(True)
        apps_table_view.verticalHeader().setDefaultAlignment(Qt.AlignmentFlag.AlignTop)

        self.set_color(self.admin_app_model)

        apps_table_view.setModel(self.admin_app_model)
        apps_table_view.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)

    def view_admin_data_of_users(self, filter=None):
        cursor = self.conn.cursor

        users_table_view = self.ui_admin_window.tableView_users

        if filter is None or filter == '':
            sql_query = f"SELECT user_id, role, full_name, login FROM users WHERE role <> 'director' AND role <> 'admin'"
        else:
            sql_query = f"SELECT user_id, role, full_name, login FROM users WHERE user_id = '{filter}' AND role <> 'director' AND role <> 'admin'"

        cursor.execute(sql_query)
        headers = ['ID', 'Права', 'Имя', 'Логин']
        rows = cursor.fetchall()

        self.admin_user_model = TableModel_with_CheckBox(rows, headers)

        header = users_table_view.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        header.setStretchLastSection(True)

        users_table_view.verticalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        users_table_view.setTextElideMode(Qt.TextElideMode.ElideMiddle)
        users_table_view.setWordWrap(True)
        users_table_view.verticalHeader().setDefaultAlignment(Qt.AlignmentFlag.AlignTop)

        self.set_color(self.admin_user_model)

        users_table_view.setModel(self.admin_user_model)
        users_table_view.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)

    def user_processing(self):
        index = self.ui_admin_window.tableView_users.selectedIndexes()[0]
        id = self.ui_admin_window.tableView_users.model().data(index)

        role = self.ui_admin_user_processing.roleComboBox.currentText()
        login = self.ui_admin_user_processing.line_login.text()
        password = self.ui_admin_user_processing.line_password.text()

        selected_user_role = self.conn.get_user_role_query(id)

        if self.conn.check_user_login_query(login):
            self.conn.update_admin_user_query(role, selected_user_role, password, str(self.user_id), id)
        else:
            self.conn.update_admin_user_query(role, selected_user_role, password, str(self.user_id), id, login)

        self.view_admin_data_of_users()

        self.admin_user_processing.close()

    def application_processing(self):
        index_id = self.ui_admin_window.tableView_applications.selectedIndexes()[0]
        id = self.ui_admin_window.tableView_applications.model().data(index_id)

        index_status = self.ui_admin_window.tableView_applications.selectedIndexes()[3]
        status_before = self.ui_admin_window.tableView_applications.model().data(index_status)

        status = self.ui_admin_app_processing.statusComboBox.currentText()
        responsible = self.ui_admin_app_processing.responsibleComboBox.currentText()
        dispatcher_id = self.ui_admin_app_processing.line_dispatcher.text()

        if len(dispatcher_id) == '' and not self.conn.check_user_id(dispatcher_id):
            dispatcher_id = ''

        if status == 'Закрыта' and status_before != status:
            self.conn.update_admin_application_query(status, responsible, dispatcher_id, id, closing_date='now')
        elif status == 'В работе' and status_before != status:
            self.conn.update_admin_application_query(status, responsible, dispatcher_id, id)
            self.conn.del_admin_closing_date(id)
        else:
            self.conn.update_admin_application_query(status, responsible, dispatcher_id, id)

        self.view_admin_data_of_applications()

        self.admin_app_processing.close()

    def open_admin_window(self):
        self.income.close()

        self.admin_window = QtWidgets.QMainWindow()
        self.ui_admin_window = main_form_MainWindow()
        self.ui_admin_window.setupUi(self.admin_window)

        self.wndw = self.ui_admin_window
        self.view_admin_data_of_applications()
        self.view_admin_data_of_users()

        self.fill_responsible_combobox(self.ui_admin_window)
        self.ui_admin_window.status_comboBox.setCurrentIndex(-1)
        self.ui_admin_window.responsible_comboBox.setCurrentIndex(-1)

        self.ui_admin_window.filtrationFrame.installEventFilter(self)
        self.fill_combobox(self.ui_admin_window.region_comboBox, self.get_region())
        self.ui_admin_window.region_comboBox.currentIndexChanged.connect(
            lambda f: self.update_cities_by_region(window=self.ui_admin_window)
        )
        self.ui_admin_window.city_comboBox.currentIndexChanged.connect(
            lambda f: self.update_streets_by_city(window=self.ui_admin_window)
        )
        self.ui_admin_window.city_radioButton.clicked.connect(
            lambda f: self.update_cities_by_radioButton("Город", self.ui_admin_window)
        )
        self.ui_admin_window.locality_radioButton.clicked.connect(
            lambda f: self.update_cities_by_radioButton("Населенный пункт", self.ui_admin_window)
        )

        self.ui_admin_window.menubar.setStyleSheet("""
                                    QMenuBar {
                                        color: white;
                                        font-size: 10pt;
                                        font-family: Arial;
                                    }

                                    QMenuBar::item:selected {
                                        background-color: rgb(69, 91, 133);
                                        font-size: 10pt;
                                        font-family: Arial;
                                    }

                                    QMenu {
                                        background-color: rgb(69, 91, 133);
                                        color: white;
                                        font-size: 10pt;
                                        font-family: Arial;
                                    }

                                    QMenu::item:selected {
                                        background-color: rgb(69, 91, 133);
                                        color: rgb(210, 226, 250);
                                    }
                                """)
        self.ui_admin_window.menu_2.setTitle(self.login)
        self.ui_admin_window.about_as_action.triggered.connect(self.open_program_info_window)
        self.ui_admin_window.logout_action.triggered.connect(
            lambda f: self.logout_program(self.admin_window)
        )
        self.ui_admin_window.add_user_panel.triggered.connect(self.admin_show_user_panel)
        self.ui_admin_window.delete_user_panel.triggered.connect(self.admin_hide_user_panel)
        self.ui_admin_window.simple_filtration_2.triggered.connect(
            lambda f: self.simple_filtration(self.ui_admin_window)
        )
        self.ui_admin_window.advanced_filtration_2.triggered.connect(
            lambda f: self.advanced_filtration(self.ui_admin_window)
        )

        self.ui_admin_window.createAppButton.hide()

        self.admin_window.show()

        self.create_calendar_date_of_creation_after()
        self.create_calendar_date_of_creation_before()
        self.create_calendar_closing_date_after()
        self.create_calendar_closing_date_before()

        self.ui_admin_window.line_date_of_creation_after.mousePressEvent = self.show_calendar_date_of_creation_after
        self.calendar_date_of_creation_after.clicked.connect(self.set_date_of_creation_after)
        self.ui_admin_window.line_date_of_creation_before.mousePressEvent = self.show_calendar_date_of_creation_before
        self.calendar_date_of_creation_before.clicked.connect(self.set_date_of_creation_before)
        self.ui_admin_window.line_closing_date_after.mousePressEvent = self.show_calendar_closing_date_after
        self.calendar_closing_date_after.clicked.connect(self.set_closing_date_after)
        self.ui_admin_window.line_cloxing_date_before.mousePressEvent = self.show_calendar_closing_date_before
        self.calendar_closing_date_before.clicked.connect(self.set_closing_date_before)

        self.ui_admin_window.tableView_applications.doubleClicked.connect(self.open_admin_app_processing_window)
        self.ui_admin_window.tableView_users.doubleClicked.connect(self.open_admin_user_processing_window)

        self.ui_admin_window.find_user_btn.clicked.connect(self.admin_find_user)
        self.ui_admin_window.select_all_btn_.clicked.connect(self.admin_select_all_users)
        self.ui_admin_window.reset_select_btn_.clicked.connect(self.admin_reset_select_users)
        self.ui_admin_window.filtrationBtn.clicked.connect(
            lambda f: self.filtration_data(self.ui_admin_window)
        )
        self.ui_admin_window.reset_filtrationBtn.clicked.connect(
            lambda f: self.reset_filtration(self.ui_admin_window)
        )
        self.ui_admin_window.processingUserButton.clicked.connect(self.open_admin_user_processing_window)
        self.ui_admin_window.processingAppButton.clicked.connect(self.open_admin_app_processing_window)
        self.ui_admin_window.reportsAppsButton.clicked.connect(self.admin_create_and_open_report)

    def admin_show_user_panel(self):
        self.ui_admin_window.frame_3.show()
        self.ui_admin_window.processingUserButton.show()
        self.ui_admin_window.reportsAppsButton.show()

    def admin_hide_user_panel(self):
        self.ui_admin_window.frame_3.hide()
        self.ui_admin_window.processingUserButton.hide()
        self.ui_admin_window.reportsAppsButton.hide()

    def admin_select_all_users(self):
        model = self.admin_user_model
        for row in range(model.rowCount()):
            index = model.index(row, 0)
            model.setData(index, True, Qt.ItemDataRole.CheckStateRole)

    def admin_reset_select_users(self):
        model = self.admin_user_model
        for row in range(model.rowCount()):
            index = model.index(row, 0)
            model.setData(index, False, Qt.ItemDataRole.CheckStateRole)

    def admin_find_user(self):
        filter = self.ui_admin_window.id_lineEdit.text()
        self.view_admin_data_of_users(filter)

    def open_admin_user_processing_window(self):
        self.admin_user_processing = QtWidgets.QMainWindow()
        self.ui_admin_user_processing = admin_user_processing_MainWindow()
        self.ui_admin_user_processing.setupUi(self.admin_user_processing)

        try:
            index_role = self.ui_admin_window.tableView_users.selectedIndexes()[1]
        except:
            self.open_select_error()
            return
        role = self.ui_admin_window.tableView_users.model().data(index_role)
        index_login = self.ui_admin_window.tableView_users.selectedIndexes()[3]
        login = self.ui_admin_window.tableView_users.model().data(index_login)

        if role in ['admin', 'dispatcher']:
            self.ui_admin_user_processing.roleComboBox.setCurrentText(role)
        else:
            self.ui_admin_user_processing.roleComboBox.setCurrentIndex(-1)
        self.ui_admin_user_processing.line_login.setText(login)

        self.admin_user_processing.show()

        self.ui_admin_user_processing.processingButton.clicked.connect(self.user_processing)
        self.ui_admin_user_processing.canselButton.clicked.connect(self.admin_user_undo_action)

    def admin_user_undo_action(self):
        self.admin_user_processing.close()
        self.view_admin_data_of_users()

    def open_admin_app_processing_window(self):
        self.admin_app_processing = QtWidgets.QMainWindow()
        self.ui_admin_app_processing = admin_application_processing_MainWindow()
        self.ui_admin_app_processing.setupUi(self.admin_app_processing)

        try:
            index_app = self.ui_admin_window.tableView_applications.selectedIndexes()[0]
        except:
            self.open_select_error()
            return
        app_id = self.ui_admin_window.tableView_applications.model().data(index_app)

        cursor = self.conn.cursor
        sql_query = f"SELECT status, responsible, responsible_mngr FROM applications WHERE application_id = '{app_id}'"
        cursor.execute(sql_query)
        status, responsible, responsible_mngr = cursor.fetchall()[0]

        sql_query = f"SELECT name FROM responsibles"
        cursor.execute(sql_query)
        data = [i[0] for i in cursor.fetchall()]

        self.fill_combobox(self.ui_admin_app_processing.responsibleComboBox, data)

        self.ui_admin_app_processing.line_dispatcher.setText(str(responsible_mngr))
        self.ui_admin_app_processing.statusComboBox.setPlaceholderText(status)
        self.ui_admin_app_processing.statusComboBox.setCurrentIndex(-1)
        self.ui_admin_app_processing.responsibleComboBox.setCurrentText(responsible)

        self.admin_app_processing.show()

        self.ui_admin_app_processing.processingButton.clicked.connect(self.application_processing)
        self.ui_admin_app_processing.canselButton.clicked.connect(self.admin_app_undo_action)

    def admin_app_undo_action(self):
        self.admin_app_processing.close()
        self.view_admin_data_of_applications()

    def admin_create_and_open_report(self):
        data = []
        checked_data = []
        checked_rows = []

        model = self.admin_user_model

        for row in range(model.rowCount()):
            if model.data(model.index(row, 0), Qt.CheckStateRole) == Qt.CheckState.Checked:
                checked_rows.append(row)

        if len(checked_rows) == 0:
            self.open_select_error()
            return
        else:

            for row in checked_rows:
                index = model.index(row, 1)
                checked_data.append(model.data(index, Qt.DisplayRole))

            str_of_users = (', ').join(checked_data)

            cursor = self.conn.cursor
            sql_query = f"SELECT user_id, full_name, role FROM users WHERE user_id IN ({str_of_users})"
            cursor.execute(sql_query)
            result = cursor.fetchall()

            for row in result:
                user_id, name, role = row

                if role == USER_ROLES[1]:
                    sql_query = f"SELECT application_id FROM applications WHERE responsible_mngr = '{user_id}' and status = 'Закрыта'"
                elif role == USER_ROLES[2]:
                    sql_query = f"SELECT application_id FROM applications WHERE creator = '{user_id}'"
                cursor.execute(sql_query)
                count_of_apps = len(cursor.fetchall())

                data.append((user_id, name, role, count_of_apps))

            self.doc.create_work_for_apps_report(data)

            self.doc.open_file(
                rf"resources\documents\work_report{str(date.today().day).zfill(2)}{str(date.today().month).zfill(2)}{str(date.today().year).zfill(2)}.xlsx")

    def view_dispatcher_data(self, filter=None, params=None):
        cursor = self.conn.cursor

        table_view = self.ui_dispatcher_window.tableView_applications

        if params is not None:
            if "status" not in params:
                key = "responsible_mngr"
                value = params.pop(key)
                string_query_dict = ' and '.join([f"{k}='{v}'" for k, v in params.items()])
                sql_query = f"SELECT application_id, status, creator, fio, description, address, responsible, TO_CHAR(date_of_creation, 'DD-MM-YYYY'), TO_CHAR(date_of_adoption, 'DD-MM-YYYY'), TO_CHAR(closing_date, 'DD-MM-YYYY') FROM applications WHERE " + string_query_dict + f" and (status = 'Новая' OR {key} = '{value}')"
            else:
                string_query_dict = ' and '.join([f"{k}='{v}'" for k, v in params.items()])
                sql_query = "SELECT application_id, status, creator, fio, description, address, responsible, TO_CHAR(date_of_creation, 'DD-MM-YYYY'), TO_CHAR(date_of_adoption, 'DD-MM-YYYY'), TO_CHAR(closing_date, 'DD-MM-YYYY') FROM applications WHERE " + string_query_dict

        else:
            sql_query = f"SELECT application_id, status, creator, fio, description, address, responsible, TO_CHAR(date_of_creation, 'DD-MM-YYYY'), TO_CHAR(date_of_adoption, 'DD-MM-YYYY'), TO_CHAR(closing_date, 'DD-MM-YYYY') FROM applications WHERE responsible_mngr = '{self.user_id}' OR status = 'Новая'"

        cursor.execute(sql_query)
        headers = ['№ заявки', 'Статус', 'Оператор', 'ФИО заявителя', 'Описание', 'Адрес', 'Ответственный',
                   'Дата создания',
                   'Дата начала обработки', 'Дата закрытия']

        rows = cursor.fetchall()

        result = [[el if el is not None else '' for el in row] for row in rows]

        for row in result:
            user_id = row[2]
            sql_query = f"SELECT full_name FROM users WHERE user_id = '{user_id}'"
            cursor.execute(sql_query)
            row[2] = cursor.fetchall()[0][0]

        self.dispatcher_model = TableModel(result, headers)

        header = table_view.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        header.setStretchLastSection(True)
        header.setOffsetToLastSection()
        header.setSectionsMovable(True)
        header.setFirstSectionMovable(False)
        header.sectionClicked.connect(
            lambda f: self.set_color(self.dispatcher_model)
        )

        table_view.verticalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        table_view.setTextElideMode(Qt.TextElideMode.ElideMiddle)
        table_view.setWordWrap(True)
        table_view.verticalHeader().setDefaultAlignment(Qt.AlignmentFlag.AlignTop)

        self.set_color(self.dispatcher_model)

        table_view.setModel(self.dispatcher_model)

        table_view.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)

    def set_color(self, model):
        for row in range(model.rowCount()):
            col = model.column_by_name('Статус')
            index = model.index(row, col)
            status = model.data(index)
            if status == 'Новая':
                model.setData(index, QColor(Qt.GlobalColor.cyan), Qt.ItemDataRole.ForegroundRole)
            elif status == 'В работе':
                model.setData(index, QColor(Qt.GlobalColor.yellow), Qt.ItemDataRole.ForegroundRole)
            elif status == 'Выполнена':
                model.setData(index, QColor(Qt.GlobalColor.green), Qt.ItemDataRole.ForegroundRole)
            elif status == 'Закрыта':
                model.setData(index, QColor(Qt.GlobalColor.color0), Qt.ItemDataRole.ForegroundRole)

            if row % 2 == 1:
                for col in range(model.columnCount()):
                    index = model.index(row, col)
                    model.setData(index, QColor(95, 126, 184), Qt.ItemDataRole.BackgroundRole)

    def fill_responsible_combobox(self, window):
        for i in self.dispatcher_get_responsibles():
            window.responsible_comboBox.addItem(i)

    def show_calendar_date_of_creation_after(self, event):
        window = self.wndw
        self.calendar_date_of_creation_after.show()
        geometry = window.line_date_of_creation_after.geometry()
        pos = window.line_date_of_creation_after.mapToGlobal(
            QtCore.QPoint(0, window.line_date_of_creation_after.height()))
        rect = QtCore.QRect(pos, geometry.size())
        self.calendar_date_of_creation_after.setGeometry(rect)

    def show_calendar_closing_date_after(self, event):
        window = self.wndw
        self.calendar_closing_date_after.show()
        geometry = window.line_closing_date_after.geometry()
        pos = window.line_closing_date_after.mapToGlobal(
            QtCore.QPoint(0, window.line_closing_date_after.height()))
        rect = QtCore.QRect(pos, geometry.size())
        self.calendar_closing_date_after.setGeometry(rect)

    def set_date_of_creation_after(self, date):
        window = self.wndw
        window.line_date_of_creation_after.setText(date.toString('dd MM yyyy'))
        self.calendar_date_of_creation_after.hide()

    def set_closing_date_after(self, date):
        window = self.wndw
        window.line_closing_date_after.setText(date.toString('dd MM yyyy'))
        self.calendar_closing_date_after.hide()

    def show_calendar_date_of_creation_before(self, event):
        window = self.wndw
        self.calendar_date_of_creation_before.show()
        geometry = window.line_date_of_creation_before.geometry()
        pos = window.line_date_of_creation_before.mapToGlobal(
            QtCore.QPoint(0, window.line_date_of_creation_before.height()))
        rect = QtCore.QRect(pos, geometry.size())
        self.calendar_date_of_creation_before.setGeometry(rect)

    def show_calendar_closing_date_before(self, event):
        window = self.wndw
        self.calendar_closing_date_before.show()
        geometry = window.line_cloxing_date_before.geometry()
        pos = window.line_cloxing_date_before.mapToGlobal(
            QtCore.QPoint(0, window.line_cloxing_date_before.height()))
        rect = QtCore.QRect(pos, geometry.size())
        self.calendar_closing_date_before.setGeometry(rect)

    def set_date_of_creation_before(self, date):
        window = self.wndw
        window.line_date_of_creation_before.setText(date.toString('dd MM yyyy'))
        self.calendar_date_of_creation_before.hide()

    def set_closing_date_before(self, date):
        window = self.wndw
        window.line_cloxing_date_before.setText(date.toString('dd MM yyyy'))
        self.calendar_closing_date_before.hide()

    def create_calendar_date_of_creation_after(self):
        self.calendar_date_of_creation_after = QCalendarWidget()
        self.calendar_date_of_creation_after.setWindowTitle('Calendar')
        self.calendar_date_of_creation_after.setVerticalHeaderFormat(
            QCalendarWidget.VerticalHeaderFormat.NoVerticalHeader)
        self.calendar_date_of_creation_after.setFixedSize(self.calendar_date_of_creation_after.sizeHint())
        self.calendar_date_of_creation_after.setWindowFlags(self.calendar_date_of_creation_after.windowFlags())
        self.calendar_date_of_creation_after.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)

    def create_calendar_closing_date_after(self):
        self.calendar_closing_date_after = QCalendarWidget()
        self.calendar_closing_date_after.setWindowTitle('Calendar')
        self.calendar_closing_date_after.setVerticalHeaderFormat(QCalendarWidget.VerticalHeaderFormat.NoVerticalHeader)
        self.calendar_closing_date_after.setFixedSize(self.calendar_date_of_creation_after.sizeHint())
        self.calendar_closing_date_after.setWindowFlags(self.calendar_date_of_creation_after.windowFlags())
        self.calendar_closing_date_after.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)

    def create_calendar_date_of_creation_before(self):
        self.calendar_date_of_creation_before = QCalendarWidget()
        self.calendar_date_of_creation_before.setWindowTitle('Calendar')
        self.calendar_date_of_creation_before.setVerticalHeaderFormat(
            QCalendarWidget.VerticalHeaderFormat.NoVerticalHeader)
        self.calendar_date_of_creation_before.setFixedSize(self.calendar_date_of_creation_before.sizeHint())
        self.calendar_date_of_creation_before.setWindowFlags(self.calendar_date_of_creation_before.windowFlags())
        self.calendar_date_of_creation_before.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)

    def create_calendar_closing_date_before(self):
        self.calendar_closing_date_before = QCalendarWidget()
        self.calendar_closing_date_before.setWindowTitle('Calendar')
        self.calendar_closing_date_before.setVerticalHeaderFormat(QCalendarWidget.VerticalHeaderFormat.NoVerticalHeader)
        self.calendar_closing_date_before.setFixedSize(self.calendar_date_of_creation_before.sizeHint())
        self.calendar_closing_date_before.setWindowFlags(self.calendar_date_of_creation_before.windowFlags())
        self.calendar_closing_date_before.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)

    def eventFilter(self, obj, event, frame=None):
        if self.user_role == USER_ROLES[1]:
            if obj == self.ui_dispatcher_window.filtrationFrame and event.type() == QtCore.QEvent.Type.KeyPress:
                if event.key() == QtCore.Qt.Key.Key_Return or event.key() == QtCore.Qt.Key.Key_Enter:
                    self.filtration_data(self.ui_dispatcher_window)
                    return True
            return super().eventFilter(obj, event)
        elif self.user_role == USER_ROLES[2]:
            if obj == self.ui_user_window.filtrationFrame and event.type() == QtCore.QEvent.Type.KeyPress:
                if event.key() == QtCore.Qt.Key.Key_Return or event.key() == QtCore.Qt.Key.Key_Enter:
                    self.filtration_data(self.ui_user_window)
                    return True
            return super().eventFilter(obj, event)
        elif self.user_role == USER_ROLES[0]:
            if obj == self.ui_admin_window.filtrationFrame and event.type() == QtCore.QEvent.Type.KeyPress:
                if event.key() == QtCore.Qt.Key.Key_Return or event.key() == QtCore.Qt.Key.Key_Enter:
                    self.filtration_data(self.ui_admin_window)
                    return True
            return super().eventFilter(obj, event)

    def open_link(self, url):
        QDesktopServices.openUrl(QUrl(url))

    def open_program_info_window(self):
        self.program_info_window = QtWidgets.QMainWindow()
        self.ui_program_info_window = program_info_MainWindow()
        self.ui_program_info_window.setupUi(self.program_info_window)

        self.ui_program_info_window.link_label.setOpenExternalLinks(True)
        self.ui_program_info_window.link_label.linkActivated.connect(self.open_link)

        self.program_info_window.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)

        movie = QMovie(r"resources/icons/ew.gif")
        label_gif = self.ui_program_info_window.label_gif
        label_gif.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_gif.setMovie(movie)
        movie.start()

        self.program_info_window.show()

        self.ui_program_info_window.exit_btm.clicked.connect(self.program_info_window.close)

    def logout_program(self, window):
        window.close()
        self.open_income_window()

    def open_dispatcher_window(self):
        self.income.close()

        self.dispatcher_window = QtWidgets.QMainWindow()
        self.ui_dispatcher_window = main_form_MainWindow()
        self.ui_dispatcher_window.setupUi(self.dispatcher_window)

        self.wndw = self.ui_dispatcher_window

        self.view_dispatcher_data()
        self.fill_responsible_combobox(self.ui_dispatcher_window)
        self.ui_dispatcher_window.status_comboBox.setCurrentIndex(-1)
        self.ui_dispatcher_window.responsible_comboBox.setCurrentIndex(-1)

        self.ui_dispatcher_window.filtrationFrame.installEventFilter(self)

        self.fill_combobox(self.ui_dispatcher_window.region_comboBox, self.get_region())
        self.ui_dispatcher_window.region_comboBox.currentIndexChanged.connect(
            lambda f: self.update_cities_by_region(window=self.ui_dispatcher_window)
        )
        self.ui_dispatcher_window.city_comboBox.currentIndexChanged.connect(
            lambda f: self.update_streets_by_city(window=self.ui_dispatcher_window)
        )
        self.ui_dispatcher_window.city_radioButton.clicked.connect(
            lambda f: self.update_cities_by_radioButton("Город", self.ui_dispatcher_window)
        )
        self.ui_dispatcher_window.locality_radioButton.clicked.connect(
            lambda f: self.update_cities_by_radioButton("Населенный пункт", self.ui_dispatcher_window)
        )

        self.ui_dispatcher_window.menubar.setStyleSheet("""
                            QMenuBar {
                                color: white;
                                font-size: 10pt;
                                font-family: Arial;
                            }

                            QMenuBar::item:selected {
                                background-color: rgb(69, 91, 133);
                                font-size: 10pt;
                                font-family: Arial;
                            }

                            QMenu {
                                background-color: rgb(69, 91, 133);
                                color: white;
                                font-size: 10pt;
                                font-family: Arial;
                            }

                            QMenu::item:selected {
                                background-color: rgb(69, 91, 133);
                                color: rgb(210, 226, 250);
                            }
                        """)
        self.ui_dispatcher_window.menu_2.setTitle(self.login)
        self.ui_dispatcher_window.about_as_action.triggered.connect(self.open_program_info_window)
        self.ui_dispatcher_window.logout_action.triggered.connect(
            lambda f: self.logout_program(self.dispatcher_window)
        )
        self.ui_dispatcher_window.add_user_panel.triggered.connect(self.open_permission_error_window)

        self.ui_dispatcher_window.simple_filtration_2.triggered.connect(
            lambda f: self.simple_filtration(self.ui_dispatcher_window)
        )
        self.ui_dispatcher_window.advanced_filtration_2.triggered.connect(
            lambda f: self.advanced_filtration(self.ui_dispatcher_window)
        )

        self.ui_dispatcher_window.frame_3.hide()
        self.ui_dispatcher_window.processingUserButton.hide()
        self.ui_dispatcher_window.createAppButton.hide()
        self.ui_dispatcher_window.reportsAppsButton.hide()

        self.dispatcher_window.show()

        self.create_calendar_date_of_creation_after()
        self.create_calendar_date_of_creation_before()
        self.create_calendar_closing_date_after()
        self.create_calendar_closing_date_before()

        self.ui_dispatcher_window.line_date_of_creation_after.mousePressEvent = self.show_calendar_date_of_creation_after
        self.calendar_date_of_creation_after.clicked.connect(self.set_date_of_creation_after)
        self.ui_dispatcher_window.line_date_of_creation_before.mousePressEvent = self.show_calendar_date_of_creation_before
        self.calendar_date_of_creation_before.clicked.connect(self.set_date_of_creation_before)
        self.ui_dispatcher_window.line_closing_date_after.mousePressEvent = self.show_calendar_closing_date_after
        self.calendar_closing_date_after.clicked.connect(self.set_closing_date_after)
        self.ui_dispatcher_window.line_cloxing_date_before.mousePressEvent = self.show_calendar_closing_date_before
        self.calendar_closing_date_before.clicked.connect(self.set_closing_date_before)

        self.ui_dispatcher_window.tableView_applications.doubleClicked.connect(
            self.open_dispatcher_application_processing_window)

        self.ui_dispatcher_window.processingAppButton.clicked.connect(
            self.open_dispatcher_application_processing_window)
        self.ui_dispatcher_window.filtrationBtn.clicked.connect(
            lambda f: self.filtration_data(self.ui_dispatcher_window)
        )
        self.ui_dispatcher_window.reset_filtrationBtn.clicked.connect(
            lambda f: self.reset_filtration(self.ui_dispatcher_window)
        )

    def simple_filtration(self, window):
        self.reset_filtration(window)
        window.region_comboBox.hide()
        window.city_comboBox.hide()
        window.street_comboBox.hide()
        window.city_radioButton.hide()
        window.locality_radioButton.hide()
        window.line_closing_date_after.hide()
        window.line_cloxing_date_before.hide()
        window.line_date_of_creation_after.hide()
        window.line_date_of_creation_before.hide()
        window.label_4.hide()
        window.label_5.hide()

    def advanced_filtration(self, window):
        self.reset_filtration(window)
        window.region_comboBox.show()
        window.city_comboBox.show()
        window.street_comboBox.show()
        window.city_radioButton.show()
        window.locality_radioButton.show()
        window.line_closing_date_after.show()
        window.line_cloxing_date_before.show()
        window.line_date_of_creation_after.show()
        window.line_date_of_creation_before.show()
        window.label_4.show()
        window.label_5.show()

    def reset_filtration(self, window):
        window.status_comboBox.setCurrentIndex(-1)
        window.region_comboBox.setCurrentIndex(-1)
        window.street_comboBox.setCurrentIndex(-1)
        window.city_comboBox.setCurrentIndex(-1)
        window.responsible_comboBox.setCurrentIndex(-1)
        window.line_date_of_creation_before.clear()
        window.line_date_of_creation_after.clear()
        window.line_cloxing_date_before.clear()
        window.line_closing_date_after.clear()
        if self.user_role == 'admin':
            self.view_admin_data_of_applications()
        elif self.user_role == 'dispatcher':
            self.view_dispatcher_data()
        else:
            self.view_user_data()

    def filtration_data(self, window):
        status = window.status_comboBox.currentText()
        region = window.region_comboBox.currentText()
        city = window.city_comboBox.currentText()
        street = window.street_comboBox.currentText()
        responsible = window.responsible_comboBox.currentText()
        date_of_creation_ot = window.line_date_of_creation_after.text()
        date_of_creation_do = window.line_date_of_creation_before.text()
        closing_date_ot = window.line_closing_date_after.text()
        closing_date_do = window.line_cloxing_date_before.text()
        dispatcher_id = self.user_id

        if self.check_date_filtration(date_of_creation_ot, date_of_creation_do):
            self.open_date_filtration_error()
            return

        if self.check_date_filtration(closing_date_ot, closing_date_do):
            self.open_date_filtration_error()
            return

        dict_query = {'status': status, 'region': region, 'city': city, 'street': street, 'responsible': responsible,
                      'date_of_creation >': date_of_creation_ot, 'date_of_creation <': date_of_creation_do,
                      'closing_date >': closing_date_ot, 'closing_date <': closing_date_do}

        dict_query = {i: dict_query[i] for i in dict_query.keys() if len(str(dict_query[i])) != 0}

        if status != "Новая" and len(dict_query) != 0 and self.user_role == 'dispatcher':
            dict_query["responsible_mngr"] = dispatcher_id

        if len(dict_query) != 0:
            if self.user_role == 'dispatcher':
                self.view_dispatcher_data(params=dict_query)
            elif self.user_role == 'admin':
                self.view_admin_data_of_applications(params=dict_query)
            else:
                self.view_user_data(params=dict_query)

    def open_dispatcher_application_processing_window(self):
        self.app_processing = QtWidgets.QMainWindow()
        self.ui_app_processing = dispatcher_app_processing_MainWindow()
        self.ui_app_processing.setupUi(self.app_processing)

        for i in self.dispatcher_get_responsibles():
            self.ui_app_processing.responsibleComboBox.addItem(i)

        try:
            index_apps = self.ui_dispatcher_window.tableView_applications.selectedIndexes()[0]
        except:
            self.open_select_error()
            return
        id = self.ui_dispatcher_window.tableView_applications.model().data(index_apps)
        cursor = self.conn.cursor
        sql_query = f"SELECT description, status, responsible, region, city, street, house_number, room, city_type FROM applications WHERE application_id={id}"
        cursor.execute(sql_query)

        description, self.dispatcher_status, responsible, region, city, street, house_number, room, city_type = \
            cursor.fetchall()[0]

        self.fill_combobox(self.ui_app_processing.region_comboBox, self.get_region())

        if city_type == 'Населенный пункт':
            self.ui_app_processing.locality_radioButton.setChecked(True)
            self.ui_app_processing.city_comboBox.setPlaceholderText(city_type)

        self.ui_app_processing.region_comboBox.currentIndexChanged.connect(
            lambda f: self.update_cities_by_region(window=self.ui_app_processing)
        )
        self.ui_app_processing.city_comboBox.currentIndexChanged.connect(
            lambda f: self.update_streets_by_city(window=self.ui_app_processing)
        )

        self.ui_app_processing.city_radioButton.clicked.connect(
            lambda f: self.update_cities_by_radioButton("Город", self.ui_app_processing)
        )
        self.ui_app_processing.locality_radioButton.clicked.connect(
            lambda f: self.update_cities_by_radioButton("Населенный пункт", self.ui_app_processing)
        )

        self.ui_app_processing.text_description.setText(description)
        self.ui_app_processing.responsibleComboBox.setCurrentText(responsible)
        self.ui_app_processing.region_comboBox.setCurrentText(region)
        self.ui_app_processing.city_comboBox.setCurrentText(city)
        self.ui_app_processing.street_comboBox.setCurrentText(street)
        self.ui_app_processing.line_number_house.setText(house_number)
        self.ui_app_processing.line_number_room.setText(room)
        self.ui_app_processing.statusComboBox.setPlaceholderText(self.dispatcher_status)
        if self.dispatcher_status in ['Новая', 'Закрыта']:
            self.ui_app_processing.statusComboBox.setCurrentIndex(-1)
        else:
            self.ui_app_processing.statusComboBox.setCurrentText(self.dispatcher_status)

        self.app_processing.show()

        self.ui_app_processing.process_button.clicked.connect(self.edit_dispatcher_application)
        self.ui_app_processing.canselButton.clicked.connect(self.dispatcher_app_undo_action)

    def dispatcher_get_responsibles(self):
        cursor = self.conn.cursor
        sql_query = "SELECT name FROM responsibles"
        cursor.execute(sql_query)
        result = list()
        for i in cursor.fetchall():
            result.append(i[0])
        return result

    def dispatcher_app_undo_action(self):
        self.app_processing.close()
        self.view_dispatcher_data()

    def edit_dispatcher_application(self):
        index = self.ui_dispatcher_window.tableView_applications.selectedIndexes()[0]
        id = self.ui_dispatcher_window.tableView_applications.model().data(index)

        description = self.ui_app_processing.text_description.toPlainText()
        region = self.ui_app_processing.region_comboBox.currentText()
        city = self.ui_app_processing.city_comboBox.currentText()
        city_type = self.ui_app_processing.city_comboBox.placeholderText()
        street = self.ui_app_processing.street_comboBox.currentText()
        house_number = self.ui_app_processing.line_number_house.text()
        room = self.ui_app_processing.line_number_room.text()
        status = self.ui_app_processing.statusComboBox.currentText()
        responsible = self.ui_app_processing.responsibleComboBox.currentText()
        dispatcher_id = self.user_id

        address = f'{region}, {CITY_TYPE[city_type]}{city}, ул.{street}, д.{house_number}, кв.{room}'

        if self.dispatcher_status == 'Закрыта':
            pass
        else:
            if '' in [description, status, responsible, region, city, street, house_number, room]:
                self.open_padding_error_window()
                return

            self.conn.update_dispatcher_application_query(self.dispatcher_status, description, address, region, city,
                                                          street, house_number, room, status, responsible,
                                                          dispatcher_id, city_type, id)

        self.view_dispatcher_data()

        self.app_processing.close()

    def view_user_data(self, params=None):
        cursor = self.conn.cursor

        table_view = self.ui_user_window.tableView_applications

        if params is not None:
            string_query_dict = ' and '.join([f"{k}='{v}'" for k, v in params.items()])
            sql_query = f"SELECT application_id, status, fio, description, address, responsible, TO_CHAR(date_of_creation, 'DD MM YYYY'), TO_CHAR(date_of_adoption, 'DD MM YYYY'), TO_CHAR(closing_date, 'DD MM YYYY') FROM applications WHERE creator = '{self.user_id}' and " + string_query_dict
        else:
            sql_query = f"SELECT application_id, status, fio, description, address, responsible, TO_CHAR(date_of_creation, 'DD MM YYYY'), TO_CHAR(date_of_adoption, 'DD MM YYYY'), TO_CHAR(closing_date, 'DD MM YYYY') FROM applications WHERE creator = '{self.user_id}'"

        cursor.execute(sql_query)
        headers = ['№ заявки', 'Статус', 'ФИО заявителя', 'Описание', 'Адрес', 'Ответственный', 'Дата создания',
                   'Дата начала обработки', 'Дата закрытия']
        rows = cursor.fetchall()

        result = [[el if el is not None else '' for el in row] for row in rows]

        self.user_model = TableModel(result, headers)

        header = table_view.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        header.setStretchLastSection(True)
        header.setOffsetToLastSection()
        header.setSectionsMovable(True)
        header.setFirstSectionMovable(False)
        header.sectionClicked.connect(
            lambda f: self.set_color(self.user_model)
        )

        table_view.verticalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        table_view.setTextElideMode(Qt.TextElideMode.ElideMiddle)
        table_view.setWordWrap(True)
        table_view.verticalHeader().setDefaultAlignment(Qt.AlignmentFlag.AlignTop)

        self.set_color(self.user_model)

        table_view.setModel(self.user_model)
        table_view.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)

    @staticmethod
    def check_date_filtration(date_ot, date_do):
        if len(date_ot) * len(date_do) != 0:
            d1, m1, y1 = [int(i) for i in date_ot.split(' ')]
            d2, m2, y2 = [int(i) for i in date_do.split(' ')]
            date1 = datetime.date(y1, m1, d1)
            date2 = datetime.date(y2, m2, d2)
            return date1 > date2

    def open_db_connect_error_window(self):
        self.db_connect_error_window = QtWidgets.QMainWindow()
        self.ui_db_connect_error_window = db_connect_error_MainWindow()
        self.ui_db_connect_error_window.setupUi(self.db_connect_error_window)

        self.db_connect_error_window.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)

        self.db_connect_error_window.show()

        self.ui_db_connect_error_window.exit_btm.clicked.connect(self.db_connect_error_window.close)

    def open_income_error_window(self):
        self.income_error_window = QtWidgets.QMainWindow()
        self.ui_income_error_window = income_error_MainWindow()
        self.ui_income_error_window.setupUi(self.income_error_window)

        self.income_error_window.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)

        self.income_error_window.show()

        self.ui_income_error_window.exit_btm.clicked.connect(self.income_error_window.close)

    def open_permission_error_window(self):
        self.permission_error_window = QtWidgets.QMainWindow()
        self.ui_permission_error_window = permission_error_MainWindow()
        self.ui_permission_error_window.setupUi(self.permission_error_window)

        self.permission_error_window.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)

        self.permission_error_window.show()

        self.ui_permission_error_window.exit_btm.clicked.connect(self.permission_error_window.close)

    def open_padding_error_window(self):
        self.padding_error_window = QtWidgets.QMainWindow()
        self.ui_padding_error_window = padding_error_MainWindow()
        self.ui_padding_error_window.setupUi(self.padding_error_window)

        self.padding_error_window.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)

        self.padding_error_window.show()

        self.ui_padding_error_window.exit_btm.clicked.connect(self.padding_error_window.close)

    def open_select_error(self):
        self.select_error_window = QtWidgets.QMainWindow()
        self.ui_select_error_window = select_error_MainWindow()
        self.ui_select_error_window.setupUi(self.select_error_window)

        self.select_error_window.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)

        self.select_error_window.show()

        self.ui_select_error_window.exit_btm_2.clicked.connect(self.select_error_window.close)

    def open_date_filtration_error(self):
        self.date_filtration_error_window = QtWidgets.QMainWindow()
        self.ui_date_filtration_error_window = date_filtration_error_MainWindow()
        self.ui_date_filtration_error_window.setupUi(self.date_filtration_error_window)

        self.date_filtration_error_window.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)

        self.date_filtration_error_window.show()

        self.ui_date_filtration_error_window.exit_btm.clicked.connect(self.date_filtration_error_window.close)

    def open_registration_window(self):
        self.income.hide()

        self.reg_window = QtWidgets.QMainWindow()
        self.ui_reg_window = reg_MainWindow()
        self.ui_reg_window.setupUi(self.reg_window)
        self.reg_window.show()

        self.ui_reg_window.registrationButton.clicked.connect(self.add_new_user)
        self.ui_reg_window.canselButton.clicked.connect(self.user_reg_undo_action)

    def open_income_window(self):
        self.income = QtWidgets.QMainWindow()
        self.income_ui = income_MainWindow()
        self.income_ui.setupUi(self.income)
        self.income.show()

        self.income_ui.incomeButton.clicked.connect(self.open_user_window)
        self.income_ui.registrationButton.clicked.connect(self.open_registration_window)

    def open_user_window(self):
        self.login = self.income_ui.line_login.text()
        password = self.income_ui.line_password.text()

        if not self.conn.check_user_login_password_query(self.login, password):
            self.open_income_error_window()
            return

        cursor = self.conn.cursor
        sql_query = f"SELECT user_id FROM users WHERE login = '{self.login}'"
        cursor.execute(sql_query)
        self.user_id = cursor.fetchall()[0][0]

        sql_query = f"SELECT role FROM users WHERE login = '{self.login}'"
        cursor.execute(sql_query)
        self.user_role = cursor.fetchall()[0][0]

        if self.user_role == USER_ROLES[0]:
            self.open_admin_window()
            return
        elif self.user_role == USER_ROLES[1]:
            self.open_dispatcher_window()
            return

        self.income.close()

        self.user_window = QtWidgets.QMainWindow()
        self.ui_user_window = main_form_MainWindow()
        self.ui_user_window.setupUi(self.user_window)

        self.wndw = self.ui_user_window

        self.view_user_data()
        self.fill_responsible_combobox(self.ui_user_window)
        self.ui_user_window.status_comboBox.setCurrentIndex(-1)
        self.ui_user_window.responsible_comboBox.setCurrentIndex(-1)

        self.ui_user_window.filtrationFrame.installEventFilter(self)

        self.fill_combobox(self.ui_user_window.region_comboBox, self.get_region())
        self.ui_user_window.region_comboBox.currentIndexChanged.connect(
            lambda f: self.update_cities_by_region(window=self.ui_user_window)
        )
        self.ui_user_window.city_comboBox.currentIndexChanged.connect(
            lambda f: self.update_streets_by_city(window=self.ui_user_window)
        )
        self.ui_user_window.city_radioButton.clicked.connect(
            lambda f: self.update_cities_by_radioButton("Город", self.ui_user_window)
        )
        self.ui_user_window.locality_radioButton.clicked.connect(
            lambda f: self.update_cities_by_radioButton("Населенный пункт", self.ui_user_window)
        )

        self.ui_user_window.menubar.setStyleSheet("""
                    QMenuBar {
                        color: white;
                        font-size: 10pt;
                        font-family: Arial;
                    }

                    QMenuBar::item:selected {
                        background-color: rgb(69, 91, 133);
                        font-size: 10pt;
                        font-family: Arial;
                    }

                    QMenu {
                        background-color: rgb(69, 91, 133);
                        color: white;
                        font-size: 10pt;
                        font-family: Arial;
                    }

                    QMenu::item:selected {
                        background-color: rgb(69, 91, 133);
                        color: rgb(210, 226, 250);
                    }
                """)
        self.ui_user_window.menu_2.setTitle(self.login)
        self.ui_user_window.about_as_action.triggered.connect(self.open_program_info_window)
        self.ui_user_window.logout_action.triggered.connect(
            lambda f: self.logout_program(self.user_window)
        )
        self.ui_user_window.add_user_panel.triggered.connect(self.open_permission_error_window)
        
        self.ui_user_window.simple_filtration_2.triggered.connect(
            lambda f: self.simple_filtration(self.ui_user_window)
        )
        self.ui_user_window.advanced_filtration_2.triggered.connect(
            lambda f: self.advanced_filtration(self.ui_user_window)
        )

        self.ui_user_window.frame_3.hide()
        self.ui_user_window.processingUserButton.hide()
        self.ui_user_window.processingAppButton.setText("Редактировать заявку")
        self.ui_user_window.reportsAppsButton.setText("Акт о выполненной заявке")

        self.user_window.show()

        self.create_calendar_date_of_creation_after()
        self.create_calendar_date_of_creation_before()
        self.create_calendar_closing_date_after()
        self.create_calendar_closing_date_before()

        self.ui_user_window.line_date_of_creation_after.mousePressEvent = self.show_calendar_date_of_creation_after
        self.calendar_date_of_creation_after.clicked.connect(self.set_date_of_creation_after)
        self.ui_user_window.line_date_of_creation_before.mousePressEvent = self.show_calendar_date_of_creation_before
        self.calendar_date_of_creation_before.clicked.connect(self.set_date_of_creation_before)
        self.ui_user_window.line_closing_date_after.mousePressEvent = self.show_calendar_closing_date_after
        self.calendar_closing_date_after.clicked.connect(self.set_closing_date_after)
        self.ui_user_window.line_cloxing_date_before.mousePressEvent = self.show_calendar_closing_date_before
        self.calendar_closing_date_before.clicked.connect(self.set_closing_date_before)

        self.ui_user_window.tableView_applications.doubleClicked.connect(
            self.open_user_edit_application_window)

        self.ui_user_window.filtrationBtn.clicked.connect(
            lambda f: self.filtration_data(self.ui_user_window)
        )
        self.ui_user_window.reset_filtrationBtn.clicked.connect(
            lambda f: self.reset_filtration(self.ui_user_window)
        )

        self.ui_user_window.createAppButton.clicked.connect(self.open_user_create_application_window)
        self.ui_user_window.processingAppButton.clicked.connect(self.open_user_edit_application_window)
        self.ui_user_window.reportsAppsButton.clicked.connect(self.user_create_and_open_report)

    def open_user_create_application_window(self):
        self.create_app_window = QtWidgets.QMainWindow()
        self.ui_create_app_window = create_app_MainWindow()
        self.ui_create_app_window.setupUi(self.create_app_window)

        self.fill_combobox(self.ui_create_app_window.region_comboBox, self.get_region())
        self.ui_create_app_window.region_comboBox.currentIndexChanged.connect(
            lambda f: self.update_cities_by_region(window=self.ui_create_app_window)
        )
        self.ui_create_app_window.city_comboBox.currentIndexChanged.connect(
            lambda f: self.update_streets_by_city(window=self.ui_create_app_window)
        )

        self.ui_create_app_window.city_radioButton.clicked.connect(
            lambda f: self.update_cities_by_radioButton("Город", self.ui_create_app_window)
        )

        self.ui_create_app_window.locality_radioButton.clicked.connect(
            lambda f: self.update_cities_by_radioButton("Населенный пункт", self.ui_create_app_window)
        )

        self.create_app_window.show()

        self.ui_create_app_window.create_button.clicked.connect(self.user_add_new_application)
        self.ui_create_app_window.canselButton.clicked.connect(self.user_app_undo_action)

    def update_cities_by_radioButton(self, text, window):
        window.city_comboBox.setPlaceholderText(text)
        self.update_cities_by_region(window=window)

    def update_cities_by_region(self, param=None, window=None):
        window.city_comboBox.clear()
        cursor = self.conn.cursor
        sql_query = f"SELECT region_id FROM region WHERE region_name='{window.region_comboBox.currentText()}'"
        cursor.execute(sql_query)

        self.region_id = cursor.fetchall()[0][0]
        if window.city_comboBox.placeholderText() == "Город":
            self.fill_combobox(window.city_comboBox, self.get_city())
        elif window.city_comboBox.placeholderText() == "Населенный пункт":
            self.fill_combobox(window.city_comboBox, self.get_locality())

    def update_streets_by_city(self, param=None, window=None):
        window.street_comboBox.clear()
        cursor = self.conn.cursor

        if window.city_comboBox.placeholderText() == "Город":
            sql_query = f"SELECT city_id FROM city WHERE city_name='{window.city_comboBox.currentText()}'"
        elif window.city_comboBox.placeholderText() == "Населенный пункт":
            sql_query = f"SELECT locality_id FROM locality WHERE locality_name='{window.city_comboBox.currentText()}'"

        cursor.execute(sql_query)

        self.city_id = cursor.fetchall()[0][0]

        if window.city_comboBox.placeholderText() == "Город":
            self.fill_combobox(window.street_comboBox, self.get_city_street())
        elif window.city_comboBox.placeholderText() == "Населенный пункт":
            self.fill_combobox(window.street_comboBox, self.get_locality_street())

    def fill_combobox(self, combobox, data):
        combobox.clear()
        for i in data:
            combobox.addItem(i)

    def get_locality_street(self):
        cursor = self.conn.cursor
        sql_query = f"SELECT street_name FROM street WHERE locality_id={self.city_id}"
        cursor.execute(sql_query)
        result = list()
        for i in cursor.fetchall():
            result.append(i[0])

        return result

    def get_city_street(self):
        cursor = self.conn.cursor
        sql_query = f"SELECT street_name FROM street WHERE city_id={self.city_id}"
        cursor.execute(sql_query)
        result = list()
        for i in cursor.fetchall():
            result.append(i[0])

        return result

    def get_locality(self):
        cursor = self.conn.cursor
        sql_query = f"SELECT locality_name FROM locality WHERE region_id={self.region_id}"
        cursor.execute(sql_query)
        result = list()
        for i in cursor.fetchall():
            result.append(i[0])
        return result

    def get_city(self):
        cursor = self.conn.cursor
        sql_query = f"SELECT city_name FROM city WHERE region_id={self.region_id}"
        cursor.execute(sql_query)
        result = list()
        for i in cursor.fetchall():
            result.append(i[0])
        return result

    def get_region(self):
        cursor = self.conn.cursor
        sql_query = "SELECT region_name FROM region"
        cursor.execute(sql_query)
        result = list()
        for i in cursor.fetchall():
            result.append(i[0])
        return result

    def user_app_undo_action(self):
        self.create_app_window.close()
        self.view_user_data()

    def user_reg_undo_action(self):
        self.reg_window.close()
        self.open_income_window()

    def open_user_edit_application_window(self):
        self.edit_app_window = QtWidgets.QMainWindow()
        self.ui_edit_app_window = create_app_MainWindow()
        self.ui_edit_app_window.setupUi(self.edit_app_window)

        try:
            index_apps = self.ui_user_window.tableView_applications.selectedIndexes()[0]
        except:
            self.open_select_error()
            return
        id = self.ui_user_window.tableView_applications.model().data(index_apps)

        cursor = self.conn.cursor
        sql_query = f"SELECT description, fio, region, city, street, house_number, room, city_type FROM applications WHERE application_id={id}"
        cursor.execute(sql_query)
        description, fio, region, city, street, house_number, room, city_type = cursor.fetchall()[0]

        if city_type == 'Населенный пункт':
            self.ui_edit_app_window.locality_radioButton.setChecked(True)
            self.ui_edit_app_window.city_comboBox.setPlaceholderText(city_type)

        self.fill_combobox(self.ui_edit_app_window.region_comboBox, self.get_region())
        self.ui_edit_app_window.region_comboBox.currentIndexChanged.connect(
            lambda f: self.update_cities_by_region(window=self.ui_edit_app_window)
        )
        self.ui_edit_app_window.city_comboBox.currentIndexChanged.connect(
            lambda f: self.update_streets_by_city(window=self.ui_edit_app_window)
        )

        self.ui_edit_app_window.city_radioButton.clicked.connect(
            lambda f: self.update_cities_by_radioButton("Город", self.ui_edit_app_window)
        )
        self.ui_edit_app_window.locality_radioButton.clicked.connect(
            lambda f: self.update_cities_by_radioButton("Населенный пункт", self.ui_edit_app_window)
        )

        self.ui_edit_app_window.text_app.setText(description)
        self.ui_edit_app_window.line_fio.setText(fio)
        self.ui_edit_app_window.region_comboBox.setCurrentText(region)
        self.ui_edit_app_window.city_comboBox.setCurrentText(city)
        self.ui_edit_app_window.street_comboBox.setCurrentText(street)
        self.ui_edit_app_window.line_number_house.setText(house_number)
        self.ui_edit_app_window.line_number_room.setText(room)

        self.edit_app_window.show()

        self.ui_edit_app_window.create_button.clicked.connect(self.user_edit_application)
        self.ui_edit_app_window.canselButton.clicked.connect(self.user_edit_app_undo_action)

    def user_edit_app_undo_action(self):
        self.edit_app_window.close()
        self.view_user_data()

    def add_new_user(self):
        full_name = self.ui_reg_window.line_full_name.text()
        login = self.ui_reg_window.line_login.text()
        password = self.ui_reg_window.line_password.text()

        if self.conn.check_user_login_query(login):
            msg = QtWidgets.QMessageBox()
            msg.setText("Подобный логин уже существует")
            msg.setInformativeText("Вы ввели неуникальный логин. Придумайте другой!")
            msg.setWindowTitle("Подобный логин уже существует")
            msg.exec()
            return

        self.conn.add_new_user_query(full_name, login, password)
        self.reg_window.close()
        self.income.show()

    def user_add_new_application(self):
        description = self.ui_create_app_window.text_app.toPlainText()
        fio = self.ui_create_app_window.line_fio.text()
        region = self.ui_create_app_window.region_comboBox.currentText()
        city = self.ui_create_app_window.city_comboBox.currentText()
        city_type = self.ui_create_app_window.city_comboBox.placeholderText()
        street = self.ui_create_app_window.street_comboBox.currentText()
        house_number = self.ui_create_app_window.line_number_house.text()
        room = self.ui_create_app_window.line_number_room.text()

        address = f'{region}, {CITY_TYPE[city_type]}{city}, ул.{street}, д.{house_number}, кв.{room}'

        if '' in [description, fio, region, city, street, house_number, room]:
            self.open_padding_error_window()
            return

        self.conn.add_new_application_query(description, fio, address, region, city, street, house_number, room,
                                            city_type, str(self.user_id))

        self.view_user_data()

        self.create_app_window.close()

    def user_edit_application(self):
        index = self.ui_user_window.tableView_applications.selectedIndexes()[0]
        id = str(self.ui_user_window.tableView_applications.model().data(index))

        description = self.ui_edit_app_window.text_app.toPlainText()
        fio = self.ui_edit_app_window.line_fio.text()
        region = self.ui_edit_app_window.region_comboBox.currentText()
        city = self.ui_edit_app_window.city_comboBox.currentText()
        type_city = self.ui_edit_app_window.city_comboBox.placeholderText()
        street = self.ui_edit_app_window.street_comboBox.currentText()
        house_number = self.ui_edit_app_window.line_number_house.text()
        room = self.ui_edit_app_window.line_number_room.text()

        address = f'{region}, {CITY_TYPE[type_city]}{city}, ул.{street}, д.{house_number}, кв.{room}'

        self.conn.update_application_query(description, fio, address, region, city, street, house_number, room,
                                           type_city, id)

        self.view_user_data()

        self.edit_app_window.close()

    def user_create_and_open_report(self):
        try:
            index = self.ui_user_window.tableView_applications.selectedIndexes()[0]
        except:
            self.open_select_error()
            return
        number_app = self.ui_user_window.tableView_applications.model().data(index)

        cursor = self.conn.cursor
        sql_query = f"SELECT fio, date_of_creation, responsible_mngr, responsible, creator, address, description, status FROM applications WHERE application_id = '{number_app}'"
        cursor.execute(sql_query)
        fio, date_of_creation, dispatcher_id, executor, customer_id, address, description, status = cursor.fetchall()[0]

        if executor is None:
            executor = 'не назначен'

        if dispatcher_id is not None:
            sql_query = f"SELECT full_name FROM users WHERE user_id = '{dispatcher_id}'"
            cursor.execute(sql_query)
            dispatcher = cursor.fetchall()[0][0]
        else:
            dispatcher = 'не назначен'

        if customer_id is not None:
            sql_query = f"SELECT full_name FROM users WHERE user_id = '{customer_id}'"
            cursor.execute(sql_query)
            customer = cursor.fetchall()[0][0]
        else:
            customer = 'не назначен'

        sql_query = f"SELECT full_name FROM users WHERE role = 'director'"
        cursor.execute(sql_query)
        director_name = cursor.fetchall()[0][0]

        self.doc.create_user_app_report(number_app, fio, str(date_of_creation), dispatcher, executor, customer, address,
                                        description, director_name, status)

        # self.doc.open_file(rf"T:\Python\applicationProject\resources\documents\report{number_app}.docx")
        self.doc.open_file(rf"resources\documents\report{number_app}.docx")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ApplicationProject()
    sys.exit(app.exec())
