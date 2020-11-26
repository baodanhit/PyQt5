from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from notificator import notificator

#from notificator.alingments import TopLeft,TopCenter,TopRight,BottomLeft,BottomCenter,BottomRight # just import what need instance
from notificator.alingments import BottomRight
def printStatus():
    print('OK')
noft = notificator()


app = QApplication()
noft.critical("Title","Message", Parent=app, Align='BottomRight', duracion=100, onclick=printStatus)
app.exec_()