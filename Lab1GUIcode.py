# Form implementation generated from reading ui file 'Lab1GUI.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 400)
        MainWindow.setMinimumSize(QtCore.QSize(400, 400))
        MainWindow.setMaximumSize(QtCore.QSize(400, 400))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.VoteExitBox = QtWidgets.QDialogButtonBox(parent=self.centralwidget)
        self.VoteExitBox.setGeometry(QtCore.QRect(6, 326, 16, 16))
        self.VoteExitBox.setCenterButtons(False)
        self.VoteExitBox.setObjectName("VoteExitBox")
        self.title_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(120, 10, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        self.title_label.setFont(font)
        self.title_label.setObjectName("title_label")
        self.ID_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.ID_label.setGeometry(QtCore.QRect(90, 60, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        self.ID_label.setFont(font)
        self.ID_label.setObjectName("ID_label")
        self.ID_input = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.ID_input.setGeometry(QtCore.QRect(130, 50, 141, 31))
        self.ID_input.setObjectName("ID_input")
        self.candidates_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.candidates_label.setGeometry(QtCore.QRect(150, 120, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        self.candidates_label.setFont(font)
        self.candidates_label.setObjectName("candidates_label")
        self.ironman_button = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.ironman_button.setGeometry(QtCore.QRect(150, 160, 100, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.ironman_button.setFont(font)
        self.ironman_button.setObjectName("ironman_button")
        self.captainamerica_button = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.captainamerica_button.setGeometry(QtCore.QRect(150, 190, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.captainamerica_button.setFont(font)
        self.captainamerica_button.setObjectName("captainamerica_button")
        self.submit_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.submit_button.setGeometry(QtCore.QRect(120, 260, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.submit_button.setFont(font)
        self.submit_button.setObjectName("submit_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title_label.setText(_translate("MainWindow", "Voting Application"))
        self.ID_label.setText(_translate("MainWindow", "ID"))
        self.candidates_label.setText(_translate("MainWindow", "Candidates"))
        self.ironman_button.setText(_translate("MainWindow", "Iron Man"))
        self.captainamerica_button.setText(_translate("MainWindow", "Captain America"))
        self.submit_button.setText(_translate("MainWindow", "SUBMIT VOTE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
