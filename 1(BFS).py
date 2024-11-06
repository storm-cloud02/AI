visited = []  # List for visited nodes
queue = []  # Initialize a queue


# Function for BFS
def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:  # Loop to visit each node
        m = queue.pop(0)
        print(m, end=" ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


# Driver code
def main():
    graph = {}
    num_vertices = int(input("Enter the number of vertices: "))

    # Taking input for each vertex and its neighbors
    for i in range(num_vertices):
        vertex = input("Enter vertex: ")
        neighbors = input(f"Enter neighbors of {vertex} separated by space: ").split()
        graph[vertex] = neighbors

    # Starting node for BFS
    start_node = input("Enter the starting node for BFS: ")

    print("\nFollowing is the Breadth-First Search (BFS): ")
    bfs(visited, graph, start_node)


# Call main function
if __name__ == "__main__":
    main()






