# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets
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


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


class Ui_MainWindow(object):
    SetOfQuizes = []

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(439, 340)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setWindowIcon(QIcon(QFileInfo(__file__).absolutePath()+'\\icon.png'))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.AddSetOfQuestions = QtWidgets.QPushButton(self.centralwidget)
        self.AddSetOfQuestions.setGeometry(QtCore.QRect(290, 260, 111, 31))
        self.AddSetOfQuestions.setCheckable(False)
        self.AddSetOfQuestions.setObjectName("AddSetOfQuestions")
        self.AddSetOfQuestions.clicked.connect(lambda: self.SubmitAnswers(MainWindow))

        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(90, 120, 82, 17))
        self.radioButton.setText("")
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 90, 121, 21))
        self.label.setObjectName("label")

        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(90, 150, 82, 17))
        self.radioButton_2.setText("")
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(90, 180, 82, 17))
        self.radioButton_3.setText("")
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_4.setGeometry(QtCore.QRect(90, 210, 82, 17))
        self.radioButton_4.setText("")
        self.radioButton_4.setObjectName("radioButton_4")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(160, 120, 251, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 150, 251, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(160, 210, 251, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(160, 180, 251, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 90, 121, 21))
        self.label_2.setObjectName("label_2")

        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(30, 260, 118, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")

        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(40, 40, 371, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 10, 81, 20))
        self.label_3.setObjectName("label_3")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 439, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def SubmitAnswers(self, MainWindow):
        answers = []
       
        def check(x):
            if x:
                return 1
            else:
                return 0

        answers.append((self.lineEdit.text(), check(self.radioButton.isChecked())))
        answers.append((self.lineEdit_2.text(), check(self.radioButton_2.isChecked())))
        answers.append((self.lineEdit_3.text(), check(self.radioButton_3.isChecked())))
        answers.append((self.lineEdit_4.text(), check(self.radioButton_4.isChecked())))
        self.SetOfQuizes.append((self.lineEdit_5.text(), answers))
       
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")
        self.lineEdit_5.setText("")
        self.radioButton.setChecked(True)

        self.progressBar.setProperty("value", self.progressBar.property("value") + 25)

        if(self.progressBar.property('value') == 100):
            # should reconsider this shit
            temp, temp1, temp2 = [], [], []
            for i in self.SetOfQuizes:
                temp.append(i[0])
                temp1.append(i[1])
            tem2 = temp.copy()
            # adds Foreygn key to tuple
            for i in temp1:
                appendix = tem2.pop(0) 
                for j in i:
                    j = list(j)
                    j.append(appendix)
                    j = tuple(j)
                    temp2.append(j)
            # Database related stuff
            conn = create_connection(QFileInfo(__file__).absolutePath()+"\\main.db")  # connecting to database
            c = conn.cursor()
   
            sql = ''' INSERT INTO quiz(id)
              VALUES (?) '''
            sql1 = '''INSERT INTO answers 
              VALUES (?,?,?) '''
            for i in temp:
                c.execute(sql, [i])
            for j in temp2:
                c.execute(sql1, j)
                
            conn.commit()
            conn.close()

            MainWindow.close()
                       
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Adding Quiz"))
        self.AddSetOfQuestions.setText(_translate("MainWindow", "Додати"))
        self.label.setText(_translate("MainWindow", "Правильна відповідь:"))
        self.label_2.setText(_translate("MainWindow", "Відповіді: "))
        self.label_3.setText(_translate("MainWindow", "Запитання:"))


if __name__ == "__main__":
    import sys
    #-----------------------------------------------
    # database = QFileInfo(__file__).absolutePath()+"\\main.db"
 
    # sql_create_quiz_table = """ CREATE TABLE IF NOT EXISTS quiz (
    #                                     id text PRIMARY KEY
    #                                 ); """
 
    # sql_create_answers_table = """CREATE TABLE IF NOT EXISTS answers (
    #                                 id test PRIMARY KEY,
    #                                 isTrue integer NOT NULL,
    #                                 quiz_id integer NOT NULL,                               
    #                                 FOREIGN KEY (quiz_id) REFERENCES quiz (id)
    #                             );"""
 
    # # create a database connection
    # conn = create_connection(database)
 
    # # create tables
    # if conn is not None:
    #     # create Quiz table
    #     create_table(conn, sql_create_quiz_table)s
 
    #     # create Answers table
    #     create_table(conn, sql_create_answers_table)
    # else:
    #     print("Error! cannot create the database connection.")
    #----------------------------------------------------------------

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    app.setStyleSheet('QMainWindow{background-color: white;border: 1px solid black;}')
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
