import string

from typing import List
from entity import Point
from entity import Edge


def read_vertexes(file_name: string) -> List[Point]:
    input_arr = open(file_name).read().split()
    v_arr = []

    i = 0
    while i < len(input_arr):
        x = int(input_arr[i])
        y = int(input_arr[i + 1])

        v_arr.append(Point(x, y))
        i += 2

    return v_arr


def read_edges(file_name: string, v_arr: List[Point]) -> List[Edge]:
    input_arr = open(file_name).read().split()
    e_arr = []

    i = 0
    while i < len(input_arr):
        start = v_arr[int(input_arr[i])]
        end = v_arr[int(input_arr[i + 1])]

        e_arr.append(Edge(start, end))
        i += 2

    return e_arr


def read_point(file_name: string) -> Point:
    input_arr = open(file_name).read().split()
    return Point(int(input_arr[0]), int(input_arr[1]))
