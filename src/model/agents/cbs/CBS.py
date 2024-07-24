from copy import deepcopy
from itertools import combinations
from math import fabs

from src.model.agents.cbs.CBSUtils import *


class ConstraintTreeNode:
    """
    A node of the constraint tree build by Conflict-Based Search.

    Attributes:
        constraints (dict): The set of vertex and edge constraints for each agent.
        solution (dict): The current solution to the node.
        cost (int): The total cost of the solution.

    Methods:
        __init__(self): Initializes the constraint tree node.
        __eq__(self, other): Checks if the constraint tree node is equal to other constraint tree node.
        __hash__(self): Returns the hash of the constraint tree node.
        __lt__(self, other): Checks if the constraint tree node is less than other constraint tree node.
    """

    def __init__(self):
        """
        Initializes the constraint tree node.
        """

        self.constraints = {}
        self.solution = {}
        self.cost = 0

    def __eq__(self, other):
        """
        Checks if the constraint tree node is equal to other constraint tree node.

        :param other: The other constraint tree node.
        :return: Boolean value indicating if the constraint tree node is equal to other constraint tree node.
        """

        if not isinstance(other, type(self)):
            return NotImplemented
        return self.solution == other.solution and self.cost == other.cost

    def __hash__(self):
        """
        Returns the hash of the constraint tree node.

        :return: The hash of the constraint tree node.
        """

        return hash(self.cost)

    def __lt__(self, other):
        """
        Checks if the constraint tree node is less than other constraint tree node.

        :param other: The other constraint tree node.
        :return: Boolean value indicating if the constraint tree node is less than other constraint tree node.
        """

        return self.cost < other.cost


class CBS:
    """
    Class implementing the Conflict-Based Search algorithm.

    Methods:
        __init__(self): Initializes the Conflict-Based Search algorithm.
        search(self, graph, waypoints): Performs the Conflict-Based Search algorithm.
        getConflict(self, solution): Gets first conflict from the solution.
        getConstraints(self, conflict): Turns conflict into two constraints.
        getSolution(self, graph, waypoints, constraints): Creates a solution that adheres to the current constraints.
        AStarWithConstraints(self, graph, start, goal, constraints): Performs A* with constraints.
    """

    def __init__(self):
        """
        Initializes the Conflict-Based Search algorithm.
        """
        pass

    def search(self, graph, waypoints):
        """
        Performs the Conflict-Based Search.

        :param graph: The graph to traverse.
        :param waypoints: The start and goal waypoints of the agents in the search.
        :return: The solution found by the search.
        """

        root = ConstraintTreeNode()
        root.constraints = {agent: Constraints() for agent in waypoints.keys()}
        root.solution = self.computeSolution(graph, waypoints, root.constraints)
        if not root.solution:
            return {}
        root.cost = sum([len(path) for path in root.solution.values()])

        openSet = set()
        closedSet = set()

        openSet |= {root}

        while openSet:
            P = min(openSet)
            openSet -= {P}
            closedSet |= {P}

            C = self.getConflict(P.solution)
            if not C:
                plan = {}
                for agent, path in P.solution.items():
                    path_dict_list = [{'t': state.time, 'x': state.location.x, 'y': state.location.y} for state in path]
                    plan[agent] = path_dict_list
                return plan

            newConstraints = self.createConstraintsFromConflict(C)

            for agent in newConstraints.keys():
                A = deepcopy(P)
                A.constraints[agent].vertex_constraints |= newConstraints[agent].vertex_constraints
                A.constraints[agent].edge_constraints |= newConstraints[agent].edge_constraints

                A.solution = self.computeSolution(graph, waypoints, A.constraints)
                if not A.solution:
                    continue
                A.cost = sum([len(path) for path in A.solution.values()])

                if A not in closedSet:
                    openSet |= {A}

        return {}

    def getConflict(self, solution):
        """
        Gets first conflict from the solution.

        :param solution: The solution found by the search.
        :return: The first conflict from the solution.
        """

        maxTime = max([len(path) for path in solution.values()])
        for t in range(maxTime):
            for agentOne, agentTwo in combinations(solution.keys(), 2):
                stateOneA = solution[agentOne][t] if t < len(solution[agentOne]) else solution[agentOne][-1]
                stateOneB = solution[agentOne][t + 1] if (t + 1) < len(solution[agentOne]) else solution[agentOne][-1]

                stateTwoA = solution[agentTwo][t] if t < len(solution[agentTwo]) else solution[agentTwo][-1]
                stateTwoB = solution[agentTwo][t + 1] if (t + 1) < len(solution[agentTwo]) else solution[agentTwo][-1]

                if stateOneA.location == stateTwoA.location:
                    return Conflict(t, 1, agentOne, agentTwo, stateOneA.location)

                if stateOneA.location == stateTwoB.location and stateOneB.location == stateTwoA.location:
                    return Conflict(t, 2, agentOne, agentTwo, stateOneA.location, stateOneB.location)

        return False

    def createConstraintsFromConflict(self, conflict):
        """
        Turns conflict into two constraints.

        :param conflict: Conflict from the solution.
        :return: Dictionary of constraints from the conflict.
        """

        constraints = {}
        if conflict.type == 1:
            constraint = Constraints(vertex=VertexConstraint(conflict.time, conflict.location_1))
            constraints[conflict.agent_1] = constraint
            constraints[conflict.agent_2] = constraint

        elif conflict.type == 2:
            constraint1 = Constraints(edge=EdgeConstraint(conflict.time, conflict.location_1, conflict.location_2))
            constraint2 = Constraints(edge=EdgeConstraint(conflict.time, conflict.location_2, conflict.location_1))

            constraints[conflict.agent_1] = constraint1
            constraints[conflict.agent_2] = constraint2

        return constraints

    def computeSolution(self, graph, waypoints, constraints):
        """
        Creates a solution that adheres to the current constraints.

        :param graph: The graph to traverse.
        :param waypoints: The start and goal waypoints of the agents in the search.
        :param constraints: The current constraints.
        :return: The solution found by the search.
        """

        solution = {}
        for agent in waypoints.keys():
            agentConstraints = constraints.setdefault(agent, Constraints())
            agentSolution = self.AStarWithConstraints(graph, waypoints[agent]['start'], waypoints[agent]['goal'],
                                                      agentConstraints)
            if not agentSolution:
                return False
            solution.update({agent: agentSolution})
        return solution

    def AStarWithConstraints(self, graph, start, goal, constraints):
        """
        Performs A* with constraints.

        :param graph: The graph to traverse.
        :param start: The start location of the agent.
        :param goal: The goal location of the agent.
        :param constraints: The current constraints.
        :return: Agent path from the start location to the goal location.
        """

        open_set = {start}
        closed_set = set()

        came_from = {}
        g_score = {start: 0}
        f_score = {start: (fabs(start.location.x - goal.location.x) + fabs(start.location.y - goal.location.y))}

        while open_set:
            temp_dict = {open_item: f_score.setdefault(open_item, float("inf")) for open_item in open_set}
            current = min(temp_dict, key=temp_dict.get)

            if current.location == goal.location:
                total_path = [current]
                while current in came_from.keys():
                    current = came_from[current]
                    total_path.append(current)
                return total_path[::-1]

            open_set -= {current}
            closed_set |= {current}

            neighbors = []

            directions = [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)]

            for x, y in directions:
                nextLocation = Location(current.location.x + x, current.location.y + y)
                nextState = State(current.time + 1, nextLocation)

                if 0 <= nextState.location.x < graph.width \
                        and 0 <= nextState.location.y < graph.height \
                        and VertexConstraint(nextState.time, nextState.location) not in constraints.vertex_constraints \
                        and (nextState.location.x, nextState.location.y) not in graph.getObstacles() \
                        and EdgeConstraint(current.time, current.location,
                                           nextState.location) not in constraints.edge_constraints:
                    neighbors.append(nextState)

            for neighbor in neighbors:
                if neighbor in closed_set:
                    continue

                tentative_g_score = g_score.setdefault(current, float("inf")) + 1

                if neighbor not in open_set:
                    open_set |= {neighbor}
                elif tentative_g_score >= g_score.setdefault(neighbor, float("inf")):
                    continue

                came_from[neighbor] = current

                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + (
                            fabs(neighbor.location.x - goal.location.x) + fabs(neighbor.location.y - goal.location.y))
        return False

