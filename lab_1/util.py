from matplotlib import pyplot as plt

from typing import List
from entity import Point
from entity import Edge


def plot(v_arr: List[Point], e_arr: List[Edge], point: Point):
    ax = plt.axes()

    i = 0
    for v in v_arr:
        plt.annotate(i, (v.x, v.y), fontsize=20)
        plt.plot(v.x, v.y, marker="o", markersize=4, markerfacecolor="green")
        i += 1

    for e in e_arr:
        ax.arrow(e.start.x, e.start.y,
                 e.end.x - e.start.x, e.end.y - e.start.y, head_width=0, head_length=0)
        plt.annotate(e.weight,
                     xy=((e.end.x + e.start.x) / 2, (e.end.y + e.start.y) / 2),
                     xytext=(10, -10),
                     textcoords='offset points',
                     fontsize=14)

    plt.plot(point.x, point.y, marker="o", markersize=8, markerfacecolor="red")
    plt.show()