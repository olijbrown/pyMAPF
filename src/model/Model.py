from src.model.graph.Graph import Graph
from src.model.agents.SingleAgent import SingleAgent
from src.model.agents.cbs.CBS import *

import time


class Model:
    """
    A class for representing the model in the MVC architecture.

    Attributes:
        maze (Graph): The graph representing a maze.
        singleAgent (SingleAgent): The single-agent that will traverse the maze.
        multiAgent (CBS): The multi-agent that will traverse the maze.
        currentSolution (dict): The current path found by a single-agent search.

    Methods:
        __init__(self): Initializes the model object.
        setMaze(self, width, height): Sets a new maze to a given width and height.
        setObstacle(self, node): Toggles a given node as an obstacle in the maze.
        setSingleAgentPath(self, search, start, goal): Sets the current path to a given search result.
        setMultiAgentPath(self, waypoints): Sets the current path to given waypoints.
    """

    def __init__(self):
        """
        Initializes the model object.
        """

        self.maze = Graph()

        self.singleAgent = SingleAgent()

        self.multiAgent = CBS()

        self.currentSolution = {}

        self.setMaze(4, 4)

    def setMaze(self, width: int, height: int):
        """
        Sets a new maze to a given width and height.

        :param width: The width of the new maze.
        :param height: The height of the new maze.
        """

        self.maze.create(width, height)

    def setObstacle(self, node: int):
        """
        Toggles a given node as an obstacle in the maze.

        :param node: The node to be toggled.
        """

        self.maze.nodes[node].obstacle = not self.maze.nodes[node].obstacle

    def setSingleAgentPath(self, search: int, start: int, goal: int):
        """
        Sets the current single agent path to a given search result.

        :param search: The search to be used for the path.
        :param start: The starting node of the agent.
        :param goal: The goal node of the agent.
        """

        self.maze.reset()

        if search == 0:
            startTime = time.time()
            self.currentSolution = self.singleAgent.DFS(self.maze, start, goal)
            endTime = time.time()
            print("DFS Time: " + str(endTime - startTime))
        elif search == 1:
            startTime = time.time()
            self.currentSolution = self.singleAgent.BFS(self.maze, start, goal)
            endTime = time.time()
            print("BFS Time: " + str(endTime - startTime))
        elif search == 2:
            startTime = time.time()
            self.currentSolution = self.singleAgent.AStar(self.maze, start, goal)
            endTime = time.time()
            print("AStar Time " + str(endTime - startTime))

    def setMultiAgentPath(self, waypoints: dict):
        """
        Sets the current multi-agent path to given waypoints.

        :param waypoints: The waypoints to be used for the path.
        :return: The current multi-agent path to given waypoints.
        """

        self.maze.reset()

        startTime = time.time()
        solution = self.multiAgent.search(self.maze, waypoints)
        endTime = time.time()
        print("CBS Time: " + str(endTime - startTime))
        if solution is not None:
            self.currentSolution = solution
        else:
            self.currentSolution = {}
