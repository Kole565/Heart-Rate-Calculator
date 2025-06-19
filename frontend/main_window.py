import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

from frontend.ui.ui_main_window import Ui_MainWindow
from backend.calculator import Calculator
from backend.exceptions import *


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.ageInput.textChanged.connect(self.on_changed)
        self.resthrInput.textChanged.connect(self.on_changed)

        self.calculator = Calculator()

    def on_changed(self, _):
        try:
            age = int(self.ageInput.text())
            rest_hr = float(self.resthrInput.text())
        except ValueError:
            return

        try:
            self.calculator.calculate(age, rest_hr)
        except InvalidInput:
            return

        self.zones = self.calculator.zones

        self._fill_zones_table()

    def _fill_zones_table(self):
        for row, (lower, upper) in enumerate(self.zones):
            self.zonesTable.setItem(row, 0, QTableWidgetItem(str(lower)))
            self.zonesTable.setItem(row, 1, QTableWidgetItem(str(upper)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
