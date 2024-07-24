import random

from PyQt5.QtCore import QTimer

import src.model.Model as Model
import src.view.View as View

from src.model.agents.cbs.CBSUtils import *


class Controller:
    """
    A class for representing the model in the MVC architecture.

    Attributes:
        model (Model): The model of the MVC architecture.
        view (View): The view of the MVC architecture.
        maxIterations (int): Number of iterations in the search animation.
        currentIteration (int): Counter for the current iteration number.
        timer (QTimer): QTimer object for the timer of the animation.
        currentSASearchType (int): The current Single-Agent Search type.
        currentMAAgentNumber (int): The current number of agents in the Multi-Agent Search.

    Methods:
        __init__(self, model, view): Initializes the controller class.
        setSingleAgent(self): Set the application to the Single-Agent mode.
        setMultiAgent(self): Set the application to the Multi-Agent mode.
        setInfo(self): Display the info instructions to the display.
        setMaze(self, size): Sets a maze to a given size.
        setObstacle(self, x, y): Sets an obstacle to a given position.
        setRandomObstacles(self): Create a random number of obstacles.
        setSingleAgentSearch(self, search): Sets the type of Single-Agent search.
        setRandomSingleAgent(self): Set random Single-Agent search conditions.
        playSingleAgentSearch(self): Play a Single-Agent search animation.
        setMAAgentNumber(self, number): Sets the number of agents in the Multi-Agent Search.
        playMultiAgentSearch(self): Play a Multi-Agent search animation.
        playAgentAnimation(agent): Play an animation on the current solution.
    """

    def __init__(self, model: Model, view: View):
        """
        Initializes the controller class.

        :param model: The model of the MVC architecture.
        :param view: The view of the MVC architecture.
        """

        self.model = model
        self.view = view

        self.maxIterations = 0
        self.currentIteration = 0

        self.timer = QTimer()
        self.timer.timeout.connect(self.playAgentAnimation)

        self.currentSASearchType = 0

        self.currentMAAgentNumber = 4

        self.view.sidebar.SAButton.clicked.connect(self.setSingleAgent)
        self.view.sidebar.MAButton.clicked.connect(self.setMultiAgent)

        self.view.header.headerInfoButton.clicked.connect(self.setInfo)

        self.view.singleAgentMenu.mazeSelectButtonGroup.buttonClicked[int].connect(self.setMaze)
        self.view.singleAgentMenu.searchSelectButtonGroup.buttonClicked[int].connect(self.setSingleAgentSearch)
        self.view.singleAgentMenu.randomiseButton.clicked.connect(self.setRandomSingleAgent)
        self.view.singleAgentMenu.playButton.clicked.connect(self.playSingleAgentSearch)

        self.view.multiAgentMenu.mazeSelectButtonGroup.buttonClicked[int].connect(self.setMaze)
        self.view.multiAgentMenu.agentNumberButtonGroup.buttonClicked[int].connect(self.setMAAgentNumber)
        self.view.multiAgentMenu.randomiseButton.clicked.connect(self.setRandomMASearch)
        self.view.multiAgentMenu.playButton.clicked.connect(self.playMultiAgentSearch)

        self.view.maze.cellClicked.connect(self.setObstacle)

    def setSingleAgent(self):
        """
        Sets the application to the Single-Agent mode.
        """

        self.view.header.headerTitle.setText("Single-Agent Search")
        self.view.drawSAMenu()
        self.setInfo()

    def setMultiAgent(self):
        """
        Sets the application to the Multi-Agent mode.
        """

        self.view.header.headerTitle.setText("Multi-Agent Search")
        self.view.drawMAMenu()
        self.setInfo()

    def setInfo(self):
        """
        Display the info instructions to the display.
        """

        self.view.maze.drawInfo()

    def setMaze(self, size: int):
        """
        Sets the maze to a given size.

        :param size: Size of the maze.
        """

        if size == 0:
            self.model.setMaze(8, 8)
            self.view.maze.drawMaze(8, 8)
        elif size == 1:
            self.model.setMaze(16, 16)
            self.view.maze.drawMaze(16, 16)
        elif size == 2:
            self.model.setMaze(32, 32)
            self.view.maze.drawMaze(32, 32)

    def setObstacle(self, x, y):
        """
        Sets the obstacle in a given position.

        :param x: The x coordinate of the node.
        :param y: The y coordinate of the node.
        """

        self.model.setObstacle(x * self.model.maze.width + y)
        if self.model.maze.nodes[x * self.model.maze.width + y].obstacle:
            self.view.maze.changeCell(x, y, "#20111B")
        else:
            self.view.maze.changeCell(x, y, "white")

    def setRandomObstacles(self):
        """
        Create a random number of obstacles.

        :return: The set of obstacles and the total number of nodes in the maze.
        """
        dimensions = self.model.maze.getDimensions()
        nodeTotal = (dimensions[0] * dimensions[1]) - 1

        lowerBound = int(nodeTotal * (20 / 100))
        upperBound = int(nodeTotal - (nodeTotal * (70 / 100)))

        totalObstacles = random.randint(lowerBound, upperBound)

        obstacles = set()
        while len(obstacles) < totalObstacles:
            node = random.randint(0, nodeTotal)

            if node not in obstacles:
                obstacles.add(node)

        for obstacle in obstacles:
            self.model.setObstacle(obstacle)
            x, y = divmod(obstacle, dimensions[1])
            self.view.maze.changeCell(x, y, "#20111B")

        return obstacles, nodeTotal

    def setSingleAgentSearch(self, search: int):
        """
        Sets the type of Single-Agent search.

        :param search: The type of search to be performed.
        """

        self.currentSASearchType = search

    def setRandomSingleAgent(self):
        """
        Set random Single-Agent search conditions.
        """

        self.setMaze(self.view.singleAgentMenu.mazeSelectButtonGroup.checkedId())
        obstacles, nodeTotal = self.setRandomObstacles()

        while True:
            start = random.randint(0, nodeTotal)
            if start not in obstacles:
                break

        while True:
            goal = random.randint(0, nodeTotal)
            if goal not in obstacles and start != goal:
                break

        self.view.singleAgentMenu.agentStart.setText(str(start))
        self.view.singleAgentMenu.agentGoal.setText(str(goal))

    def playSingleAgentSearch(self):
        """
        Play a single-agent search animation.
        """

        self.timer.stop()

        obstacles = self.model.maze.getObstacles()
        self.setMaze(self.view.singleAgentMenu.mazeSelectButtonGroup.checkedId())
        for obstacle in obstacles:
            self.setObstacle(obstacle[0], obstacle[1])

        start = int(self.view.singleAgentMenu.agentStart.text())
        goal = int(self.view.singleAgentMenu.agentGoal.text())
        self.model.setSingleAgentPath(self.currentSASearchType, start, goal)

        if self.model.currentSolution:
            self.maxIterations = max(len(agent_positions) for agent_positions in self.model.currentSolution.values())
            self.currentIteration = 0
            self.timer.start(300)

    def setMAAgentNumber(self, number: int):
        """
        Sets the number of agents in a Multi-Agent search.

        :param number: The number of agents in the Multi-Agent search.
        """
        self.currentMAAgentNumber = number

    def setRandomMASearch(self):
        """
        Set random Multi-Agent search conditions.
        """

        self.setMaze(self.view.multiAgentMenu.mazeSelectButtonGroup.checkedId())
        obstacles, nodeTotal = self.setRandomObstacles()

        for agent in range(1, self.currentMAAgentNumber + 1):
            while True:
                start = random.randint(0, nodeTotal)
                if start not in obstacles:
                    break

            while True:
                goal = random.randint(0, nodeTotal)
                if goal not in obstacles and start != goal:
                    break

            getattr(self.view.multiAgentMenu, f"agent{agent}Start").setText(str(start))
            getattr(self.view.multiAgentMenu, f"agent{agent}Goal").setText(str(goal))
            obstacles.add(start)
            obstacles.add(goal)

    def playMultiAgentSearch(self):
        """
        Play a multi-agent search animation.
        """

        self.timer.stop()

        obstacles = self.model.maze.getObstacles()
        self.setMaze(self.view.multiAgentMenu.mazeSelectButtonGroup.checkedId())
        for obstacle in obstacles:
            self.setObstacle(obstacle[0], obstacle[1])

        waypoints = {}
        for agent in range(1, self.currentMAAgentNumber + 1):
            agentStart = int(getattr(self.view.multiAgentMenu, f"agent{agent}Start").text())
            agentGoal = int(getattr(self.view.multiAgentMenu, f"agent{agent}Goal").text())
            xStart, yStart = divmod(agentStart, self.model.maze.height)
            xGoal, yGoal = divmod(agentGoal, self.model.maze.height)
            waypoints[f"agent{agent}"] = {
                "start": State(0, Location(xStart, yStart)),
                "goal": State(0, Location(xGoal, yGoal))
            }

        self.model.setMultiAgentPath(waypoints)

        if self.model.currentSolution:
            self.maxIterations = max(len(agent_positions) for agent_positions in self.model.currentSolution.values())
            self.currentIteration = 0
            self.timer.start(300)

    def playAgentAnimation(self):
        """
        Play an agent animation.
        """

        if self.maxIterations != 0:
            previousPositions = []
            currentPositions = []
            for agent, positions in self.model.currentSolution.items():
                if self.currentIteration < len(positions):
                    currentPosition = positions[self.currentIteration]
                    agentName = agent.replace("agent", "")
                    currentPositions.append((currentPosition['x'], currentPosition['y'], "#BE100E", agentName))
                    if self.currentIteration != 0:
                        previousPosition = positions[self.currentIteration - 1]
                        previousPositions.append((previousPosition['x'], previousPosition['y'], "white", ""))
            for previous in previousPositions:
                self.view.maze.changeCell(previous[0], previous[1], previous[2], previous[3])
            for current in currentPositions:
                self.view.maze.changeCell(current[0], current[1], current[2], current[3])
            self.currentIteration += 1
            self.maxIterations -= 1
        else:
            self.timer.stop()
