from collections import deque


def bfs(graph, root):
    visited = set()
    queue = deque([root])
    visited.add(root)

    parent = {root: None}

    print("\nBFS Traversal:")
    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                parent[neighbour] = vertex
                queue.append(neighbour)

    print()
    return parent


def print_bfs_tree(parent):
    print("\nBFS Tree (Parent -> Child):")
    for node in parent:
        if parent[node] is not None:
            print(f"{parent[node]} -> {node}")




n = int(input("Enter number of nodes: "))
nodes = list(map(int, input("Enter node values: ").split()))

graph = {node: [] for node in nodes}

m = int(input("Enter number of edges: "))
print("Enter edges (u v):")

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

start = int(input("Enter starting node: "))

parent = bfs(graph, start)
print_bfs_tree(parent)
