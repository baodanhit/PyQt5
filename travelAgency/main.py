import sys
from PyQt5.QtWidgets import QDialog, QApplication, QInputDialog, QListWidgetItem
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
'''	Đơn giá hiển thị vé máy bay như sau: Hàn quốc 8000000,
 Thái lan 1400000, Nhật bản  1600000, Đài Loan  600000, 
 Singapore  2400000, Malaysia 2800000
Tiền phòng/ ngày: Hàn quốc 2000000, Thái lan 1000000,
  Nhật bản  2500000, Đài Loan  1200000, Singapore  1200000, Malaysia 1000000
Tổng tiền phải trả = (Tiền máy bay + tiền phòng * số ngày ở)* số người đi,

'''

class AppWindow(QDialog):
    def __init__(self):
        super(AppWindow, self).__init__()
        self.ui = uic.loadUi('ui_main.ui', self)

        self.airlineCost = {
            "Hàn Quốc": 8000000,
            "Thái Lan": 1400000,
            "Nhật Bản": 1600000,
            "Đài Loan": 600000,
            "Singapore": 2400000,
            "Malaysia": 2800000
        }
        self.roomCost = {
            "Hàn Quốc": 2000000,
            "Thái Lan": 1000000,
            "Nhật Bản": 2500000,
            "Đài Loan": 1200000,
            "Singapore": 1200000,
            "Malaysia": 1000000
        }
        self.imageUrl = {
            "Hàn Quốc": "korea.jpg",
            "Thái Lan": "thailand.jpg",
            "Nhật Bản": "japan.jpg",
            "Đài Loan": "taiwan.jpg",
            "Singapore": "singapore.jpg",
            "Malaysia": "malaysia.jpg"
        }
        self.ui.comboBoxDestination.currentIndexChanged.connect(self.changeDestination)
        self.ui.btnCalc.clicked.connect(self.calc)
        self.updateCost()
        self.show()
    def changeDestination(self):
        destination = self.ui.comboBoxDestination.currentText()
        url = self.imageUrl[destination]
        image = QPixmap(url)
        self.ui.labelImg.setPixmap(image)
        self.updateCost()
    def updateCost(self):
        des = self.ui.comboBoxDestination.currentText()
        self.lineEditCost.setText("{:,}".format(self.airlineCost[des]+self.roomCost[des]))
    def calc(self):
        customer_name = self.ui.lineEditCustomerName.text()
        destination = self.ui.comboBoxDestination.currentText()
        number = self.ui.spinBoxNumber.value()
        days = self.ui.spinBoxDays.value()
        date_start = self.ui.calendarWidget.selectedDate().toString("dd-MM-yyyy")
        airline_cost = self.airlineCost[destination]
        room_cost = self.roomCost[destination]
        total = (airline_cost + room_cost*days)*number
        self.ui.labelInfo.setText("Khách hàng: {}\n"
                                  "Nơi đi: {}\n"
                                  "Số người đi: {}\n"
                                  "Số ngày đi: {}\n"
                                  "Ngày bắt đầu: {}\n"
                                  "Tổng tiền: {:,} VNĐ".format(customer_name, destination, number, days, date_start, total))
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AppWindow()
    sys.exit(app.exec_())
