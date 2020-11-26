import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import uic
import os


class ApplWindow(QDialog):
    def __init__(self):
        super(ApplWindow, self).__init__()
        uiPath = os.path.join(os.path.dirname(__file__) + '\DemoLineEdit.ui')
        self.ui = uic.loadUi(uiPath, self)
        self.ui.pushButton.clicked.connect(self.Add)
        self.show()

    def Add(self):
        self.ui.resultText.setText(self.ui.lineEdit.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ApplWindow()
    sys.exit(app.exec_())
