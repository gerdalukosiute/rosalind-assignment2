sample_data = """#raw data here"""

def add_edges_for_tree(n, edges):
    graph = {}
    for i in range(1, n + 1):
        graph[i] = []

    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * (n + 1) #to ensure each node is visited once in DFS

    def DFS(node):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                DFS(neighbor)

    connected = 0

    for node in range(1, n + 1):
        if not visited[node]:
            DFS(node)
            connected += 1

    #if n-1 edges satisfied and no cycles (implied in exercise), graph = tree
    edges_needed= connected - 1

    return edges_needed

def format_input(sample_data):
    lines = sample_data.strip().split('\n')
    n = int(lines[0])
    edges = [tuple(map(int, line.split())) for line in lines[1:]]
    return n, edges

n, edges = format_input(sample_data)
result = add_edges_for_tree(n, edges)
print(result)