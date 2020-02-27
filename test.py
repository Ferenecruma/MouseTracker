# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QFileInfo
from PyQt5.QtGui import QIcon
import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return conn


class Ui_Form(object):
    answers = []

    def CreateAndFetchData(self):       
        conn = create_connection(QFileInfo(__file__).absolutePath()+"\\main.db")
        c = conn.cursor()
        questions = (list(c.execute('SELECT * FROM quiz')))
        for q in questions:
            self.answers.append(list(c.execute('SELECT * FROM answers WHERE quiz_id = ?', q)))    
        for a in self.answers:
            print(a)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(756, 531)
        Form.setWindowIcon(QIcon(QFileInfo(__file__).absolutePath()+'\\icon.png'))

        self.CreateAndFetchData()
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(280, 70, 241, 31))
        self.label.setObjectName("label")
        self.label.setText(self.answers[0][0][2])
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(220, 130, 321, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText(self.answers[0][0][0])
        self.pushButton.clicked.connect(lambda: self.Clicked(Form))
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 200, 321, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setText(self.answers[0][1][0])
        self.pushButton_2.clicked.connect(lambda: self.Clicked(Form))
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(220, 270, 321, 51))
        self.pushButton_3.setText(self.answers[0][2][0])
        self.pushButton_3.clicked.connect(lambda: self.Clicked(Form))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(220, 340, 321, 51))
        self.pushButton_4.setText(self.answers[0][3][0])
        self.pushButton_4.clicked.connect(lambda: self.Clicked(Form))
        self.pushButton_4.setObjectName("pushButton_4")
        # self.retranslateUi(Form)
        self.answers.pop(0)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setWindowTitle("Test")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Test"))
        self.label.setText(_translate("Form", "Запитання"))
        self.pushButton.setText(_translate("Form", "Відповідь 1"))
        self.pushButton_2.setText(_translate("Form", "Відповідь 2"))
        self.pushButton_3.setText(_translate("Form", "Відповідь 3"))
        self.pushButton_4.setText(_translate("Form", "Відповідь 4"))
    
    def Clicked(self, Form):
        if (len(self.answers) != 0):
            temp = self.answers.pop(0)
            self.label.setText(str(temp[0][2]))
            self.pushButton.setText(str(temp[0][0]))
            self.pushButton_2.setText(str(temp[1][0]))
            self.pushButton_3.setText(str(temp[2][0]))
            self.pushButton_4.setText(str(temp[3][0]))
        else:
            Form.close()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
