import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import uic

class Customer:
    def __init__(self, id='undefined', name='unknown', amount='0', cost='0'):
        self.id = id
        self.name = name
        self.amount = amount
        self.cost = cost
        self.totalCost = self.amount*self.cost
    def getId(self):
        return self.id
    def getName(self):
        return self.name
    def getAmount(self):
        return self.amount
    def getCost(self):
        return self.cost
    def getTotalCost(self):
        return self.totalCost

class AppWindow(QDialog):
    def __init__(self):
        super(AppWindow, self).__init__()
        self.ui = uic.loadUi('ui_main.ui', self)
        self.show()
        self.btnExit.clicked.connect(self.close)
        self.btnCalc.clicked.connect(self.calc)

    def calc(self):
        name = self.ui.lineEditName.text()
        id = self.ui.lineEditId.text()
        amount = self.lineEditAmount.text()
        cost = self.lineEditCost.text()
        if name and id and amount and cost:
            if amount.isnumeric() and cost.isnumeric():
                try:
                    amount = int(amount)
                    cost = int(cost)
                    if amount >= 1 and cost >= 1000:
                        customer = Customer(id, name, amount, cost)
                        if self.ui.radioButtonInTime.isChecked():
                            customer.totalCost -= customer.getTotalCost()*0.05
                        else:
                            customer.totalCost += customer.getTotalCost()*0.05
                        self.ui.labelInfo.setText("Mã KH: {}\n"
                                                  "Tên KH: {}\n"
                                                  "Số lượng: {}\n"
                                                  "Đơn giá: {:,}\n"
                                                  "Thành tiền: {:,}\n".format(customer.getId(),
                                                                customer.getName(),
                                                                str(customer.getAmount()),
                                                                customer.getCost(),
                                                                customer.getTotalCost()))
                        self.ui.lineEditTotalAmount.setText(str(customer.amount))
                        self.ui.lineEditTotalCost.setText(str(customer.totalCost))
                    else:
                        self.ui.labelInfo.setText('Thông tin không hợp lệ!')
                except ValueError:
                    self.ui.labelInfo.setText('Thông tin không hợp lệ!')
            else:
                self.ui.labelInfo.setText('Vui lòng nhập số cho Số lượng và Đơn giá!')
        else:
            self.ui.labelInfo.setText('Vui lòng nhập đầy đủ thông tin!')
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AppWindow()
    sys.exit(app.exec_())
