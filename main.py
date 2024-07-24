from PyQt5.QtWidgets import *

from src.model.Model import Model
from src.view.View import View
from src.controller.Controller import Controller


def main():
    app = QApplication([])

    with open("src/view/assets/style.qss", 'r') as file:
        qss = file.read()
        app.setStyleSheet(qss)

    model = Model()
    view = View()
    controller = Controller(model, view)

    view.show()
    app.exec_()


if __name__ == '__main__':
    main()
