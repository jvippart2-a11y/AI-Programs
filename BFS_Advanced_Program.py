from collections import deque


n = int(input("Enter number of nodes: "))

V = input("Enter node values: ").split()


g = {x: [] for x in V}

m = int(input("Enter number of edges: "))

print("Enter edges (u v):")
for _ in range(m):
    a, b = input().split()
    g[a].append(b)
    g[b].append(a)

start = input("Enter starting node: ")

q = deque([start])
visited = set()
parent = {start: None}
step = 1


def get_path(node):
    path = []
    while node is not None:
        path.append(node)
        node = parent[node]
    return path[::-1]


while q:
    x = q.popleft()
    visited.add(x)

    unvisited = set(V) - visited

    print(f"\nStep {step}")
    print("Source node:", x)
    print("Adjacent:", g[x])
    print("Visited:", visited)
    print("Unvisited:", unvisited)
    print("Path:", " -> ".join(get_path(x)))

    for y in g[x]:
        if y not in visited and y not in q:
            q.append(y)
            parent[y] = x

    step += 1



print("\nOptimal Solution (Shortest paths from source):")
for node in V:
    if node in parent:
        print(f"{start} -> {node}: {' -> '.join(get_path(node))}")
    else:
        print(f"{start} -> {node}: No path")
