# String Alignment & Edit Distance Solvers

This repository provides Python implementations for solving the string alignment problem, also known as calculating the minimum **edit distance**. The goal is to find the minimum cost to transform one string into another using a series of edit operations: insertion, deletion, and substitution.

This problem is fundamental in computational linguistics (e.g., Word Error Rate - WER), bioinformatics (sequence alignment), and computer science (diff utilities).

This project provides two classic algorithms to solve the problem:
1.  **Shortest Path Search (A*)**: Models the problem as finding the cheapest path on a grid.
2.  **Dynamic Programming**: The standard and highly efficient textbook solution.

## Algorithms Implemented

### 1. Shortest Path Search (`shortest_path_solver.py`)

This approach models the alignment problem as a graph search.

-   **Model**: An alignment between `string1` (length `m`) and `string2` (length `n`) can be viewed as a path on an `(m+1) x (n+1)` grid. A node at `(i, j)` represents the alignment of the prefix `string1[:i]` with `string2[:j]`.
-   **Actions**:
    -   **Diagonal move** `(i, j) -> (i+1, j+1)`: Represents a match or a substitution.
    -   **Horizontal move** `(i, j) -> (i+1, j)`: Represents deleting a character from `string1`.
    -   **Vertical move** `(i, j) -> (i, j+1)`: Represents inserting a character into `string1`.
-   **Solution**: The problem is to find the shortest path from `(0, 0)` to `(m, n)`. The implementation uses A* search (which behaves like Dijkstra's algorithm in this case) with a priority queue to always explore the most promising path first.

### 2. Dynamic Programming (`dp_solver.py`)

This is the canonical and more efficient approach for solving the edit distance problem (related to the Levenshtein distance).

-   **Model**: A DP table `D` of size `(m+1) x (n+1)` is created, where `D[i][j]` stores the minimum cost to align the prefix `string1[:i]` with `string2[:j]`.
-   **Recurrence Relation**: The value of `D[i][j]` is calculated based on the outcomes of three possible operations:
    ```
    cost_sub = D[i-1][j-1] + cost(string1[i], string2[j])
    cost_del = D[i-1][j] + cost_of_deletion
    cost_ins = D[i][j-1] + cost_of_insertion

    D[i][j] = min(cost_sub, cost_del, cost_ins)
    ```
-   **Solution**: The final minimum cost is found at `D[m][n]`. The optimal alignment is then reconstructed by backtracking from this final cell to `D[0][0]`.

## Project Structure

```
string-alignment-solver/
├── README.md                 # This file
├── main.py                   # Main user interface and script entry point
├── shortest_path_solver.py   # A* search-based solver
└── dp_solver.py              # Dynamic Programming solver
```

## How to Run

1.  Make sure you have Python 3 installed.
2.  Place all three `.py` files (`main.py`, `shortest_path_solver.py`, `dp_solver.py`) in the same directory.
3.  Run the main script from your terminal:
    ```bash
    python main.py
    ```
4.  The script will prompt you to enter two strings.
5.  After entering the strings, you will be asked to choose which algorithm to use for the calculation.

### Example Session

```
$ python main.py
--- String Alignment & Edit Distance Calculator ---
Enter the first string: intention
Enter the second string: execution

Please choose an algorithm to solve:
  1. Shortest Path (A* Search)
  2. Dynamic Programming (Classic Edit Distance)
  3. Exit
Enter your choice (1, 2, or 3): 2

========================================
Algorithm: Dynamic Programming
========================================
The minimum alignment cost is: 8
Optimal Alignment:
  String 1: -INTENTION
  String 2: EXECUTION-
========================================
```
