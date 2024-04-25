def is_valid_move(matrix, visited, x, y):
    rows = len(matrix)
    cols = len(matrix[0])
    return 0 <= x < rows and 0 <= y < cols and matrix[x][y] == 1 and (x, y) not in visited


def shortest_path(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    steps = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = [(i, 0) for i in range(rows) if matrix[i][0] == 1]
    visited = set(queue)
    path_length = 0
    path_tracker = {node: None for node in queue}
    while queue:
        depth_size = len(queue)
        for i in range(depth_size):
            x, y = queue.pop(0)
            if y == cols - 1:
                path = []
                current_node = (x, y)
                while current_node is not None:
                    path.insert(0, current_node)
                    current_node = path_tracker[current_node]
                return path_length, path
            for dir_x, dir_y in steps:
                new_x, new_y = x + dir_x, y + dir_y
                if is_valid_move(matrix, visited, new_x, new_y):
                    visited.add((new_x, new_y))
                    queue.append((new_x, new_y))
                    path_tracker[(new_x, new_y)] = (x, y)
        path_length += 1
    return -1, []


def transform_matrix(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    new_matrix = [[matrix[x][y] for y in range(columns)] for x in range(rows)]
    for x in range(rows):
        for y in range(columns):
            if matrix[x][y] == 0:
                for dir_x in [-1, 0, 1]:
                    for dir_y in [-1, 0, 1]:
                        new_x, new_y = x + dir_x, y + dir_y
                        if 0 <= new_x < rows and 0 <= new_y < columns:
                            new_matrix[new_x][new_y] = 0
    return new_matrix


def read_matrix(file_path):
    with open(file_path, 'r') as file:
        matrix = [list(map(int, line.strip().split(', '))) for line in file]
    return matrix


def write_result(filename, shortest_path, path):
    with open(filename, 'w') as file:
        file.write(f"Shortest Path: {shortest_path}\n")
        file.write(f"Path: {path}")


def main():
    matrix = read_matrix("../test/resorses/input.txt")
    transformed_matrix = transform_matrix(matrix)
    result = shortest_path(transformed_matrix)
    length, path = result
    write_result("../test/resorses/output.txt", length, path)


if __name__ == "__main__":
    main()
