from heapq import heappush, heappop

# --- Constants for standard edit distance costs ---
COST_INSERTION = 1   # Cost for inserting a character ('-')
COST_DELETION = 1    # Cost for deleting a character
COST_SUBSTITUTION = 2 # Cost for replacing one character with another

class Node:
    """Represents a state in the search space."""
    def __init__(self, parent, pos, cost):
        self.parent = parent
        self.pos = pos  # (x, y) position in the alignment grid
        self.cost = cost

    def __lt__(self, other):
        # Comparison for the priority queue
        return self.cost < other.cost

def get_successors(node, str1, str2):
    """Generates valid next moves (nodes) from the current node."""
    successors = []
    x, y = node.pos

    # Move 1: Diagonal (Match or Substitution)
    if x < len(str1) and y < len(str2):
        move_cost = 0 if str1[x] == str2[y] else COST_SUBSTITUTION
        successors.append(Node(node, (x + 1, y + 1), node.cost + move_cost))

    # Move 2: Horizontal (Deletion from str1)
    if x < len(str1):
        successors.append(Node(node, (x + 1, y), node.cost + COST_DELETION))

    # Move 3: Vertical (Insertion into str1)
    if y < len(str2):
        successors.append(Node(node, (x, y + 1), node.cost + COST_INSERTION))
        
    return successors

def reconstruct_path(final_node, str1, str2):
    """Backtracks from the goal to reconstruct the aligned strings."""
    aligned1, aligned2 = [], []
    curr = final_node
    
    while curr.parent:
        px, py = curr.parent.pos
        cx, cy = curr.pos

        if cx > px and cy > py:  # Diagonal move
            aligned1.append(str1[px])
            aligned2.append(str2[py])
        elif cx > px:  # Horizontal move (Deletion)
            aligned1.append(str1[px])
            aligned2.append('-')
        else:  # Vertical move (Insertion)
            aligned1.append('-')
            aligned2.append(str2[py])
        curr = curr.parent

    # The lists are built backwards, so reverse them
    return "".join(reversed(aligned1)), "".join(reversed(aligned2))

def solve_shortest_path(str1, str2):
    """
    Solves the alignment problem by finding the shortest path in a grid.
    Uses A* search (effectively Dijkstra's here as heuristic is 0).
    """
    pq = [Node(None, (0, 0), 0)]  # Priority Queue with the root node
    visited = set()

    while pq:
        current_node = heappop(pq)

        if current_node.pos in visited:
            continue
        visited.add(current_node.pos)

        # Check if we've reached the goal
        if current_node.pos == (len(str1), len(str2)):
            final_cost = current_node.cost
            aligned1, aligned2 = reconstruct_path(current_node, str1, str2)
            return final_cost, aligned1, aligned2

        # Explore neighbors
        for successor in get_successors(current_node, str1, str2):
            if successor.pos not in visited:
                heappush(pq, successor)
    
    return -1, "Error", "Error" # Should not be reached