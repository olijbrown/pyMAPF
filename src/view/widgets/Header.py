from PyQt5.QtWidgets import *


class Header(QWidget):
    """
    Header widget for the application.

    Attributes:
        headerTitle (QLabel): Label containing the header title.
        headerInfoButton (QPushButton): Button that shows the header information.

    Methods:
        __init__(self, parent=None): Initialize the header widget.
    """

    def __init__(self):
        """
        Initialize the header widget.
        """

        super().__init__()

        self.setFixedWidth(975)
        self.setFixedHeight(75)

        mainLayout = QHBoxLayout()
        self.setLayout(mainLayout)

        self.headerTitle = QLabel("Single-Agent Search")
        self.headerTitle.setObjectName("headerTitle")
        mainLayout.addWidget(self.headerTitle)

        spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        mainLayout.addItem(spacer)

        self.headerInfoButton = QPushButton("Help")
        self.headerInfoButton.setObjectName("headerInfoButton")
        mainLayout.addWidget(self.headerInfoButton)
