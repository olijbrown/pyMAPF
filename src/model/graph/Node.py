class Node:
    """
    A class for representing a node in a graph.

    Attributes:
        xPos (int): X-coordinate of the node.
        yPos (int): Y-coordinate of the node.
        gScore (float): Current distance from the start node in a search.
        fScore (float): Current estimated distance to the end node in a search.
        obstacle (bool): Indicates whether the node is an obstacle.
        visited (bool): Indicates whether the node has been visited.
        parent (Node): The parent node of this node.
        neighbours ([Node]): List of nodes that neighbour this one.

    Methods:
        __init__(self, x, y): Initializes a node with co-ordinates (x, y)
        __str__(self): Returns a string representation of the node.
        __lt__(self, other): Returns true if the node is less than the other.
    """

    def __init__(self, x, y):
        """
        Initializes a node with co-ordinates (x, y)

        :param x: X-coordinate of the node.
        :param y: Y-coordinate of the node.
        """

        self.xPos = x
        self.yPos = y
        self.gScore = 0
        self.fScore = 0
        self.obstacle = False
        self.visited = False
        self.parent = None
        self.neighbours = []

    def __str__(self) -> str:
        """
        Returns the string representation of the node.

        :return: String representation of the node.
        """

        return f"(x:{self.xPos}, y:{self.yPos})"

    def __lt__(self, other) -> bool:
        """
        Returns true if the node is less than the other.
        :param other: The node to compare.
        :return: Boolean indicating if the node is less than the other.
        """

        return self.fScore < other.fScore
