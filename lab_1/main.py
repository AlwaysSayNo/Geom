import read
import util
import algo


vertexes_arr = read.read_vertexes("vertexes.txt")
edges_arr = read.read_edges("edges.txt", vertexes_arr)
point = read.read_point("point.txt")

vertexes_arr = sorted(vertexes_arr, key=lambda p: p.y)

v_size = len(vertexes_arr)

edges_in = []
edges_out = []

for i in range(v_size):
    edges_in.append([])
    edges_out.append([])

for e in edges_arr:
    e.weight = 1

    start_i = vertexes_arr.index(e.start)
    end_i = vertexes_arr.index(e.end)

    edges_in[end_i].append(e)
    edges_out[start_i].append(e)

algo.balance_up(vertexes_arr, edges_in, edges_out)
algo.balance_down(vertexes_arr, edges_in, edges_out)

util.plot(vertexes_arr, edges_arr, point)

num_chains = algo.sum_weight(edges_out[0])

ordered_out = []
for v in edges_out:
    v = algo.sort_edges(v)
    ordered_out.append(v)

chains = algo.create_chains(vertexes_arr, ordered_out)

for i, chain in enumerate(chains):
    print(f"Chain {i}: {vertexes_arr.index(chain[0].start)}", end="")
    for edge in chain:
        print(f" {vertexes_arr.index(edge.end)}", end="")
    print()

result = algo.find(point, chains)

if result is not None:
    print(f"Point is between chains {result[0]} and {result[1]}")
else:
    print("Point is not inside graph")

## Find region
