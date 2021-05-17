from PyQt5.QtWidgets import *
import pyqtgraph as pg
import os
import Funkcje1


class App(QMainWindow):  # główne okno
    def __init__(self):
        super().__init__()
        # Definiuje geometrię okna
        self.glowny_dock = Layout()
        self.setCentralWidget(self.glowny_dock)

        self.left = 100
        self.top = 100
        self.width = 800
        self.height = 300
        self.setGeometry(self.left, self.top, self.width, self.height)
        # Definiuje tytuł okna
        self.setWindowTitle('Bryły')

        self.save = QAction('Save', self)  # Przypisuje nazwę do pozycji menu
        self.save.triggered.connect(self.Save)  # Przypisuje wywołanie metody do danej pozycji menu

        self.exitProgram = QAction('Exit', self)
        self.exitProgram.triggered.connect(self.exit_program)


        self.menuBar = self.menuBar()

        fileMenu = self.menuBar.addMenu('File')  # Dodaje menu File
        fileMenu.addAction(self.save)  # Dodaje pozcycję save w menu File
        fileMenu.addAction(self.exitProgram)  # Dodaje pozycję exit save w menu File

        self.show()

    def Save(self):
            print("Tu zapisujesz plik")


    @staticmethod
    def exit_program():
            print('Kończy działanie aplikacji')
            os._exit(0)

class Layout(QWidget):

    def __init__(self):
        super().__init__()
        self.graphWidget = pg.PlotWidget()

        self.layout1 = QGridLayout(self)

        self.tekst_1 = "Gęstość (d) "
        self.tekst_2 = "wartość "
        self.tekst_3 = "wartość "
        self.tekst_4 = "wartość "
        self.tekst_5 = "wartość "

        #Radio do napisów
        self.radio0 = []
        self.radio0.append(QRadioButton('KULA'))
        self.radio0.append(QRadioButton('CZWOROŚCIAN FOREMNY'))
        self.radio0.append(QRadioButton('ELIPSOIDA'))
        self.radio0.append(QRadioButton('OSTROSŁUP'))
        self.radio0.append(QRadioButton('STOŻEK'))
        self.radio0.append(QRadioButton('WALEC'))


        self.layout1.addWidget(self.radio0[0], 0, 0)
        self.layout1.addWidget(self.radio0[1], 0, 1)
        self.layout1.addWidget(self.radio0[2], 0, 2)
        self.layout1.addWidget(self.radio0[3], 1, 0)
        self.layout1.addWidget(self.radio0[4], 1, 1)
        self.layout1.addWidget(self.radio0[5], 1, 2)
        # Napisy

        self.etykieta1 = QLineEdit(self.tekst_1, self)
        self.etykieta2 = QLineEdit(self.tekst_2, self)
        self.etykieta3 = QLineEdit(self.tekst_3, self)
        self.etykieta4 = QLineEdit(self.tekst_4, self)
        self.etykieta5 = QLineEdit(self.tekst_5, self)

        self.layout1.addWidget(self.etykieta1, 2, 0)
        self.layout1.addWidget(self.etykieta2, 3, 0)
        self.layout1.addWidget(self.etykieta3, 4, 0)
        self.layout1.addWidget(self.etykieta4, 5, 0)
        self.layout1.addWidget(self.etykieta5, 6, 0)

        # Pola do wpisywania
        self.DoubleSpinBox_1 = QDoubleSpinBox(self)
        self.DoubleSpinBox_2 = QDoubleSpinBox(self)
        self.DoubleSpinBox_3 = QDoubleSpinBox(self)
        self.DoubleSpinBox_4 = QDoubleSpinBox(self)
        self.DoubleSpinBox_5 = QDoubleSpinBox(self)

        self.layout1.addWidget(self.DoubleSpinBox_1, 2, 2)
        self.layout1.addWidget(self.DoubleSpinBox_2, 3, 2)
        self.layout1.addWidget(self.DoubleSpinBox_3, 4, 2)
        self.layout1.addWidget(self.DoubleSpinBox_4, 5, 2)
        self.layout1.addWidget(self.DoubleSpinBox_5, 6, 2)

        #Rariobutton
        self.radio1 = []
        self.radio1.append(QRadioButton('KULA'))
        self.radio1.append(QRadioButton('CZWOROŚCIAN FOREMNY'))
        self.radio1.append(QRadioButton('ELIPSOIDA'))
        self.radio1.append(QRadioButton('OSTROSŁUP'))
        self.radio1.append(QRadioButton('STOŻEK'))
        self.radio1.append(QRadioButton('WALEC'))

        self.textbox1 = QLineEdit(self)
        self.textbox2= QLineEdit(self)
        self.textbox3 = QLineEdit(self)

        #QLabel
        self.label = QLabel()
        self.layout2 = QGridLayout(self)
        self.layout2.addWidget(self.radio1[0])
        self.layout2.addWidget(self.radio1[1])
        self.layout2.addWidget(self.radio1[2])
        self.layout2.addWidget(self.radio1[3])
        self.layout2.addWidget(self.radio1[4])
        self.layout2.addWidget(self.radio1[5])

        self.layout2.addWidget(self.textbox1)
        self.layout2.addWidget(self.textbox2)
        self.layout2.addWidget(self.textbox3)

        self.layout2.addWidget(self.label)

        self.group1 = QGroupBox(self)
        self.group1.setLayout(self.layout1)
        self.group2 = QGroupBox(self)
        self.group2.setLayout(self.layout2)

        self.layout = QHBoxLayout(self)
        self.layout.addWidget(self.group1, 0)
        self.layout.addWidget(self.group2, 1)
        self.setLayout(self.layout)

        self.setLayout(self.layout1)

        #Wywoływanie
        self.radio0[0].toggled.connect(self.radio0_toggle)
        self.radio0[1].toggled.connect(self.radio0_toggle)
        self.radio0[2].toggled.connect(self.radio0_toggle)
        self.radio0[3].toggled.connect(self.radio0_toggle)
        self.radio0[4].toggled.connect(self.radio0_toggle)
        self.radio0[5].toggled.connect(self.radio0_toggle)

        self.radio1[0].toggled.connect(self.KULA)
        self.radio1[1].toggled.connect(self.CZWOROSCIAN)
        self.radio1[2].toggled.connect(self.ELIPSOIDA)
        self.radio1[3].toggled.connect(self.OSTROSLUP)
        self.radio1[4].toggled.connect(self.STOZEK)
        self.radio1[5].toggled.connect(self.WALEC)

        self.show()

    def radio0_toggle(self):
        for i in range(len(self.radio1)):

                if self.radio0[0].isChecked():
                    self.etykieta2.setText("Promień (r)")
                    self.etykieta3.setText("")
                    self.etykieta4.setText("")
                    self.etykieta5.setText("")
                    break

                if self.radio0[1].isChecked():
                    self.etykieta2.setText("Bok (a)")
                    self.etykieta3.setText("")
                    self.etykieta4.setText("")
                    self.etykieta5.setText("")
                    break

                if self.radio0[2].isChecked():
                    self.etykieta2.setText("Pół oś (a)")
                    self.etykieta3.setText("Pół oś (b)")
                    self.etykieta4.setText("Pół oś (c)")
                    self.etykieta5.resize(130,20)
                    self.etykieta5.setText("Kąt (x), x należy [-1;1]")
                    break

                if self.radio0[3].isChecked():
                    self.etykieta2.setText("Bok (a)")
                    self.etykieta3.setText("Bok (b)")
                    self.etykieta4.resize(120, 20)
                    self.etykieta4.setText("Wysokość całkowita (H)")
                    self.etykieta5.resize(110, 20)
                    self.etykieta5.setText("Wysokość boczna (h)")
                    break

                if self.radio0[4].isChecked():
                    self.etykieta2.setText("Promień (r)")
                    self.etykieta3.setText("Krawędź (l)")
                    self.etykieta4.resize(120, 20)
                    self.etykieta4.setText("Wysokość całkowita (H)")
                    self.etykieta5.setText("")
                    break

                if self.radio0[5].isChecked():
                    self.etykieta2.setText("Promień (r)")
                    self.etykieta3.resize(120, 20)
                    self.etykieta3.setText("Wysokość całkowita (H)")
                    self.etykieta4.setText("")
                    self.etykieta5.setText("")
                    break

    def KULA(self):
        try:
            if self.radio1[0].isChecked() == True:
                r = self.DoubleSpinBox_2.value()
                d = self.DoubleSpinBox_1.value()
                self.textbox1.setText("Objętość wynosi: " + str(Funkcje1.objetosc_kula(r)))
                self.textbox2.setText("Masa wynosi: " + str(Funkcje1.masa_kula(r, d)))
                self.textbox3.setText("Pole wynosi: " + str(Funkcje1.pole_kula(r)))
        except:
            print(self.radio1[0].isChecked())

    def CZWOROSCIAN(self):
        try:
            if self.radio1[1].isChecked() == True:
                d = self.DoubleSpinBox_1.value()
                a = self.DoubleSpinBox_2.value()
                self.textbox1.setText("Objętość wynosi: " + str(Funkcje1.objetosc_kostka(a)))
                self.textbox2.setText("Masa wynosi: " + str(Funkcje1.masa_kostka(a, d)))
                self.textbox3.setText("Pole wynosi: " + str(Funkcje1.pole_kostka(a)))
        except:
            print(self.radio1[1].isChecked())

    def ELIPSOIDA(self):
        try:
            if self.radio1[2].isChecked() == True:
                d = self.DoubleSpinBox_1.value()
                a = self.DoubleSpinBox_2.value()
                b = self.DoubleSpinBox_3.value()
                c = self.DoubleSpinBox_4.value()
                x = self.DoubleSpinBox_5.value()
                self.textbox1.setText("Objętość wynosi: " + str(Funkcje1.objetosc_elipsoida(a, b, c)))
                self.textbox2.setText("Masa wynosi: " + str(Funkcje1.masa_elipsoida(a, b, c, d)))
                self.textbox3.setText("Pole wynosi: " + str(Funkcje1.pole_elipsoida(a, b, x)))
        except:
            print(self.radio1[2].isChecked())

    def OSTROSLUP(self):
        try:
            if self.radio1[3].isChecked() == True:
                d = self.DoubleSpinBox_1.value()
                a = self.DoubleSpinBox_2.value()
                b = self.DoubleSpinBox_3.value()
                H = self.DoubleSpinBox_4.value()
                h = self.DoubleSpinBox_5.value()
                self.textbox1.setText("Objętość wynosi: " + str(Funkcje1.objetosc_ostroslupa(a, b, H)))
                self.textbox2.setText("Masa wynosi: " + str(Funkcje1.masa_ostroslupa(a, b, d, H)))
                self.textbox3.setText("Pole wynosi: " + str(Funkcje1.pole_ostroslupa(a, b, h)))
        except:
            print(self.radio1[3].isChecked())

    def STOZEK(self):
        try:
            if self.radio1[4].isChecked() == True:
                d = self.DoubleSpinBox_1.value()
                r = self.DoubleSpinBox_2.value()
                l = self.DoubleSpinBox_3.value()
                H = self.DoubleSpinBox_4.value()
                self.textbox1.setText("Objętość wynosi: " + str(Funkcje1.objetosc_stozek(r, H)))
                self.textbox2.setText("Masa wynosi: " + str(Funkcje1.masa_stozek(d, r, H)))
                self.textbox3.setText("Pole wynosi: " + str(Funkcje1.pole_stozek(r, l)))
        except:
            print(self.radio1[4].isChecked())

    def WALEC(self):
        try:
            if self.radio1[5].isChecked() == True:
                d = self.DoubleSpinBox_1.value()
                r = self.DoubleSpinBox_2.value()
                H = self.DoubleSpinBox_3.value()
                self.textbox1.setText("Objętość wynosi: " + str(Funkcje1.objetosc_walec(r, H)))
                self.textbox2.setText("Masa wynosi: " + str(Funkcje1.masa_walec(r, H, d)))
                self.textbox3.setText("Pole wynosi: " + str(Funkcje1.pole_walec(r, H)))
        except:
            print(self.radio1[5].isChecked())
