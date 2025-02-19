import sys
sys.path.append("..")
from communication.qt_log_communicate import Communicate

class Logger:
    def __init__(self):
        self.communicate = Communicate()
        self.clear_log_file()

    def log(self, message):
        self.communicate.log_signal.emit(message)
        self.dump(message=message)

    def dump(self, message):
        with open("log.txt", 'a') as f:
            f.write(message + '\n')

    def clear_log_file(self):
        with open("log.txt", 'w') as f:
            f.write('')
