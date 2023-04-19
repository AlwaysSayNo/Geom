import math


class Point:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.w_in = 0
        self.w_out = 0

    def __repr__(self):
        return "(" + str(self.x) + "; " + str(self.y) + ")"


class Edge:

    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end
        self.weight = 0
        self.rotation = math.atan2(end.y - start.y, end.x - start.x)

    def __repr__(self):
        return str(edges_arr.index(self))
