from PySide6 import QtGui
from PySide6.QtCore import Qt, QAbstractTableModel, QModelIndex
from PySide6.QtGui import QFont, QBrush


class TableModel(QAbstractTableModel):
    def __init__(self, data, headers):
        super(TableModel, self).__init__()
        self._data = data
        self._headers = headers
        self._font_colors = dict()
        self._background_color = dict()

    def rowCount(self, parent=QModelIndex()):
        return len(self._data)

    def columnCount(self, parent=QModelIndex()):
        return len(self._data[0])

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            return str(self._data[index.row()][index.column()])
        elif role == Qt.ItemDataRole.ForegroundRole:
            if index in self._font_colors:
                return self._font_colors[index]
        elif role == Qt.ItemDataRole.BackgroundRole:
            if index in self._background_color:
                return self._background_color[index]
        return None

    def setData(self, index, value, role=Qt.ItemDataRole.EditRole):
        if role == Qt.ItemDataRole.ForegroundRole:
            self._font_colors[index] = value
            self.dataChanged.emit(index, index, [Qt.ItemDataRole.FontRole])
            return True
        elif role == Qt.ItemDataRole.BackgroundRole:
            self._background_color[index] = value
            self.dataChanged.emit(index, index, [Qt.ItemDataRole.BackgroundRole])
            return True
        else:
            if self._data[index.row()][index.column()] != value:
                self._data[index.row()][index.column()] = value
                self.dataChanged.emit(index, index, [Qt.ItemDataRole.DisplayRole, Qt.ItemDataRole.EditRole])
            return True

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole and orientation == Qt.Orientation.Horizontal:
            return self._headers[section]
        elif orientation == Qt.Orientation.Vertical:
            return str(section + 1)
        return None

    def column_by_name(self, column_name):
        for column in range(self.columnCount()):
            header_data = self.headerData(column, Qt.Orientation.Horizontal, Qt.ItemDataRole.DisplayRole)
            if header_data == column_name:
                return column
        return -1

    def flags(self, index):
        return super().flags(index)

    def sort(self, column, order=Qt.AscendingOrder):
        self.layoutAboutToBeChanged.emit()
        self._data = sorted(self._data, key=lambda x: x[column], reverse=order == Qt.DescendingOrder)
        self.layoutChanged.emit()


class TableModel_with_CheckBox(QAbstractTableModel):
    def __init__(self, data, headers):
        super(TableModel_with_CheckBox, self).__init__()
        self._data = data
        self._headers = headers
        self._background_color = dict()
        self._checked_items = [False] * len(data)  # список для хранения состояния чекбоксов

    def rowCount(self, parent=QModelIndex()):
        return len(self._data)

    def columnCount(self, parent=QModelIndex()):
        return len(self._data[0]) + 1  # добавляем 1 столбец для чекбоксов

    def column_by_name(self, column_name):
        for column in range(self.columnCount()):
            header_data = self.headerData(column, Qt.Orientation.Horizontal, Qt.ItemDataRole.DisplayRole)
            if header_data == column_name:
                return column
        return -1

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            if index.column() == 0:  # если столбец с чекбоксами
                return None
            return str(self._data[index.row()][index.column() - 1])
        if role == Qt.ItemDataRole.BackgroundRole:
            if index in self._background_color:
                return self._background_color[index]
        if role == Qt.ItemDataRole.CheckStateRole and index.column() == 0:  # если столбец с чекбоксами
            return Qt.Checked if self._checked_items[index.row()] else Qt.Unchecked
        return None

    def setData(self, index, value, role=Qt.ItemDataRole.EditRole):
        if role == Qt.ItemDataRole.CheckStateRole and index.column() == 0:  # если столбец с чекбоксами
            self._checked_items[index.row()] = value
            self.dataChanged.emit(index, index)
            return True
        if role == Qt.ItemDataRole.BackgroundRole:
            self._background_color[index] = value
            self.dataChanged.emit(index, index, [Qt.ItemDataRole.BackgroundRole])
            return True
        return super().setData(index, value, role)

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole and orientation == Qt.Orientation.Horizontal:
            if section == 0:  # если столбец с чекбоксами
                return ""
            return self._headers[section - 1]
        elif orientation == Qt.Orientation.Vertical:
            return str(section + 1)
        return None

    def flags(self, index):
        flags = super().flags(index)
        if index.column() == 0:  # если столбец с чекбоксами
            flags |= Qt.ItemIsUserCheckable
        return flags

    def sort(self, column, order=Qt.AscendingOrder):
        self.layoutAboutToBeChanged.emit()
        self._data = sorted(self._data, key=lambda x: x[column - 1], reverse=order == Qt.DescendingOrder)
        self.layoutChanged.emit()
