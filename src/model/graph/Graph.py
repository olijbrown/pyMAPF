from src.model.graph.Node import Node


class Graph:
    """
    A class for representing a graph/maze data-structure.

    Attributes:
        width (int): The width of the graph/maze.
        height (int): The height of the graph/maze.
        nodes (list): The list of nodes in the graph/maze.

    Methods:
        __init__(self): Initializes the graph/maze object.
        create(self, w, h): Creates a new graph/maze of size (width * height).
        reset(self): Resets each node in the graph/maze back to its original state.
        heuristic(self, a, b): Returns the manhattan heuristic from a to b.
        getDimensions(): Returns the dimensions of the graph/maze.
        getObstacles(): Returns the obstacles of the graph/maze.
    """

    def __init__(self):
        """
        Initializes the graph/maze object.
        """

        self.width = 0
        self.height = 0
        self.nodes = {}

    def create(self, width: int, height: int):
        """
        Creates a new graph/maze of size (width * height).

        :param width: Width of the maze.
        :param height: Height of the maze.
        """

        self.width = width
        self.height = height
        self.nodes = {}

        for y in range(self.height):
            for x in range(self.width):
                self.nodes[y * self.width + x] = Node(x, y)

        for y in range(self.height):
            for x in range(self.width):
                if y > 0:
                    self.nodes[y * self.width + x].neighbours.append((y - 1) * self.width + x)
                if y < self.height - 1:
                    self.nodes[y * self.width + x].neighbours.append((y + 1) * self.width + x)
                if x > 0:
                    self.nodes[y * self.width + x].neighbours.append(y * self.width + (x - 1))
                if x < self.width - 1:
                    self.nodes[y * self.width + x].neighbours.append(y * self.width + (x + 1))

    def reset(self):
        """
        Resets each node in the graph/maze back to its original state.
        """

        for y in range(self.height):
            for x in range(self.width):
                self.nodes[y * self.width + x].gScore = 0
                self.nodes[y * self.width + x].fScore = 0
                self.nodes[y * self.width + x].visited = False
                self.nodes[y * self.width + x].parent = None

    def heuristic(self, a: int, b: int) -> int:
        """
        Returns the manhattan heuristic from a to b.

        :param a: The id of the starting node.
        :param b: The id of the goal node.
        :return: The manhattan heuristic between a and b.
        """

        return abs(self.nodes[a].xPos - self.nodes[b].xPos) + abs(self.nodes[a].yPos - self.nodes[b].yPos)

    def getDimensions(self) -> list:
        """
        Returns the dimensions of the graph/maze.
        :return: The dimensions of the graph/maze.
        """

        return [self.width, self.height]

    def getObstacles(self) -> list:
        """
        Returns the obstacles of the graph/maze.
        :return: The obstacles of the graph/maze.
        """

        obstacles = []

        for y in range(self.height):
            for x in range(self.width):
                node = self.nodes[y * self.width + x]
                if node.obstacle:
                    obstacles.append((node.yPos, node.xPos))

        return obstacles
