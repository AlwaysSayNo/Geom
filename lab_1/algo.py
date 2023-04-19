import math

from typing import List
from entity import Point
from entity import Edge


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
            point_start_vector = Point(point.x - e.start.x, point.y - e.start.y)
            point_end_vector = Point(point.x - e.end.x, point.y - e.end.y)

            if math.atan2(point_start_vector.y, point_start_vector.x) == 0 \
                    or math.atan2(point_end_vector.y, point_end_vector.x) == 0:
                if i == 0:
                    return [0, 1]
                else:
                    return [i - 1, i]

            if e.start.y < point.y < e.end.y:
                edge_vector = Point(e.end.x - e.start.x, e.end.y - e.start.y)

                if math.atan2(point_start_vector.y, point_start_vector.x) > math.atan2(edge_vector.y, edge_vector.x):
                    if i == 0:
                        return None
                    return [i - 1, i]
