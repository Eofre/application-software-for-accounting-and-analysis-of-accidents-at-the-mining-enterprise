import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from mainwindow import Ui_MainWindow
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Учет происшествий")

        self.engine = create_engine("sqlite+pysqlite:///database.db", echo=True)

        self.load_emergency_type()
        self.load_mestorozdenie()
        
        self.load_emergency_occurrence()

        self.ui.cmbDeposit.currentIndexChanged.connect(self.load_emergency_occurrence)
        self.ui.cmbType.currentIndexChanged.connect(self.load_emergency_occurrence)
    
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
        with Session(self.engine) as s:

            query = """
            SELECT *
            FROM emergency_occurrence
            WHERE (:mid = 0 OR mestorozdenie_id = :mid) AND (:tid = 0 OR emergency_type_id = :tid)
            """

            rows = s.execute(text(query), {"mid": deposit_id, "tid": emergencyType_id})
            for r in rows:
                print(r)
    
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

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
