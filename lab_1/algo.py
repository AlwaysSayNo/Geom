import math

from typing import List
from entity import Point
from entity import Edge
from numpy import array
from numpy import cross
from numpy.linalg import norm


def sum_weight(edges: List[Edge]) -> int:
    return sum(e.weight for e in edges)


def left_most(edges: List[Edge]) -> Edge:
    return max(edges, key=lambda e: e.rotation)


def sort_edges(edges: List[Edge]) -> List[Edge]:
    return sorted(edges, key=lambda e: e.rotation, reverse=True)


def leftmost_unused(edges: List[Edge]) -> Edge:
    i = 0
    result = edges[0]

    while i < len(edges):
        if edges[i].weight > 0:
            result = edges[i]
            break
        i += 1

    return result


def balance_up(v_arr: List[Point], e_in: List[List[Edge]], e_out: List[List[Edge]]):
    for i in range(1, len(v_arr) - 1):
        v = v_arr[i]

        v.w_in = sum_weight(e_in[i])
        v.w_out = sum_weight(e_out[i])

        if v.w_in > v.w_out:
            left_e = left_most(e_out[i])
            left_e.weight = v.w_in - v.w_out + left_e.weight


def balance_down(v_arr: List[Point], e_in: List[List[Edge]], e_out: List[List[Edge]]):
    for i in range(len(v_arr) - 1, 1, -1):
        v = v_arr[i]

        v.w_in = sum_weight(e_in[i])
        v.w_out = sum_weight(e_out[i])

        if v.w_out > v.w_in:
            left_e = left_most(e_in[i])
            left_e.weight = v.w_out - v.w_in + left_e.weight


def create_chains(v_arr: List[Point], ordered_edges: List[List[Edge]]) -> List[List[Edge]]:
    n = sum_weight(ordered_edges[0])
    chains = []

    for i in range(n):
        chain = []

        curr = 0
        while curr != len(ordered_edges) - 1:
            e = leftmost_unused(ordered_edges[curr])
            chain.append(e)

            e.weight -= 1
            curr = v_arr.index(e.end)

        chains.append(chain)

    return chains


def find(point: Point, chains):
    for i in range(0, len(chains)):
        for e in chains[i]:

            if e.start.y <= point.y <= e.end.y:

                if is_on_vertex(point, e) or is_on_edge(point, e):
                    if i == 0:
                        return [0]
                    else:
                        return [i]

                point_vector = Point(point.x - e.start.x, point.y - e.start.y)
                edge_vector = Point(e.end.x - e.start.x, e.end.y - e.start.y)

                if math.atan2(point_vector.y, point_vector.x) > math.atan2(edge_vector.y, edge_vector.x):
                    if i == 0:
                        return []
                    return [i - 1, i]
    return []


def is_on_vertex(point: Point, e: Edge):
    """
        If point is on vertex then it should have diff_x == 0 and diff_y == 0 with this vertex
    """
    start_v, end_v = get_vertexes_with_edge(point, e)

    return start_v.y == start_v.x == 0 \
        or end_v.y == end_v.x == 0


def is_on_edge(point: Point, e: Edge):
    """
        If point is on edge then one of vertex coordinate should be equal to 0
    """
    start_v, end_v = get_vertexes_with_edge(point, e)

    return start_v.x == end_v.x == 0 \
        or start_v.y == end_v.y == 0


def get_vertexes_with_edge(point: Point, e: Edge):
    start_v = Point(point.x - e.start.x, point.y - e.start.y)
    end_v = Point(point.x - e.end.x, point.y - e.end.y)

    return [start_v, end_v]


def find_on_edge(point: Point, chain: List[Edge]):
    return find_on_edges(point, chain)[0]


def find_on_edges(point: Point, chain: List[Edge]):
    return [e for e in chain if e.start.y <= point.y <= e.end.y]


def find_closest_edge(point: Point, l_chain: List[Edge], r_chain: List[Edge]):
    min_d = None
    edge = None

    for e in find_on_edges(point, l_chain + r_chain):
        curr_d = point_line_distance(point, e)
        if min_d is None or min_d >= curr_d:
            min_d = curr_d
            edge = e

    return edge


def point_line_distance(p: Point, line: Edge):
    p1, p2, p3 = array([p.x, p.y]), array([line.start.x, line.start.y]), array([line.end.x, line.end.y])
    return norm(cross(p2 - p1, p1 - p3)) / norm(p2 - p1)
