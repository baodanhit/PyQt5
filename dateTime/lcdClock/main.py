import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtCore import QTimer, QTime
from PyQt5 import uic


class AppWindow(QDialog):
    def __init__(self):
        super(AppWindow, self).__init__()
        self.ui = uic.loadUi('lcdClock.ui', self)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.disp)
        self.timer.start(1000)
        self.disp
        self.show()
    def disp(self):
        time = QTime.currentTime()
        text = time.toString('hh:mm:ss')
        self.ui.lcdNumber.display(text)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AppWindow()
    sys.exit(app.exec_())
