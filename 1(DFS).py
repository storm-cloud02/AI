# Function for DFS
def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")  # Print the node
        visited.append(node)  # Mark the node as visited
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)  # Recur for all unvisited neighbors


# Input graph from user
def input_graph():
    graph = {}
    n = int(input("Enter the number of nodes: "))

    for _ in range(n):
        node = input("Enter node: ")
        neighbours = input(f"Enter neighbours of {node} (comma separated, leave empty if none): ").split(',')
        neighbours = [neighbour.strip() for neighbour in neighbours if neighbour.strip()]
        graph[node] = neighbours

    return graph


# Driver code
print("Enter your graph:")
graph = input_graph()

visited = []  # List for visited nodes
start_node = input("Enter the starting node for DFS: ")

print("Following is the Depth-First Search (DFS) traversal:")
dfs(visited, graph, start_node)



