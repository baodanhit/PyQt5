'''
	Xây dựng lớp Student có hai thuộc tính code, name
	Xây dựng lớp Marks kế thừa từ lớp Student, có thêm hai thuộc tính riêng là History Marks, Geography Marks
	Nhập thông tin Student Code, Student Name, History Marks, Geography Marks,
 sau đó nhấp vào nút Click sẽ hiển thị thông tin bên dưới Label
'''


import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import uic

class Student:
    def __init__(self, name='noname', code='none'):
        self.name = name
        self.code = code
    def getName(self):
        return self.name
    def getCode(self):
        return self.code
class Mark(Student):
    def __init__(self, name='noname', code='none', historyMarks=0, geographyMarks=0):
        super().__init__(name, code)
        self.historyMarks = historyMarks
        self.geographyMarks = geographyMarks
    def getHistoryMark(self):
        return self.historyMarks
    def getGeographyMark(self):
        return self.geographyMarks
class AppWindow(QDialog):
    def __init__(self):
        super(AppWindow, self).__init__()
        self.ui = uic.loadUi('ui_main.ui', self)
        self.show()
        self.ui.btnOK.clicked.connect(self.createMark)
    def createMark(self):
        name = self.ui.studentNameLineEdit.text()
        code = self.ui.studentCodeLineEdit.text()
        history = self.ui.historyMarkLineEdit.text()
        geography = self.ui.geographyMarkLineEdit.text()

        marks = Mark(name, code, history, geography)

        self.ui.studentInfoLabel.setText("Student name: {}\n"
                                         "Student code: {}\n"
                                         "Marks: \n"
                                         "  History: {}\n"
                                         "  Geography: {}".
                                         format(marks.getName(),
                                                marks.getCode(),
                                                str(marks.getHistoryMark()),
                                                str(marks.getGeographyMark())))
    def vadidateMarks(self, mark_obj):
        self.isValid = True
        if not mark_obj.name or not mark_obj.code or not mark_obj.historyMarks or not mark_obj.geographyMarks:
            self.isValid = False
        else:
            try:
                mark_obj.historyMarks = float(mark_obj.historyMarks)
                mark_obj.geographyMarks = float(mark_obj.geographyMarks)
            except ValueError:
                self.isValid = False
        return self.isValid

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AppWindow()
    sys.exit(app.exec_())
