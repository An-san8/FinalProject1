from PyQt6.QtWidgets import *
from Lab1GUIcode import *

import csv


def save_info(id_user, candidate):
    with open('vote_stats.csv','a', newline='') as file:
        write = csv.writer(file)
        write.writerow([id_user, candidate])


def id_vote():
    with open("Lab1_ID.txt", 'r') as file:
        id_line = [line.strip() for line in file]
    return id_line


class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.submit_button.clicked.connect(self.submit_vote)

    def submit_vote(self):
        id_user = self.ID_input.toPlainText().strip()
        id_valid = id_vote()

        if id_user not in id_valid:
            QMessageBox.warning(self,"Invalid", "Please enter a valid ID")
            return

        candidate = ""
        if self.captainamerica_button.isChecked():
            candidate = 'Captain America'
        elif self.ironman_button.isChecked():
            candidate = 'Iron Man'

        if candidate:
            QMessageBox.information(self,"Success", "Vote Entered")
            save_info(id_user, candidate)
        else:
            QMessageBox.warning(self,'Error', "Please cast your vote")

