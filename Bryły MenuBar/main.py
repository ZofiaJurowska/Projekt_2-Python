from PyQt5.QtWidgets import *
import sys
import main_window

app = QApplication(sys.argv)
ex = main_window.App()
app.exec_()