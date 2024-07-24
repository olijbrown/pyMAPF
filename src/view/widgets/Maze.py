from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import *

from src.model.graph.Graph import Graph
from src.view.widgets.Info import Info


class Maze(QWidget):
    """
    Maze widget for the application.

    Attributes:
        mainLayout (QGridLayout): Main layout for the Maze widget.

    Methods:
        __init__(self, parent=None): Initialize the Maze widget.
        drawMaze(self, width, height): Draw a maze at a given size.
        changeCell (self, x, y, colour, text): Change a cell in the Maze widget.
        drawInfo (self): Draw the info widget to the maze.
        clear (self): Clear the Maze widget.
    """

    cellClicked = pyqtSignal(int, int)

    def __init__(self):
        """
        Initialize the Maze widget.
        """

        super().__init__()

        self.setFixedWidth(600)
        self.setFixedHeight(600)

        self.mainLayout = QGridLayout()
        self.setLayout(self.mainLayout)

        self.drawInfo()

    def drawMaze(self, width: int, height: int):
        """
        Draw a maze at a given size.

        :param width: Width of the maze.
        :param height: Height of the maze.
        """
        self.clear()

        for x in range(width):
            for y in range(height):
                button = QPushButton()
                button.setFixedSize(int(500/width), int(500/width))
                button.setObjectName("mazeCell")
                button.clicked.connect(lambda _, xPos=x, yPos=y, btn=Qt.LeftButton: self.cellClicked.emit(xPos, yPos))
                button.setStyleSheet("background-color: white;")
                self.mainLayout.addWidget(button, x, y)

    def changeCell(self, x: int, y: int, colour: str, text: str = ""):
        """
        Change a cell in the Maze widget.

        :param x: X coordinate of the cell to be changed.
        :param y: Y coordinate of the cell to be changed.
        :param colour: Colour to change the cell to.
        :param text: Text to change the cell to.
        """

        cell = self.mainLayout.itemAtPosition(x, y)
        if cell:
            button = cell.widget()
            button.setText(text)
            button.setStyleSheet(f"background-color: {colour};")

    def drawInfo(self):
        """
        Draw the info widget to the maze.
        """

        self.clear()

        info = Info()
        self.mainLayout.addWidget(info, 0, 0)

    def clear(self):
        """
        Clear the Maze widget.
        """

        while self.mainLayout.count():
            item = self.mainLayout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
