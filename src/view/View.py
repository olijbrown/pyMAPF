import os

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from src.view.widgets.Sidebar import Sidebar
from src.view.widgets.Header import Header
from src.view.widgets.Maze import Maze
from src.view.widgets.SAMenu import SAMenu
from src.view.widgets.MAMenu import MAMenu


class View(QMainWindow):
    """
    A class for representing the view in the MVC architecture.

    Attributes:
        sidebar (Sidebar): Sidebar widget instance.
        header (Header): Header widget instance.
        maze (Maze): Maze widget instance.
        menuLayout (QGridLayout): Container for the menu layout.
        singleAgentMenu (SAMenu): Single Agent Menu widget instance.
        multiAgentMenu (MAMenu): Multi Agent Menu widget instance.

    Methods:
        __init__(self): Initializes the main window class.
        drawSAMenu(self): Draws the Single-Agent menu.
        drawMAMenu(self): Draws the Multi-Agent menu.
    """

    def __init__(self):
        """
        Initializes the main window class.
        """

        super().__init__()

        cwd = os.getcwd()
        QFontDatabase.addApplicationFont(cwd + "/src/view/assets/Apple ][.ttf")

        self.setWindowTitle("MAPF")

        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)

        mainLayout = QHBoxLayout(centralWidget)

        self.sidebar = Sidebar()
        mainLayout.addWidget(self.sidebar)

        subLayout = QVBoxLayout()
        mainLayout.addLayout(subLayout)

        self.header = Header()
        subLayout.addWidget(self.header)

        mazeLayout = QHBoxLayout()
        subLayout.addLayout(mazeLayout)

        self.maze = Maze()
        mazeLayout.addWidget(self.maze)

        self.menuLayout = QGridLayout()
        mazeLayout.addLayout(self.menuLayout)

        self.singleAgentMenu = SAMenu()
        self.menuLayout.addWidget(self.singleAgentMenu, 0, 0)

        self.multiAgentMenu = MAMenu()
        self.menuLayout.addWidget(self.multiAgentMenu, 0, 0)

        self.drawSAMenu()

    def drawSAMenu(self):
        """
        Draws the Single-Agent menu to the application.
        """
        self.singleAgentMenu.show()
        self.multiAgentMenu.hide()

    def drawMAMenu(self):
        """
        Draws the Multi-Agent menu to the application.
        """

        self.multiAgentMenu.show()
        self.singleAgentMenu.hide()
