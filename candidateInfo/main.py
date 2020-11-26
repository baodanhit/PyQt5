import sys
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from PyQt5 import uic


class Candidate:
    def __init__(self, name='unknown', sex='undefined', address='unknown', qualification='none', assets='none'):
        self.name = name
        self.sex = sex
        self.address = address
        self.qualification = qualification
        self.assets = assets


class AppWindow(QDialog):
    def __init__(self):
        super(AppWindow, self).__init__()
        self.ui = uic.loadUi('ui_main.ui', self)
        self.candidate = ''
        self.ui.btnOk.clicked.connect(self.printInfo)
        self.ui.btnExit.clicked.connect(self.close)

        self.show()
    def getInfo(self):
        name = self.ui.lineEditName.text()
        sex = 'Nam' if self.ui.radioButtonSex_male.isChecked() else 'Nữ'
        address = self.ui.textEditAddress.toPlainText()
        qualification = self.ui.comboBoxQualification.currentText()
        assets = []
        if self.ui.checkBoxHome.isChecked():
            assets.append('Home')
        if self.ui.checkBoxCar.isChecked():
            assets.append('Car')
        if self.ui.checkBoxBike.isChecked():
            assets.append('Bike')
        self.candidate = Candidate(name, sex, address, qualification, assets)

    def printInfo(self):
        self.getInfo()
        message = 'invalid info'
        if self.candidate:
            message = 'Tên: {}\t\n' \
                      '{}\t\n' \
                      '{}\t\n' \
                      '{}\t'.format(
                self.candidate.name,
                self.candidate.sex,
                self.candidate.address,
                "\n".join(self.candidate.assets)
            )
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Thông tin")
        msg.setText(self.candidate.qualification)
        msg.setInformativeText(message)
        msg.exec_()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AppWindow()
    sys.exit(app.exec_())
