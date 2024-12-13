import sys
from PyQt6.QtWidgets import QApplication
from Lab1_Logic import Logic


def main():
    application = QApplication([])
    window = Logic()
    window.show()
    application.exec()


if __name__ == '__main__':
    main()
