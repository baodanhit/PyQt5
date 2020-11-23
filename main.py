import sys
from PyQt5.QtWidgets import QDialog, QApplication, QListWidgetItem
from PyQt5 import uic


class AppWindow(QDialog):
    def __init__(self):
        super(AppWindow, self).__init__()
        self.ui = uic.loadUi('interface.ui', self)
        self.slots = []
        self.selectingSlots = []
        # ~~~~~~~~ GET SLOT OBJECTS (CHECKBOXES) FROM UI ~~~~~~~ #
        for i in range(1, 17):
            self.slots.append(eval('self.ui.checkBox_'+str(i)))
        # ~~~~~~~~~ HANDLE EVENT ON SLOTS ~~~~~~~~~ #
        for slot in self.slots:
            slot.clicked.connect(self.updateSelecting)
        # ~~~~~~~~~~~~~~~~~ EVENTS ~~~~~~~~~~~~~~~~ #
        self.ui.btnAddSlot.clicked.connect(self.updateSelected)
        self.ui.btnClearSelecting.clicked.connect(self.clearSelecting)
        self.ui.btnClearSelected.clicked.connect(self.clearSelected)

        self.show()

    def updateSelecting(self):
        self.selectingSlots = []
        selectingList = self.ui.listWidgetSelecting
        selectingList.clear()
        for slot in self.slots:
            if slot.isChecked():
                selectingList.addItem(slot.text())
                self.selectingSlots.append(slot.text())

    def updateSelected(self):
        selectedList = self.ui.listWidgetSelected
        selectedList.clear()
        for slot in self.selectingSlots:
            selectedList.addItem(slot)

    def clearSelecting(self):
        self.ui.listWidgetSelecting.clear()
        self.selectingSlots = []
        for slot in self.slots:
            slot.setChecked(False)

    def clearSelected(self):
        self.ui.listWidgetSelected.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AppWindow()
    sys.exit(app.exec_())
