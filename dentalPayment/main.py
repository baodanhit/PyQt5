import sys
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from PyQt5 import uic


class AppWindow(QDialog):
    def __init__(self):
        super(AppWindow, self).__init__()
        self.ui = uic.loadUi('ui_main.ui', self)
        self.giaTayTrang = 200000
        self.giaNienRang = 300000
        self.giaNhoRang = 250000
        self.giaTrongRang = 150000
        self.ui.btnCheckout.clicked.connect(self.printInfo)
        self.ui.checkBoxNienRang.stateChanged.connect(self.calcTotal)
        self.ui.checkBoxTayTrang.stateChanged.connect(self.calcTotal)
        self.ui.spinBoxNhoRang.editingFinished.connect(self.calcTotal)
        self.ui.spinBoxTrongRang.editingFinished.connect(self.calcTotal)
        self.show()
    def calcTotal(self):
        serviceTayTrang = self.ui.checkBoxTayTrang.isChecked()
        serviceNienRang = self.ui.checkBoxNienRang.isChecked()
        serviceNhoRang = self.ui.spinBoxNhoRang.value()
        serviceTrongRang = self.ui.spinBoxTrongRang.value()

        total = 0
        if serviceTayTrang:
            total += self.giaTayTrang
        if serviceNienRang:
            total += self.giaNienRang
        total += self.giaNhoRang * serviceNhoRang
        total += self.giaTrongRang * serviceTrongRang
        self.ui.lineEditTotal.setText(str(total))
        return str(total)
    def printInfo(self):
        customerName = self.ui.lineEditName.text()
        customerSex = self.ui.comboBoxSex.currentText()
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Thông tin")
        msg.setText("Cảm ơn {} {} đã chọn dịch vụ!".format("anh" if customerSex == 'Nam' else "chị", customerName))
        msg.setInformativeText("Tổng chi phí: {} VNĐ".format(self.calcTotal()))
        msg.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AppWindow()
    sys.exit(app.exec_())
