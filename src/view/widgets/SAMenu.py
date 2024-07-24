from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import *


class SAMenu(QWidget):
    """
    Single-Agent Menu widget for the application.

    Attributes:
        mainLayout (QVBoxLayout): Main layout of the Single-Agent Menu widget.
        mazeSelectButtonGroup (QButtonGroup): Button group for the Maze Select buttons.
        smallMazeRadioButton (QRadioButton): The small maze radio button.
        mediumMazeRadioButton (QRadioButton): The medium maze radio button.
        largeMazeRadioButton (QRadioButton): The large maze radio button.
        searchSelectButtonGroup (QButtonGroup): Button group for the Search Select buttons.
        DFSRadioButton (QRadioButton): The Depth-First Search radio button.
        BFSRadioButton (QRadioButton): The Breadth-First Search radio button.
        AStarRadioButton (QRadioButton): The A* Search radio button.
        agentStart (QLineEdit): Start position of the agent.
        agentGoal (QLineEdit): Goal position of the agent.
        randomiseButton (QPushButton): Button for randomising the maze.
        playButton (QPushButton): Button for playing the maze animation.

    Methods:
        __init__(self, parent=None): Initialize the Single-Agent Menu widget.
    """

    def __init__(self):
        """
        Initialize the Single-Agent Menu widget.
        """

        super().__init__()

        self.setFixedWidth(375)
        self.setFixedHeight(600)

        self.mainLayout = QVBoxLayout()
        self.setLayout(self.mainLayout)


        menuMazeTitle = QLabel("SELECT MAZE SIZE")
        menuMazeTitle.setObjectName("menuTitle")
        self.mainLayout.addWidget(menuMazeTitle)

        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        self.mainLayout.addWidget(line)

        mazeSelectorLayout = QHBoxLayout()
        self.mainLayout.addLayout(mazeSelectorLayout)

        self.mazeSelectButtonGroup = QButtonGroup()

        self.smallMazeRadioButton = QRadioButton("8x8")
        self.mazeSelectButtonGroup.addButton(self.smallMazeRadioButton, 0)
        mazeSelectorLayout.addWidget(self.smallMazeRadioButton)

        self.mediumMazeRadioButton = QRadioButton("16x16")
        self.mazeSelectButtonGroup.addButton(self.mediumMazeRadioButton, 1)
        mazeSelectorLayout.addWidget(self.mediumMazeRadioButton)

        self.largeMazeRadioButton = QRadioButton("32x32")
        self.mazeSelectButtonGroup.addButton(self.largeMazeRadioButton, 2)
        mazeSelectorLayout.addWidget(self.largeMazeRadioButton)


        menuSearchTitle = QLabel("SELECT SEARCH TYPE")
        menuSearchTitle.setObjectName("menuTitle")
        self.mainLayout.addWidget(menuSearchTitle)

        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        self.mainLayout.addWidget(line)

        searchSelectorLayout = QHBoxLayout()
        self.mainLayout.addLayout(searchSelectorLayout)

        self.searchSelectButtonGroup = QButtonGroup()

        self.DFSRadioButton = QRadioButton("DFS")
        self.searchSelectButtonGroup.addButton(self.DFSRadioButton, 0)
        searchSelectorLayout.addWidget(self.DFSRadioButton)

        self.BFSRadioButton = QRadioButton("BFS")
        self.searchSelectButtonGroup.addButton(self.BFSRadioButton, 1)
        searchSelectorLayout.addWidget(self.BFSRadioButton)

        self.AStarRadioButton = QRadioButton("A*")
        self.searchSelectButtonGroup.addButton(self.AStarRadioButton, 2)
        searchSelectorLayout.addWidget(self.AStarRadioButton)


        agentWaypointTitle = QLabel("AGENT WAYPOINTS")
        agentWaypointTitle.setObjectName("menuTitle")
        self.mainLayout.addWidget(agentWaypointTitle)

        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        self.mainLayout.addWidget(line)

        agentWaypointLayout = QHBoxLayout()
        self.mainLayout.addLayout(agentWaypointLayout)

        self.agentStart = QLineEdit()
        self.agentStart.setPlaceholderText("Start")
        agentWaypointLayout.addWidget(self.agentStart)

        self.agentGoal = QLineEdit()
        self.agentGoal.setPlaceholderText("Goal")
        agentWaypointLayout.addWidget(self.agentGoal)


        mazeControlTitle = QLabel("MAZE CONTROLS")
        mazeControlTitle.setObjectName("menuTitle")
        self.mainLayout.addWidget(mazeControlTitle)

        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        self.mainLayout.addWidget(line)

        mazeControlLayout = QHBoxLayout()
        self.mainLayout.addLayout(mazeControlLayout)

        self.randomiseButton = QPushButton("Randomise")
        self.randomiseButton.setObjectName("menuButton")
        mazeControlLayout.addWidget(self.randomiseButton)

        self.playButton = QPushButton("Play")
        self.playButton.setObjectName("menuButton")
        mazeControlLayout.addWidget(self.playButton)

        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.mainLayout.addItem(spacer)
