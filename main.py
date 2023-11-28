import sys
import io
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5 import uic

t = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>894</width>
    <height>742</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QTableWidget" name="tableWidget">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>20</y>
      <width>861</width>
      <height>451</height>
     </rect>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>894</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""

class Cofe(QMainWindow):
    def __init__(self):
        super().__init__()
        con = sqlite3.connect("coffee.sqlite")
        self.cur = con.cursor()
        self.initUI()
        con.close()

    def initUI(self):
        f = io.StringIO(t)
        uic.loadUi(f, self)
        result = self.cur.execute("""SELECT * FROM cofe""").fetchall()
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))
        for i in range(len(result)):
            for r in range(len(result[i])):
                self.tableWidget.setItem(i, r, QTableWidgetItem(str(result[i][r])))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Cofe()
    ex.show()
    sys.exit(app.exec())