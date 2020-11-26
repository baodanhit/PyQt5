import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import uic
import os

class ApplWindow(QDialog):
    def __init__(self):
        super(ApplWindow, self).__init__()
        uiPath = os.path.join(os.path.dirname(__file__)+'\checkBox.ui')
        self.ui = uic.loadUi(uiPath, self)
        self.ui.checkBox_1.stateChanged.connect(self.calc)
        self.ui.checkBox_2.stateChanged.connect(self.calc)
        self.ui.checkBox_3.stateChanged.connect(self.calc)
        self.show()
    def calc(self):
        amount = 10
        if self.ui.checkBox_1.isChecked():
            amount+=1
        if self.ui.checkBox_2.isChecked():
            amount+=2
        if self.ui.checkBox_3.isChecked():
            amount+=3
        self.ui.labelTotal.setText("Total: {0}$".format(str(amount)))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ApplWindow()
    sys.exit(app.exec_())
