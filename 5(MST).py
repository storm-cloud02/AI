import heapq


class Graph:
    def __init__(self, vertices):  # Use double underscores for __init__
        self.V = vertices  # Number of vertices
        self.graph = {}  # Dictionary to store the graph

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))  # Undirected graph

    def prim_mst(self):
        # Initialize a priority queue
        min_heap = []
        # To track vertices included in the MST
        in_mst = [False] * self.V

        # Check if there are edges from the starting vertex
        if 0 not in self.graph:
            print("Vertex 0 has no edges. Please ensure valid input.")
            return [], 0

        # Start with the first vertex (0)
        in_mst[0] = True
        # Push all edges from the first vertex into the min_heap
        for v, weight in self.graph[0]:
            heapq.heappush(min_heap, (weight, 0, v))  # (weight, from_vertex, to_vertex)

        mst_weight = 0
        mst_edges = []

        while min_heap:
            weight, u, v = heapq.heappop(min_heap)

            if in_mst[v]:
                continue  # Skip if the vertex is already in the MST

            # Include this edge in the MST
            in_mst[v] = True
            mst_weight += weight
            mst_edges.append((u, v, weight))

            # Push all edges from the newly added vertex into the min_heap
            for next_v, next_weight in self.graph[v]:
                if not in_mst[next_v]:
                    heapq.heappush(min_heap, (next_weight, v, next_v))

        return mst_edges, mst_weight


def main():
    # Input number of vertices
    num_vertices = int(input("Enter the number of vertices: "))
    g = Graph(num_vertices)

    # Input edges
    num_edges = int(input("Enter the number of edges: "))
    for _ in range(num_edges):
        u, v, weight = map(int, input("Enter edge (u, v, weight): ").split())
        g.add_edge(u, v, weight)

    # Compute MST
    mst_edges, total_weight = g.prim_mst()

    if mst_edges:
        print("\nEdges in the Minimum Spanning Tree:")
        for u, v, weight in mst_edges:
            print(f"{u} -- {v} (weight: {weight})")
        print("Total weight of MST:", total_weight)
    else:
        print("No MST found due to invalid input.")


if __name__ == "__main__":  # Use double underscores for __name__ and __main__
    main()






