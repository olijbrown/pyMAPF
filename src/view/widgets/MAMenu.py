from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import *


class MAMenu(QWidget):
    """
    Multi-Agent Menu widget for the application.

    Attributes:
        mainLayout (QVBoxLayout): Main layout of the Multi-Agent Menu widget.
        mazeSelectButtonGroup (QButtonGroup): Button group for the Maze Select buttons.
        smallMazeRadioButton (QRadioButton): The small maze radio button.
        mediumMazeRadioButton (QRadioButton): The medium maze radio button.
        largeMazeRadioButton (QRadioButton): The large maze radio button.
        agentNumberButtonGroup (QButtonGroup): Button group for the Agent Number buttons.
        fourAgentRadioButton (QRadioButton): The four agent radio button.
        sixAgentRadioButton (QRadioButton): The six agent radio button.
        eightAgentRadioButton (QRadioButton): The eight agent radio button.
        agent1Start (QLineEdit): Start position of the first agent.
        agent1Goal (QLineEdit): Goal position of the first agent.
        agent2Start (QLineEdit): Start position of the second agent.
        agent2Goal (QLineEdit): Goal position of the second agent.
        agent3Start (QLineEdit): Start position of the third agent.
        agent3Goal (QLineEdit): Goal position of the third agent.
        agent4Start (QLineEdit): Start position of the fourth agent.
        agent4Goal (QLineEdit): Goal position of the fourth agent.
        agent5Start (QLineEdit): Start position of the fifth agent.
        agent5Goal (QLineEdit): Goal position of the fifth agent.
        agent6Start (QLineEdit): Start position of the sixth agent.
        agent6Goal (QLineEdit): Goal position of the sixth agent.
        agent7Start (QLineEdit): Start position of the seventh agent.
        agent7Goal (QLineEdit): Goal position of the seventh agent.
        agent8Start (QLineEdit): Start position of the eighth agent.
        agent8Goal (QLineEdit): Goal position of the eighth agent.
        randomiseButton (QPushButton): Button for randomising the maze.
        playButton (QPushButton): Button for playing the maze animation.

    Methods:
        __init__(self, parent=None): Initialize the Multi-Agent Menu widget.
    """

    def __init__(self):
        """
        Initialize the Multi-Agent Menu widget.
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


        agentNumberTitle = QLabel("SELECT NUMBER OF AGENTS")
        agentNumberTitle.setObjectName("menuTitle")
        self.mainLayout.addWidget(agentNumberTitle)

        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        self.mainLayout.addWidget(line)

        agentNumberLayout = QHBoxLayout()
        self.mainLayout.addLayout(agentNumberLayout)

        self.agentNumberButtonGroup = QButtonGroup()

        self.fourAgentRadioButton = QRadioButton("4")
        self.agentNumberButtonGroup.addButton(self.fourAgentRadioButton, 4)
        agentNumberLayout.addWidget(self.fourAgentRadioButton)

        self.sixAgentRadioButton = QRadioButton("6")
        self.agentNumberButtonGroup.addButton(self.sixAgentRadioButton, 6)
        agentNumberLayout.addWidget(self.sixAgentRadioButton)

        self.eightAgentRadioButton = QRadioButton("8")
        self.agentNumberButtonGroup.addButton(self.eightAgentRadioButton, 8)
        agentNumberLayout.addWidget(self.eightAgentRadioButton)


        agentWaypointTitle = QLabel("SET AGENT WAYPOINTS")
        agentWaypointTitle.setObjectName("menuTitle")
        self.mainLayout.addWidget(agentWaypointTitle)

        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        self.mainLayout.addWidget(line)

        agentWaypointLayout = QHBoxLayout()
        self.mainLayout.addLayout(agentWaypointLayout)

        self.agent1Start = QLineEdit()
        self.agent1Start.setPlaceholderText("A1 Start")
        agentWaypointLayout.addWidget(self.agent1Start)

        self.agent1Goal = QLineEdit()
        self.agent1Goal.setPlaceholderText("A1 Goal")
        agentWaypointLayout.addWidget(self.agent1Goal)

        agentWaypointLayout = QHBoxLayout()
        self.mainLayout.addLayout(agentWaypointLayout)

        self.agent2Start = QLineEdit()
        self.agent2Start.setPlaceholderText("A2 Start")
        agentWaypointLayout.addWidget(self.agent2Start)

        self.agent2Goal = QLineEdit()
        self.agent2Goal.setPlaceholderText("A2 Goal")
        agentWaypointLayout.addWidget(self.agent2Goal)

        agentWaypointLayout = QHBoxLayout()
        self.mainLayout.addLayout(agentWaypointLayout)

        self.agent3Start = QLineEdit()
        self.agent3Start.setPlaceholderText("A3 Start")
        agentWaypointLayout.addWidget(self.agent3Start)

        self.agent3Goal = QLineEdit()
        self.agent3Goal.setPlaceholderText("A3 Goal")
        agentWaypointLayout.addWidget(self.agent3Goal)

        agentWaypointLayout = QHBoxLayout()
        self.mainLayout.addLayout(agentWaypointLayout)

        self.agent4Start = QLineEdit()
        self.agent4Start.setPlaceholderText("A4 Start")
        agentWaypointLayout.addWidget(self.agent4Start)

        self.agent4Goal = QLineEdit()
        self.agent4Goal.setPlaceholderText("A4 Goal")
        agentWaypointLayout.addWidget(self.agent4Goal)

        agentWaypointLayout = QHBoxLayout()
        self.mainLayout.addLayout(agentWaypointLayout)

        self.agent5Start = QLineEdit()
        self.agent5Start.setPlaceholderText("A5 Start")
        agentWaypointLayout.addWidget(self.agent5Start)

        self.agent5Goal = QLineEdit()
        self.agent5Goal.setPlaceholderText("A5 Goal")
        agentWaypointLayout.addWidget(self.agent5Goal)

        agentWaypointLayout = QHBoxLayout()
        self.mainLayout.addLayout(agentWaypointLayout)

        self.agent6Start = QLineEdit()
        self.agent6Start.setPlaceholderText("A6 Start")
        agentWaypointLayout.addWidget(self.agent6Start)

        self.agent6Goal = QLineEdit()
        self.agent6Goal.setPlaceholderText("A6 Goal")
        agentWaypointLayout.addWidget(self.agent6Goal)

        agentWaypointLayout = QHBoxLayout()
        self.mainLayout.addLayout(agentWaypointLayout)

        self.agent7Start = QLineEdit()
        self.agent7Start.setPlaceholderText("A7 Start")
        agentWaypointLayout.addWidget(self.agent7Start)

        self.agent7Goal = QLineEdit()
        self.agent7Goal.setPlaceholderText("A7 Goal")
        agentWaypointLayout.addWidget(self.agent7Goal)

        agentWaypointLayout = QHBoxLayout()
        self.mainLayout.addLayout(agentWaypointLayout)

        self.agent8Start = QLineEdit()
        self.agent8Start.setPlaceholderText("A8 Start")
        agentWaypointLayout.addWidget(self.agent8Start)

        self.agent8Goal = QLineEdit()
        self.agent8Goal.setPlaceholderText("A8 Goal")
        agentWaypointLayout.addWidget(self.agent8Goal)


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
