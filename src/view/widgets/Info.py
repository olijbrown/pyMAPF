from PyQt5.QtWidgets import *


class Info(QWidget):
    """
    Info widget for the application.

    Methods:
        __init__(self, parent=None): Initialize the Info widget.
    """

    def __init__(self):
        """
        Initialize the Info widget.
        """

        super().__init__()

        self.setFixedWidth(600)
        self.setFixedHeight(600)

        mainLayout = QGridLayout()
        self.setLayout(mainLayout)

        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        mainLayout.addItem(spacer)

        infoTitle = QLabel("How-To Instructions:")
        infoTitle.setObjectName("infoTitle")
        mainLayout.addWidget(infoTitle)

        with open("src/view/assets/infoText.txt", "r") as file:
            infoBody = QLabel(file.read())
            infoBody.setObjectName("infoBody")
            infoBody.setWordWrap(True)
            mainLayout.addWidget(infoBody)

        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        mainLayout.addItem(spacer)
