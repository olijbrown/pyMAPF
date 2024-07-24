import heapq
from collections import deque

from src.model.graph.Node import Node
from src.model.graph.Graph import Graph


class SingleAgent:
    """
    A class for representing a single agent.

    Methods:
        __init__(self): Initializes the single-agent object.
        DFS(self, graph, start, goal): Performs the DFS on a given graph/maze.
        BFS(self, graph, start, goal): Performs the BFS on a given graph/maze.
        AStar(self, graph, start, goal): Performs the A* search on a given graph/maze.
        createPath(self, node): Creates a path from the given node to its origin.
    """

    def __init__(self):
        """
        Initializes the single-agent object.
        """

        pass

    def DFS(self, graph: Graph, start: int, goal: int) -> dict:
        """
        Performs the DFS on a given graph/maze.

        :param graph: The graph/maze the agent will traverse.
        :param start: The starting node for the search.
        :param goal: The goal node for the search.
        :return: The resulting path (if one has been found).
        """

        stack = [graph.nodes[start]]
        graph.nodes[start].visited = True

        while stack:
            currentNode = stack.pop()

            if currentNode == graph.nodes[goal]:
                path = self.createPath(currentNode)
                return path

            for index in currentNode.neighbours:
                neighbour = graph.nodes[index]
                if not neighbour.visited and not neighbour.obstacle:
                    neighbour.parent = currentNode
                    stack.append(neighbour)
                    neighbour.visited = True

        return {}

    def BFS(self, graph: Graph, start: int, goal: int) -> dict:
        """
        Performs the BFS on a given graph/maze.

        :param graph: The graph/maze the agent will traverse.
        :param start: The starting node for the search.
        :param goal: The goal node for the search.
        :return: The resulting path (if one has been found).
        """

        queue = deque()
        queue.append(graph.nodes[start])
        graph.nodes[start].visited = True

        while queue:
            currentNode = queue.popleft()

            if currentNode == graph.nodes[goal]:
                path = self.createPath(currentNode)
                return path

            for index in currentNode.neighbours:
                neighbour = graph.nodes[index]
                if not neighbour.visited and not neighbour.obstacle:
                    neighbour.parent = currentNode
                    queue.append(neighbour)
                    neighbour.visited = True

        return {}

    def AStar(self, graph: Graph, start: int, goal: int) -> dict:
        """
        Performs the A* search on a given graph/maze.

        :param graph: The graph/maze the agent will traverse.
        :param start: The starting node for the search.
        :param goal: The goal node for the search.
        :return: The resulting path (if one has been found).
        """

        openSet = [(0, graph.nodes[start])]
        heapq.heapify(openSet)

        while openSet:
            currentNode = heapq.heappop(openSet)[1]

            if currentNode == graph.nodes[goal]:
                path = self.createPath(currentNode)
                return path

            currentNode.visited = True

            for index in currentNode.neighbours:
                neighbour = graph.nodes[index]

                if neighbour.obstacle or neighbour.visited:
                    continue

                tempGScore = currentNode.gScore + 1
                if neighbour not in openSet or tempGScore < neighbour.gScore:
                    neighbour.parent = currentNode
                    neighbour.gScore = tempGScore
                    neighbour.fScore = tempGScore + graph.heuristic(index, goal)

                    if neighbour not in openSet:
                        heapq.heappush(openSet, (neighbour.fScore, neighbour))

        return {}

    def createPath(self, node: Node):
        """
        Creates a path from the given node to its origin.

        :param node: The node to create the path from.
        :return: List of nodes representing the path.
        """

        path = []
        parent = node
        while parent.parent is not None:
            path.append(parent)
            parent = parent.parent
        path.append(parent)
        path.reverse()

        if not path:
            return {}

        solution = {"agent0": []}
        counter = 0
        for position in path:
            solution["agent0"].append({
                "t": counter,
                "x": position.yPos,
                "y": position.xPos})
            counter += 1

        return solution
