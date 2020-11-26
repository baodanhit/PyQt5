import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import uic


class AppWindow(QDialog):
    def __init__(self):
        super(AppWindow, self).__init__()
        self.ui = uic.loadUi('booknsugar.ui', self)
        self.ui.spinBoxBook.editingFinished.connect(self.compute)
        self.ui.spinBoxSugar.editingFinished.connect(self.compute)

        self.show()

    def compute(self):
        bookPrice = self.ui.BookPrice.text()
        bookTotal = 0
        sugarPrice = self.ui.SugarPrice.text()
        sugarTotal = 0
        total = 0
        if bookPrice:
            bookTotal = int(bookPrice) * self.ui.spinBoxBook.value()
        if sugarPrice:
            sugarTotal = float(sugarPrice) * self.ui.spinBoxSugar.value()
        self.ui.amountBook.setText(str(bookTotal))
        self.ui.amountSugar.setText(str(sugarTotal))
        self.ui.total.setText(str(bookTotal + sugarTotal))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AppWindow()
    sys.exit(app.exec_())
