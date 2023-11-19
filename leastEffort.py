import heapq
import math


class Node:
    def __init__(self, height, column, row):
        self.height = height
        self.column = column
        self.row = row
        self.min_effort_to_node = 0 if (row == 0 and column == 0) else math.inf
        self.preceding_node = None
        self.adjacent_nodes = []


class Edge:
    def __init__(self, node1, node2, effort):
        self.node1 = node1
        self.node2 = node2
        self.effort = effort


def link_cells(heights):
    completed_cells = []
    completed_edges = []

    for row, cells in enumerate(heights):
        for column, cell in enumerate(cells):
            current_cell = Node(cell, column, row)

            if row > 0:
                top_cell = filter(lambda x: x.column is column and x.row is row - 1, completed_cells).__next__()
                current_cell.adjacent_nodes.append(top_cell)
                top_cell.adjacent_nodes.append(current_cell)
                completed_edges.append(Edge(top_cell, current_cell, abs(top_cell.height - current_cell.height)))

            if column > 0:
                left_cell = filter(lambda x: x.column is column - 1 and x.row is row, completed_cells).__next__()
                current_cell.adjacent_nodes.append(left_cell)
                left_cell.adjacent_nodes.append(current_cell)
                completed_edges.append(Edge(left_cell, current_cell, abs(current_cell.height - left_cell.height)))

            completed_cells.append(current_cell)

    return completed_cells, completed_edges


def find_min_effort_plus(heights: list):
    rows, cols = len(heights), len(heights[0])
    visited_cells = set()
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    min_heap = [[0, 0, 0]]

    while min_heap:
        diff, row, col = heapq.heappop(min_heap)

        if (row, col) in visited_cells:
            continue

        visited_cells.add((row, col))
        if (row, col) == (rows - 1, cols - 1):
            return diff

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if new_row < 0 or new_col < 0 or new_row == rows or new_col == cols or (new_row, new_col) in visited_cells:
                continue

            effort = abs(heights[row][col] - heights[new_row][new_col])
            max_effort = max(diff, effort)
            heapq.heappush(min_heap, [max_effort, new_row, new_col])


def find_min_effort(nodes):
    explored_nodes = []

    while len(nodes) > 0:
        nodes.sort(key=lambda x: x.min_effort_to_node)
        node_to_explore = nodes[0]

        for adj_node in node_to_explore.adjacent_nodes:
            effort_to_node = abs(node_to_explore.height - adj_node.height)
            max_effort_in_path = effort_to_node if effort_to_node > node_to_explore.min_effort_to_node else node_to_explore.min_effort_to_node

            if max_effort_in_path < adj_node.min_effort_to_node:
                adj_node.min_effort_to_node = max_effort_in_path

        explored_nodes.append(node_to_explore)
        nodes.remove(node_to_explore)

    return sorted(explored_nodes, key=lambda x: x.row + x.column)


def find_paths(nodes):
    final_node = nodes[-1]
    paths = []

    def explore_path(node, current_path=None):
        if current_path is None:
            current_path = []

        current_path.append(node)

        if node is final_node:
            paths.append(list(current_path))
            current_path.remove(node)
            return

        for new_node in node.adjacent_nodes:
            if new_node not in current_path:
                explore_path(new_node, current_path)

        current_path.remove(node)
        return

    explore_path(nodes[0])
    return paths


def get_height_differences(path):
    if len(path) == 1:
        return [0]

    return [abs(path[i + 1].height - path[i].height) for i in range(len(path) - 1)]


def main(heights):
    print(find_min_effort_plus(heights))


if __name__ == '__main__':
    main([[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]])
