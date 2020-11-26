import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import uic
import os


class ApplWindow(QDialog):
    def __init__(self):
        super(ApplWindow, self).__init__()
        uiPath = os.path.join(os.path.dirname(__file__) + '\icendrinks.ui')
        self.ui = uic.loadUi(uiPath, self)
        self.ui.checkBox_1.stateChanged.connect(self.calc)
        self.ui.checkBox_2.stateChanged.connect(self.calc)
        self.ui.checkBox_3.stateChanged.connect(self.calc)
        self.ui.checkBox_4.stateChanged.connect(self.calc)
        self.ui.checkBox_5.stateChanged.connect(self.calc)
        self.ui.checkBox_6.stateChanged.connect(self.calc)
        self.ui.checkBox_7.stateChanged.connect(self.calc)
        self.show()

    def calc(self):
        amount = 0
        # icecream
        if self.ui.groupBoxIceCream.isChecked():
            if self.ui.checkBox_1.isChecked():
                amount += 1
            if self.ui.checkBox_2.isChecked():
                amount += 2
            if self.ui.checkBox_3.isChecked():
                amount += 3
            if self.ui.checkBox_4.isChecked():
                amount += 4

        # drinks
        if self.ui.groupBoxDrink.isChecked():
            if self.ui.checkBox_5.isChecked():
                amount += 1
            if self.ui.checkBox_6.isChecked():
                amount += 1
            if self.ui.checkBox_7.isChecked():
                amount += 1
        self.ui.labelTotal.setText("Total amount is: {0}$".format(str(amount)))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ApplWindow()
    sys.exit(app.exec_())
