from PyQt6.QtCore import pyqtSignal, QObject

class Communicate(QObject):
    log_signal = pyqtSignal(str)