import sys
from PyQt5.QtWidgets import QDialog, QApplication, QInputDialog, QListWidgetItem
from PyQt5 import uic


class AppWindow(QDialog):
    def __init__(self):
        super(AppWindow, self).__init__()
        self.ui = uic.loadUi('ui_main.ui', self)
        self.ui.comboBoxType.currentIndexChanged.connect(self.disp)
        self.show()
    def disp(self):
        self.ui.labelSelected.setText(self.ui.comboBoxType.currentText())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AppWindow()
    sys.exit(app.exec_())
