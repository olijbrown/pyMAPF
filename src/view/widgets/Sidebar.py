from PyQt5.QtWidgets import *


class Sidebar(QWidget):
    """
    Sidebar widget for the application.

    Attributes:
        SAButton (QPushButton): Button for setting the Single-Agent Menu.
        MAButton (QPushButton): Button for setting the Multi-Agent Menu.

    Methods:
        __init__(self, parent=None): Initialize the Sidebar widget.
    """

    def __init__(self):
        """
        Initialize the Sidebar widget.
        """

        super().__init__()

        self.setFixedWidth(225)
        self.setFixedHeight(675)

        mainLayout = QVBoxLayout()
        mainLayout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(mainLayout)

        headerTitle = QLabel("MAPF")
        headerTitle.setObjectName("sidebarTitle")
        mainLayout.addWidget(headerTitle)

        headerSubtitle = QLabel("Multi-Agent Pathfinding")
        headerSubtitle.setObjectName("sidebarSubtitle")
        headerSubtitle.setWordWrap(True)
        mainLayout.addWidget(headerSubtitle)

        self.SAButton = QPushButton("Single-Agent")
        self.SAButton.setObjectName("sidebarButton")
        mainLayout.addWidget(self.SAButton)

        self.MAButton = QPushButton("Multi-Agent")
        self.MAButton.setObjectName("sidebarButton")
        mainLayout.addWidget(self.MAButton)

        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        mainLayout.addItem(spacer)

        headerFooter = QLabel("Based on the \"Single-Agent and Multi-Agent Search in Maze Games\" project brief")
        headerFooter.setObjectName("sidebarFooter")
        headerFooter.setWordWrap(True)
        mainLayout.addWidget(headerFooter)
