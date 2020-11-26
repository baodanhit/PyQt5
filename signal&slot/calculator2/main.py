import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5 import uic

class AppWindow(QDialog):
    def __init__(self):
        super(AppWindow, self).__init__()
        width = 280
        height = 450
        # setting  the fixed size of window
        self.setFixedSize(width, height)
        self.ui = uic.loadUi('calc2.ui', self)
        # init values
        self.tempNums = ''
        self.tempString = ''
        self.result = '0'
        self.histories = []
        self.newExp = False
        self.ui.screenMainLine.setText('0')
        # handle events
        self.ui.btnN0.clicked.connect(lambda: self.inputNumber('0'))
        self.ui.btnN0.setShortcut('0')
        self.ui.btnN1.clicked.connect(lambda: self.inputNumber('1'))
        self.ui.btnN1.setShortcut('1')
        self.ui.btnN2.clicked.connect(lambda: self.inputNumber('2'))
        self.ui.btnN2.setShortcut('2')
        self.ui.btnN3.clicked.connect(lambda: self.inputNumber('3'))
        self.ui.btnN3.setShortcut('3')
        self.ui.btnN4.clicked.connect(lambda: self.inputNumber('4'))
        self.ui.btnN4.setShortcut('4')
        self.ui.btnN5.clicked.connect(lambda: self.inputNumber('5'))
        self.ui.btnN5.setShortcut('5')
        self.ui.btnN6.clicked.connect(lambda: self.inputNumber('6'))
        self.ui.btnN6.setShortcut('6')
        self.ui.btnN7.clicked.connect(lambda: self.inputNumber('7'))
        self.ui.btnN7.setShortcut('7')
        self.ui.btnN8.clicked.connect(lambda: self.inputNumber('8'))
        self.ui.btnN8.setShortcut('8')
        self.ui.btnN9.clicked.connect(lambda: self.inputNumber('9'))
        self.ui.btnN9.setShortcut('9')
        self.ui.btnNDot.clicked.connect(lambda: self.inputNumber('.'))
        self.ui.btnNDot.setShortcut('.')
        self.ui.btnNLeftBracket.clicked.connect(lambda: self.inputNumber('('))
        self.ui.btnNLeftBracket.setShortcut('(')
        self.ui.btnNRightBracket.clicked.connect(lambda: self.inputNumber(')'))
        self.ui.btnNRightBracket.setShortcut(')')
        self.ui.btnOPlus.clicked.connect(lambda: self.inputOperator('+'))
        self.ui.btnOPlus.setShortcut('+')
        self.ui.btnOSubtraction.clicked.connect(lambda: self.inputOperator('-'))
        self.ui.btnOSubtraction.setShortcut('-')
        self.ui.btnOMultiplication.clicked.connect(lambda: self.inputOperator('*'))
        self.ui.btnOMultiplication.setShortcut('*')
        self.ui.btnODivision.clicked.connect(lambda: self.inputOperator('/'))
        self.ui.btnODivision.setShortcut('/')
        self.ui.btnOEqual.clicked.connect(lambda: self.calc())
        # self.ui.btnOEqual.setShortcut('Enter')
        self.ui.btnFAllClear.clicked.connect(lambda: self.clear())
        self.ui.btnFDelete.clicked.connect(lambda: self.deleteChar())
        self.ui.btnFDelete.setShortcut('Backspace')
        self.ui.btnFUp.clicked.connect(lambda: self.moveUp())
        # self.ui.btnFUp.setShortcut('Key_Up')
        self.ui.btnFDown.clicked.connect(lambda: self.moveDown())
        # self.ui.btnFDown.setShortcut('Key_Down')
        self.show()
    def modifyPre(self):
        if self.newExp:
            self.tempString = self.result
            self.newExp = False
    def inputNumber(self, num):
        self.modifyPre()
        self.tempNums += num
        self.tempString += num
        self.ui.screenMainLine.setText(self.tempString)
    def inputOperator(self, operator):
        self.modifyPre()
        self.tempString += operator
        self.tempNums = ''
        self.ui.screenMainLine.setText(self.tempString)
    def calc(self):
        self.expression = self.tempString
        if self.tempString == '':
            self.expression = '0'
            self.result = '0'
        else:
            try:
                self.result = str(eval(self.expression))
                self.ui.screenMainLine.setText(self.result)
                self.histories.append(self.expression)
                self.current = len(self.histories)
            except (SyntaxError, ZeroDivisionError):
                self.ui.screenMainLine.setText('error')
                self.result = self.expression
        self.ui.screenSubLine.setText(self.expression)
        self.newExp = True
        self.tempNums = ''
        self.tempString = ''
    def clear(self):
        self.tempNums = ''
        self.tempString = ''
        self.newExp = False
        self.ui.screenMainLine.setText('0')
        self.ui.screenSubLine.setText(self.result)
    def deleteChar(self):
        self.modifyPre()
        if len(self.tempString) > 1:
            self.tempString = self.tempString[0:-1:1]
        else:
            self.tempString = ''
        if self.tempString == '':
            self.ui.screenMainLine.setText('0')
        else:
            self.ui.screenMainLine.setText(self.tempString)
    def moveUp(self):
        if self.current > 0:
            self.current -= 1
            self.tempString = self.histories[self.current]
            self.ui.screenMainLine.setText(self.tempString)
            if self.current == 0:
                self.ui.screenSubLine.setText('')
            else:
                self.ui.screenSubLine.setText(self.histories[self.current-1])
    def moveDown(self):
        if self.current < len(self.histories):
            self.current += 1
            self.ui.screenSubLine.setText(self.histories[self.current - 1])
            if self.current <= len(self.histories)-1:
                self.tempString = self.histories[self.current]
                self.ui.screenMainLine.setText(self.tempString)
            else:
                self.tempString = ''
                self.ui.screenMainLine.setText('0')

# main
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AppWindow()
    sys.exit(app.exec_())