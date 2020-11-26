import sys
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from PyQt5 import uic
import os

class ApplWindow(QDialog):
    def __init__(self):
        super(ApplWindow, self).__init__()
        uiPath = os.path.join(os.path.dirname(__file__)+'\loverFinder.ui')
        self.ui = uic.loadUi(uiPath, self)
        self.ui.btnContinue.clicked.connect(self.toast)
        self.ui.btnCancel.clicked.connect(self.close)
        self.show()
    def toast(self):
        QMessageBox.about(self, "Thông báo", "Xin chào!\nKhông tìm thấy người iu nào cho bạn!\nHãy tiếp tục làm người cô đơn đi nhé :>")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ApplWindow()
    sys.exit(app.exec_())
