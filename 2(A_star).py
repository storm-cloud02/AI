def aStarAlgo(start_node, stop_node):
    open_set = set([start_node])
    closed_set = set()
    g = {}  # Store distance from starting node
    parents = {}  # Parents contain an adjacency map of all nodes

    # Distance of starting node from itself is zero
    g[start_node] = 0
    # Start node is root node, i.e., it has no parent node
    parents[start_node] = start_node

    while len(open_set) > 0:
        n = None
        # Node with lowest f() is found
        for v in open_set:
            if n == None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v

        if n == stop_node or Graph_nodes[n] == None:
            pass
        else:
            for (m, weight) in get_neighbors(n):
                # Nodes 'm' not in open_set and closed_set are added to open_set
                # n is set as the parent of m
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                else:
                    if g[m] > g[n] + weight:
                        # Update g(m)
                        g[m] = g[n] + weight
                        parents[m] = n
                        # If m is in closed_set, remove and add to open_set
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)

        if n == None:
            print('Path does not exist!')
            return None

        # If the current node is the stop_node, reconstruct the path from it to the start_node
        if n == stop_node:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            print('Path found: {}'.format(path))
            return path

        # Remove n from the open_list, and add it to closed_list
        # because all of its neighbors were inspected
        open_set.remove(n)
        closed_set.add(n)

    print('Path does not exist!')
    return None


# Function to return neighbors and their distances from the passed node
def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None


# Function to get heuristic distances from each node
def heuristic(n):
    H_dist = {
        'A': 11,
        'B': 6,
        'C': 5,
        'D': 7,
        'E': 3,
        'F': 6,
        'G': 5,
        'H': 3,
        'I': 1,
        'J': 0
    }
    return H_dist[n]


# Input the graph from the user
def input_graph():
    graph = {}
    while True:
        node = input("Enter a node (or type 'done' to finish): ")
        if node.lower() == 'done':
            break
        neighbors_str = input(f"Enter neighbors of {node} and their weights (e.g., B,6 D,3): ")
        neighbors = []
        if neighbors_str.strip():
            for neighbor in neighbors_str.split():
                node_info = neighbor.split(',')
                neighbors.append((node_info[0].strip(), int(node_info[1].strip())))
        graph[node] = neighbors

    return graph


# Driver code to take user inputs and run A* algorithm
print("Enter your graph:")
Graph_nodes = input_graph()

start_node = input("Enter the start node: ")
stop_node = input("Enter the stop node: ")

aStarAlgo(start_node, stop_node)





