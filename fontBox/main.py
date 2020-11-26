import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtGui import QFont
from PyQt5 import uic


class AppWindow(QDialog):
    def __init__(self):
        super(AppWindow, self).__init__()
        self.ui = uic.loadUi('ui_main.ui', self)
        self.ui.fontComboBox.currentFontChanged.connect(self.changeFont)
        self.show()
    def changeFont(self):
        font = (self.ui.fontComboBox.currentFont())
        print(font)
        self.ui.textEdit.setFont(font)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AppWindow()
    sys.exit(app.exec_())
