import sys
from PyQt5.QtWidgets import QDialog, QApplication, QInputDialog, QListWidgetItem
from PyQt5 import uic


class AppWindow(QDialog):
    def __init__(self):
        super(AppWindow, self).__init__()
        self.ui = uic.loadUi('ui_main.ui', self)
        self.items = []
        self.ui.btnAdd.clicked.connect(self.add)
        self.ui.btnRemove.clicked.connect(self.remove)
        self.show()
    def add(self):
        type = 'Bò'
        process = []
        if self.ui.radioButtonChicken.isChecked():
            type = 'Gà'
        elif self.ui.radioButtonFish.isChecked():
            type = 'Cá'
        if self.ui.checkBoxGrilled.isChecked():
            process.append('Nướng')
        if self.ui.checkBoxBoiled.isChecked():
            process.append('Luộc')
        if self.ui.checkBoxDried.isChecked():
            process.append('Chiên')
        for p in process:
            item = type + ' ' + p
            if item not in self.items:
                self.items.append(item)
                self.ui.listWidgetSelected.addItem(item)
                self.updateTotal()
    def remove(self):
        selectedItems = self.ui.listWidgetSelected.selectedItems()
        if selectedItems:
            for item in selectedItems:
                self.ui.listWidgetSelected.takeItem(self.ui.listWidgetSelected.row(item))
                self.items.remove(item.text())
                self.updateTotal()
        else:
            return
    def updateTotal(self):
        self.ui.labelTotal.setText('Tổng cộng: '+ str(len(self.items)))
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AppWindow()
    sys.exit(app.exec_())
