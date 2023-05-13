import sys
from PySide2.QtWidgets import QApplication, QMainWindow,QDialog
from PySide2 import QtCore, QtWidgets
from mainwindow import Ui_MainWindow
from edit_dialog import Ui_Dialog
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session
from PySide2.QtCharts import QtCharts
# from PySide2.QtCharts import QtCharts
# raphicsView

class ItemsModel(QtCore.QAbstractTableModel):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.items = []
        # self.regions = {}

    def setItems(self, items):
        self.beginResetModel()
        self.items = items
        self.endResetModel()
    
    def setEmergencyType(self, emergencyTypes):
        self.beginResetModel()
        self.emergencyTypes = emergencyTypes
        self.endResetModel()

    def setDeposit(self, deposits):
        self.beginResetModel()
        self.deposits = deposits
        self.endResetModel()

    def rowCount(self, *args, **kwargs) -> int:
        return len(self.items)
    
    def columnCount(self, *args, **kwargs) -> int:
        return 6
    
    def data(self, index: QtCore.QModelIndex, role: QtCore.Qt.ItemDataRole):
        if not index.isValid():
            return
        
        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            emergency_occurrence_info = self.items[index.row()]
            col = index.column()
            if col == 0:
                return self.deposits[emergency_occurrence_info.mestorozdenie_id].name
            elif col == 1:
                return f'{emergency_occurrence_info.since}'
            elif col == 2:
                return f'{emergency_occurrence_info.until}'
            elif col == 3:
                return f'{emergency_occurrence_info.injured_amount}'
            elif col == 4:
                return self.emergencyTypes[emergency_occurrence_info.emergency_type_id].name
            elif col == 5:
                return f'{emergency_occurrence_info.comment}'
        elif role == QtCore.Qt.ItemDataRole.UserRole:
            return self.items[index.row()]

    def headerData(self, section: int, orientation: QtCore.Qt.Orientation, role: QtCore.Qt.ItemDataRole):
        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            if orientation == QtCore.Qt.Orientation.Horizontal:
                return {
                    0: "Месторождение",
                    1: "Начало происшествия",
                    2: "Окончание происшествия",
                    3: "Сумма ущерба",
                    4: "Тип происшествия",
                    5: "Комментарий",
                }.get(section)

class EditDialog(QDialog):
    def __init__(self, deposits,emergencyTypes, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.btnAdd.clicked.connect(self.accept)
        self.ui.btnCancel.clicked.connect(self.reject)

        print(deposits)
        for d in deposits.values():
            self.ui.cmbDeposit.addItem(d.name, d)
        
        print(emergencyTypes)
        for t in emergencyTypes.values():
            self.ui.cmbType.addItem(t.name, t)

    def get_data(self):
        return {
            "deposit_id": self.ui.cmbDeposit.currentData().id,
            "type_id": self.ui.cmbType.currentData().id,
            "since": self.ui.timeSince.text(),
            "until": self.ui.timeUntil.text(),
            "injured": self.ui.txtInjured.text(),
            "comment": self.ui.txtComment.text(),        
        }

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Учет происшествий")

        self.engine = create_engine("sqlite+pysqlite:///database.db", echo=True)

        self.model = ItemsModel()
        self.ui.tblItems.setModel(self.model)

        # чтобы авторесайзить
        self.ui.tblItems.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.ResizeToContents)

        self.load_emergency_type()
        self.load_mestorozdenie()
        
        self.load_emergency_occurrence()

        self.ui.cmbDeposit.currentIndexChanged.connect(self.load_emergency_occurrence)
        self.ui.cmbType.currentIndexChanged.connect(self.load_emergency_occurrence)
        self.ui.btnAdd.clicked.connect(self.on_btnAdd_click)
    

    def draw_line_chart(self):
        # series = QtCharts.QLineSeries()
        # series.append(0,0)
        # series.append(2,4)
        # series.append(3,9)
        # series.append(4,16)
        # series.setName("Питон говно")
        self.data_by_deposits = {}

        chart = QtCharts.QChart()

        for row in self.rows:
            items = self.data_by_deposits.setdefault(row.mestorozdenie_id, [])
            items.append(row)

        print(self.data_by_deposits)

        for mestorozdenie_id, mestorozdenie_data in self.data_by_deposits.items():

            mestorozdenie_name = self.deposits[mestorozdenie_id].name
         
        # создаем последовательность точек для вывода 
            series = QtCharts.QLineSeries()
        # даем ей название
            series.setName(mestorozdenie_name)
        # включаем отображение точек
            series.setPointsVisible(True)
            # series.setMarkerSize(4)
        
        # заполняем последовательность точек
        for row in mestorozdenie_data:
            # row.year -- это координа X, row.population -- координата Y
            series.append(1, row.injured_amount)
        
        # добавляем последовательность точек на график
            chart.addSeries(series)
       
    # активируем отображение осей
        chart.createDefaultAxes()
        chart.axisX().setTitleText("Год")
        chart.axisX().setLabelFormat("%i")
        chart.axisX().setMax(chart.axisX().max() + 1)
        chart.axisX().setMin(chart.axisX().min() - 1)
    
        chart.axisY().setLabelFormat("%i")
        chart.axisY().setTitleText("Сумма затрат, р.")
        chart.axisY().setMax(chart.axisY().max() + 100000)
        chart.axisY().setMin(chart.axisY().min() - 100000)
    
    # подключаем график к форме
        self.ui.graphicsView.setChart(chart)
       
        # chart.addSeries(series)
        # chart.createDefaultAxes()

        # self.ui.graphicsView.setChart(chart)
   

    def on_btnAdd_click(self):
        dialog = EditDialog(self.deposits, self.emergencyTypes)
        r = dialog.exec()
        if r == 0:
            return

        data = dialog.get_data()
        with Session(self.engine) as s:
            query = """
            INSERT INTO emergency_occurrence(mestorozdenie_id, since, until, injured_amount, emergency_type_id, comment)
            VALUES (:did, :s, :u, :i, :tid, :c)
            """

            s.execute(text(query), {
                "did": data['deposit_id'],
                "tid": data['type_id'],
                "s": data['since'],
                "u": data['until'],
                "i": data['injured'],
                "c": data['comment'],
            })
            s.commit()

        self.load_emergency_type()
        self.load_mestorozdenie()
        self.load_emergency_occurrence()
        

    def load_emergency_occurrence(self):
        deposits_data = self.ui.cmbDeposit.currentData()
        emergencyTypes_data = self.ui.cmbType.currentData()

        if deposits_data:
            deposit_id = self.ui.cmbDeposit.currentData().id
        else:
            deposit_id = 0

       
        if emergencyTypes_data:
            emergencyType_id = self.ui.cmbType.currentData().id
        else:
            emergencyType_id = 0

        self.rows = []

        with Session(self.engine) as s:

            query = """
            SELECT *
            FROM emergency_occurrence
            WHERE (:mid = 0 OR mestorozdenie_id = :mid) AND (:tid = 0 OR emergency_type_id = :tid)
            """

            rows = s.execute(text(query), {"mid": deposit_id, "tid": emergencyType_id})
            for r in rows:
                print(r)
                self.rows.append(r)
        
     
        self.model.setItems(self.rows)
        self.draw_line_chart()

    def load_mestorozdenie(self):
        self.deposits = {}

        with Session(self.engine) as s:

            query = """
            SELECT *
            FROM mestorozdenie
            """

            rows = s.execute(text(query))
            for r in rows:
                self.deposits[r.id] = r

        self.ui.cmbDeposit.addItem("Все месторождения")
        for r in self.deposits.values():
                self.ui.cmbDeposit.addItem(r.name, r)
        self.model.setDeposit(self.deposits)

    def load_emergency_type(self):
        self.emergencyTypes = {}

        with Session(self.engine) as s:

            query = """
            SELECT *
            FROM emergency_type
            """

            rows = s.execute(text(query))
            for r in rows:
                self.emergencyTypes[r.id] = r

        self.ui.cmbType.addItem("Все виды происшествий")
        for r in self.emergencyTypes.values():
                self.ui.cmbType.addItem(r.name, r)
        self.model.setEmergencyType(self.emergencyTypes)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
