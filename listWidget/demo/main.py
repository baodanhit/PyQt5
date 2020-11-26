import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import uic


class AppWindow(QDialog):
    def __init__(self):
        super(AppWindow, self).__init__()
        self.ui = uic.loadUi('listWidget.ui', self)
        self.ui.listWidgetSrc.itemSelectionChanged.connect(self.dispSelected)

        self.show()
    def dispSelected(self):
        self.ui.listWidgetDes.clear()
        items = self.ui.listWidgetSrc.selectedItems()
        x = []
        for i in list(items):
            self.ui.listWidgetDes.addItem(i.text())
            x.append(str(i.text()))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AppWindow()
    sys.exit(app.exec_())
