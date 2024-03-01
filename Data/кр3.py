import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
import os


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("dob.ui", self)
        self.pushButton.clicked.connect(self.seve)
        self.con = sqlite3.connect("coffee.sqlite")

        self.modified = {}
        self.titles = None

    def seve(self):
        cur = self.con.cursor()
        cur.execute('INSERT INTO cofe (name, step, coct, opicanie, stomost, V) VALUES (?, ?, ?, ?, ?, ?)', (self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text(), self.lineEdit_6.text(), self.lineEdit_4.text(), self.lineEdit_5.text()))
        self.con.commit()
        ex.close()
        os.system('python main.py')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())