import os
import sys

from RobotDashboardMainWindow import Ui_MainWindow
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox
)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()