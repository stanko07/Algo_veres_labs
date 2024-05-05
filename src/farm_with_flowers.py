def relax_weight(graph, path, cur_flow):
    for edge in path:
        graph[edge[0]][edge[1]] -= cur_flow
        if graph[edge[0]][edge[1]] == 0:
            del graph[edge[0]][edge[1]]


def DFS(graph, start, destination):
    stack = [(start, float("inf"), None)]
    visited = set()
    route = []
    min_weight = float("inf")

    while stack:
        cur_element, weight, parent = stack.pop()
        if parent:
            for p in route.copy():
                if p[0] == parent:
                    route.remove(p)
            route.append((parent, cur_element))

        min_weight = min(min_weight, weight)
        if (cur_element not in graph
                or cur_element == destination):
            break
        visited.add(cur_element)

        for vertex, edge_weight in graph[cur_element].items():
            if vertex in visited:
                continue
            stack.append((vertex, edge_weight, cur_element))

    if (not stack and len(route) == 0
            or route[0][0] != start or
            route[-1][1] != destination):
        return [], 0
    return route, min_weight


def max_flow(filename):
    start, destination, graph = read_file(filename)
    total_flow = 0
    while True:
        path, found_flow = DFS(graph, start, destination)
        if found_flow == 0 or path[0][0] != 'MF':
            break
        total_flow += found_flow
        relax_weight(graph, path, found_flow)
    return total_flow


def read_file(file_path):
    adjacency_list = {}

    with open(file_path, 'r', encoding='utf-8') as file:
        farms = file.readline().strip().split(',')
        shops = file.readline().strip().split(',')
        adjacency_list["MF"] = {farm: float('inf') for farm in farms}
        for shop in shops:
            if shop not in adjacency_list:
                adjacency_list[shop] = {"MS": float('inf')}
                for line in file:
                    source, destination, weight = line.strip().split(',')
                    if source not in adjacency_list:
                        adjacency_list[source] = {}
                    adjacency_list[source][destination] = int(weight)
            return "MF", "MS", adjacency_list
