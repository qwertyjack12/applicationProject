import psycopg2
from psycopg2.extensions import STATUS_READY
from PySide6 import QtWidgets, QtSql


class Data:
    def __init__(self):
        super(Data, self).__init__()
        self.create_connection()
        self.flag_connection = self.create_connection()

    def create_connection(self):
        con_info = {
            "host": "localhost",
            "port": "5432",
            "database": "applications_db",
            "user": "postgres",
            "password": "1111",
        }

        self.cursor = None
        self.con = None

        try:
            self.con = psycopg2.connect(**con_info)
            self.cursor = self.con.cursor()
            if self.con.status == STATUS_READY:
                print("Соединение с базой данных PostgreSQL установлено успешно.")
        except:
            # QtWidgets.QMessageBox.critical(None, "Can't open db", "Click Ok to exit!")
            return False

        return True

    def execute_query_with_params(self, sql_query, query_values=None):
        if query_values is not None:
            self.cursor.execute(sql_query, query_values)
            self.con.commit()

    def add_new_application_query(self, description, fio, address, region, city, street, house_number, room, city_type, user_id):
        sql_query = "INSERT INTO applications (description, fio, address, region, city, street, house_number, room, date_of_creation, city_type, creator) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        self.execute_query_with_params(sql_query, [description, fio, address, region, city, street, house_number, room, 'now', city_type, user_id])

    def update_application_query(self, description,  fio, address, region, city, street, house_number, room, city_type, id):
        query_dict = {'description': description, 'fio': fio, 'address': address, 'region': region, 'city': city,
                      'street': street, 'house_number': house_number, 'room': room, 'city_type': city_type}
        query_dict = {i: query_dict[i] for i in query_dict.keys() if len(str(query_dict[i])) != 0}

        if len(query_dict) != 0:
            string_query_dict = ', '.join([f'{i} = %s' for i in query_dict.keys()])
            sql_query = "UPDATE applications SET " + string_query_dict + " WHERE application_id = %s"
            params = list(query_dict.values())
            params.append(id)
            self.execute_query_with_params(sql_query, params)

    def update_dispatcher_application_query(self, dispatcher_status, description, address, region, city, street, house_number, room, status, responsible, dispatcher_id, city_type, id):
        query_dict = {'description': description, 'address': address, 'region': region, 'city': city, 'street': street,
                      'house_number': house_number, 'room': room, 'status': status, 'responsible': responsible,
                      'city_type': city_type, 'responsible_mngr': dispatcher_id}
        query_dict = {i: query_dict[i] for i in query_dict.keys() if len(str(query_dict[i])) != 0}

        if dispatcher_status == 'Новая':
            sql_query = "UPDATE applications SET description = %s, address = %s, city_type = %s, region = %s, city = %s, street = %s, house_number = %s, room = %s, status = %s, responsible = %s, date_of_adoption = %s, responsible_mngr = %s WHERE application_id = %s"
            self.execute_query_with_params(sql_query, [description, address, city_type, region, city, street, house_number, room, status, responsible, 'now', dispatcher_id, id])
        elif len(query_dict) != 0:
            string_query_dict = ', '.join([f'{i} = %s' for i in query_dict.keys()])
            sql_query = "UPDATE applications SET " + string_query_dict + " WHERE application_id = %s"
            params = list(query_dict.values())
            params.append(id)
            self.execute_query_with_params(sql_query, params)

    def update_admin_user_query(self, role, selected_user_role, password, user_id, selected_id, login=''):
        if user_id != selected_id and selected_user_role != 'director':
            query_dict = {'role': role, 'login': login, 'password': password}
        else:
            query_dict = {'login': login, 'password': password}
        query_dict = {i: query_dict[i] for i in query_dict.keys() if len(query_dict[i]) != 0}

        if len(role) * len(login) * len(password) != 0 and user_id != selected_id:
            sql_query = "UPDATE users SET role = %s, login = %s, password = %s WHERE user_id = %s"
            self.execute_query_with_params(sql_query, [role, login, password, selected_id])
        elif len(query_dict) != 0:
            string_query_dict = ', '.join([f'{i} = %s' for i in query_dict.keys()])
            sql_query = "UPDATE users SET " + string_query_dict + " WHERE user_id = %s"
            params = list(query_dict.values())
            params.append(selected_id)
            self.execute_query_with_params(sql_query, params)

    def update_admin_application_query(self, status, responsible, dispatcher_id, id, closing_date=''):
        query_dict = {'status': status, 'responsible': responsible, 'responsible_mngr': dispatcher_id,
                      'closing_date': closing_date}
        query_dict = {i: query_dict[i] for i in query_dict.keys() if len(str(query_dict[i])) != 0}

        if len(query_dict) != 0:
            string_query_dict = ', '.join([f'{i} = %s' for i in query_dict.keys()])
            sql_query = "UPDATE applications SET " + string_query_dict + " WHERE application_id = %s"
            params = list(query_dict.values())
            params.append(id)
            self.execute_query_with_params(sql_query, params)

    def del_admin_closing_date(self, id):
        sql_query = f"UPDATE applications SET closing_date = NULL WHERE application_id = %s"
        self.execute_query_with_params(sql_query, [id])

    def user_filtration_query(self, filter_category, id):
        sql_query = f"SELECT application_id, description, status, responsible, date_of_creation, date_of_adoption, closing_date FROM applications WHERE status=%s and creator=%s"
        self.execute_query_with_params(sql_query, [filter_category, id])

    def check_user_login_password_query(self, login, password):
        self.cursor.execute(f"SELECT login, password FROM users WHERE login='{login}' and password='{password}'")
        result = self.cursor.fetchall()
        return len(result)

    def check_user_login_query(self, login):
        self.cursor.execute(f"SELECT login FROM users WHERE login='{login}'")
        result = self.cursor.fetchall()
        return len(result)

    def check_user_id(self, user_id):
        self.cursor.execute(f"SELECT user_id FROM users WHERE user_id='{user_id}'")
        result = self.cursor.fetchall()
        return len(result)

    def add_new_user_query(self, full_name, login, password):
        sql_query = "INSERT INTO users (full_name, login, password) VALUES (%s, %s, %s)"
        self.execute_query_with_params(sql_query, [full_name, login, password])

    def get_user_role_query(self, id):
        sql_query = f"SELECT role FROM users WHERE user_id = '{id}'"
        self.cursor.execute(sql_query)
        result = self.cursor.fetchall()[0][0]
        return result
