class Location:
    """
    A class representing a location.

    Methods:
        __init__(self, x, y): Sets the location's coordinates.
        __eq__(self, other): Checks if two locations are equal.
    """

    def __init__(self, x=-1, y=-1):
        """
        Initializes the location's coordinates.

        :param x: The x coordinate of the location.
        :param y: The y coordinate of the location.
        """

        self.x = x
        self.y = y

    def __eq__(self, other):
        """
        Checks if two locations are equal.

        :param other: The other location to compare.
        :return: Boolean value indicating if two locations are equal.
        """

        return self.x == other.x and self.y == other.y


class State:
    """
    A class representing a state.

    Methods:
        __init__(self, time, location): Creates a state at a given time and location.
        __eq__(self, other): Checks if two states are equal.
        __hash__(self): Returns the hash of the state.
    """

    def __init__(self, time, location):
        """
        Initializes the state's time and coordinates.

        :param time: The time of the state.
        :param location: The location of the state.
        """

        self.time = time
        self.location = location

    def __eq__(self, other):
        """
        Checks if two states are equal.

        :param other: The other state to compare.
        :return: Boolean value indicating if two states are equal.
        """

        return self.time == other.time and self.location == other.location

    def __hash__(self):
        """
        Returns the hash of the state.

        :return: The hash of the state.
        """

        return hash(str(self.time) + str(self.location.x) + str(self.location.y))


class Conflict:
    """
    A class representing a conflict.

    Methods:
        __init__(self, time, cType, a1, a2, v1, v2): Creates a conflict at a given time and location.
    """

    def __init__(self, time, cType, a1, a2, v1, v2=Location()):
        """
        Creates a conflict at a given time and location.
        :param time: The time of the conflict.
        :param cType: The type of conflict.
        :param a1: The first agent in the conflict.
        :param a2: The second agent in the conflict.
        :param v1: The first location of the conflict.
        :param v2: The second location of the conflict.
        """

        self.time = time
        self.type = cType

        self.agent_1 = a1
        self.agent_2 = a2

        self.location_1 = v1
        self.location_2 = v2


class VertexConstraint:
    """
    A class representing a vertex constraint.

    Methods:
        __init(self): Initializes the vertex constraint.
        __eq__(self, other): Checks if two vertex constraints are equal.
        __hash__(self): Returns the hash of the vertex constraint.
    """

    def __init__(self, time, location):
        """
        Initializes the vertex constraint.

        :param time: The time of the vertex constraint.
        :param location: The location of the vertex constraint.
        """

        self.time = time
        self.location = location

    def __eq__(self, other):
        """
        Checks if two vertex constraints are equal.

        :param other: The other vertex constraint to compare.
        :return: Boolean value indicating if two vertex constraints are equal.
        """

        return self.time == other.time and self.location == other.location

    def __hash__(self):
        """
        Returns the hash of the vertex constraint.

        :return: The hash of the vertex constraint.
        """

        return hash(str(self.time) + str((self.location.x, self.location.y)))


class EdgeConstraint:
    """
    A class representing an edge constraint.

    Methods:
        __init__(self, time, locationOne, locationTwo): Creates an edge constraint.
        __eq__(self, other): Checks if two edge constraints are equal.
        __hash__(self): Returns the hash of the edge constraint.
    """

    def __init__(self, time, location_1, location_2):
        """
        Initializes the edge constraint.

        :param time: The time of the edge constraint.
        :param location_1: The first location of the edge constraint.
        :param location_2: The second location of the edge constraint.
        """

        self.time = time
        self.location_1 = location_1
        self.location_2 = location_2

    def __eq__(self, other):
        """
        Checks if two edge constraints are equal.

        :param other: The other edge constraint to compare.
        :return: Boolean value indicating if two edge constraints are equal.
        """

        return self.time == other.time \
            and self.location_1 == other.location_1 \
            and self.location_2 == other.location_2

    def __hash__(self):
        """
        Returns the hash of the edge constraint.

        :return: The hash of the edge constraint.
        """

        return hash(str(self.time)
                    + str((self.location_1.x, self.location_1.y))
                    + str((self.location_2.x, self.location_2.y)))


class Constraints:
    """
    A class representing a set of constraints.

    Methods:
        __init__(self, vertex, edge): Initializes the constraints.
    """

    def __init__(self, vertex=None, edge=None):
        """
        Initializes the constraints.

        :param vertex: The set of vertex constraints.
        :param edge: The set of edge constraints.
        """

        self.vertex_constraints = set()
        self.edge_constraints = set()

        if vertex is not None:
            self.vertex_constraints |= {vertex}

        if edge is not None:
            self.edge_constraints |= {edge}
