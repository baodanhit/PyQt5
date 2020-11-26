import sys
from PyQt5.QtWidgets import QDialog, QApplication, QInputDialog, QListWidgetItem
from PyQt5 import uic


class AppWindow(QDialog):
    def __init__(self):
        super(AppWindow, self).__init__()
        self.ui = uic.loadUi('listWidget_Food.ui', self)
        self.ui.listWidgetDisplay.addItem('Pizza')
        self.ui.listWidgetDisplay.addItem('Pho')
        self.ui.listWidgetDisplay.addItem('Milk')
        self.ui.btnAdd.clicked.connect(self.dispList)
        self.ui.btnEdit.clicked.connect(self.editItem)
        self.ui.btnDeleteItem.clicked.connect(self.deleteItem)
        self.ui.btnDeleteAll.clicked.connect(self.deleteAll)
        self.show()
    def dispList(self):
        food = self.ui.inputFood
        if food.text():
            self.ui.listWidgetDisplay.addItem(food.text().capitalize())
        food.setText('')
        food.setFocus()
    def editItem(self):
        row = self.ui.listWidgetDisplay.currentRow()
        newText, ok = QInputDialog.getText(self, "Edit item", "Enter new text")
        if ok and (len(newText)!=0):
           self.ui.listWidgetDisplay.takeItem(row)
           self.ui.listWidgetDisplay.insertItem(row, QListWidgetItem(newText))
    def deleteItem(self):
        self.ui.listWidgetDisplay.takeItem(self.ui.listWidgetDisplay.currentRow())
    def deleteAll(self):
        self.ui.listWidgetDisplay.clear()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AppWindow()
    sys.exit(app.exec_())
