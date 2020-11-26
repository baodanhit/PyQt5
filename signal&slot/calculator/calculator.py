import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import uic

class AppWindow(QDialog):
    def __init__(self):
        super(AppWindow, self).__init__()
        self.ui = uic.loadUi('calculator.ui', self)
        self.ui.pushButtonAdd.clicked.connect(self.add)
        self.ui.pushButtonSub.clicked.connect(self.sub)
        self.ui.pushButtonMul.clicked.connect(self.mul)
        self.ui.pushButtonSup.clicked.connect(self.sup)
        self.show()
    def getA(self):
        a = (self.ui.lineEditFirst.text())
        if len(a) == 0:
            a = 0
        else :
            a = int(a)
        return a
    def getB(self):
        b = (self.ui.lineEditSecond.text())
        if len(b) == 0:
            b = 0
        else :
            b = int(b)
        return b
    def add(self):
        self.ui.labelResult.setText(str(self.getA()+self.getB()))
    def sub(self):
        self.ui.labelResult.setText(str(self.getA()-self.getB()))
    def mul(self):
        self.ui.labelResult.setText(str(self.getA()*self.getB()))
    def sup(self):
        self.ui.labelResult.setText(str(self.getA()/self.getB()))
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AppWindow()
    sys.exit(app.exec_())