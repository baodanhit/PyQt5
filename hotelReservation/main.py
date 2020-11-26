import sys
from PyQt5.QtWidgets import QDialog, QApplication, QInputDialog, QListWidgetItem
from PyQt5 import uic


class AppWindow(QDialog):
    def __init__(self):
        super(AppWindow, self).__init__()
        self.ui = uic.loadUi('ui_main.ui', self)
        self.roomCost = {"Suite": 40, "Super Luxury": 30, "Super Deluxe": 20, "Ordinary": 10}
        self.ui.btnCalc.clicked.connect(self.calc)
        self.show()
    def calc(self):
        date = self.ui.calendarWidget.selectedDate().toString('dd-MM-yyyy')
        days = self.ui.spinBoxDays.value()
        roomType = self.comboBoxRoomType.currentText()
        cost = self.roomCost[roomType]
        totalCost = days*cost

        self.ui.labelInfo.setText("Date of reservation: {0}\n"
                                  "Number of days: {1}\n"
                                  "Room type selected: {2}".format(date, days, roomType))
        self.ui.labelCost.setText("Room rent for single day for {} type is {} $\n"
                                  "Total room rent is {} $".format(roomType, cost, totalCost))
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AppWindow()
    sys.exit(app.exec_())
