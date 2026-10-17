# TASK411 — Finding the Snake in a Grid

You are given a two-dimensional array representing a grid containing a snake. The snake occupies connected cells represented by the following characters:

| Character | Meaning |
|---|---|
| `h` | Snake’s head |
| `<` | Body cell pointing to the previous cell on its left |
| `>` | Body cell pointing to the previous cell on its right |
| `v` | Body cell pointing to the previous cell below it |
| `^` | Body cell pointing to the previous cell above it |
| Space | Empty cell |

Each body cell’s arrow points toward the preceding cell along the path to the head. Therefore, when tracing from the head toward the tail, the next cell is an adjacent body cell whose arrow points to the current cell.

## Task

Write a program that locates the head and returns an ordered list of coordinates representing the entire snake, from the head to the final cell of its tail.

Use the coordinate format:

```text
[row, column]
```

Use zero-based indexing. The top-left cell is `[0, 0]`; rows increase downward, and columns increase to the right.

For example, `[3, 2]` identifies the cell in the fourth row and third column.

The program must work for arbitrary `M × N` array dimensions, where `M` is the number of rows and `N` is the number of columns. Do not rely on the examples’ sizes or positions.

## Input assumptions

Assume that the array is rectangular and contains exactly one valid snake:

- There is exactly one head, represented by `h`.
- All body cells belong to one continuous path connected to the head.
- Connections occur only between cells sharing an edge; diagonal connections are not allowed.
- Each body cell points to its predecessor toward the head.
- There are no branches, loops or disconnected body cells.
- There is exactly one tail endpoint.

Empty cells do not belong to the snake. Occupied cells may be adjacent without being consecutive along its path; use the arrows to determine the connections.

Input validation is not required. The matrix may be supplied directly as an array in the chosen programming language.

## Required result

Return every snake cell exactly once, starting at the head and following the path to the tail.

Represent every coordinate as `[row, column]`.

The tail is reached when no adjacent body cell points to the current cell.

## Example I

Input array:

```c
char a[4][4] = {
    {' ', 'v', '<', '<'},
    {'v', '<', ' ', '^'},
    {'>', '>', 'v', '^'},
    {' ', ' ', 'h', '^'}
};
```

The head is at `[3, 2]`.

Expected coordinate sequence:

```text
[[3, 2], [2, 2], [2, 1], [2, 0],
 [1, 0], [1, 1], [0, 1], [0, 2],
 [0, 3], [1, 3], [2, 3], [3, 3]]
```

## Example II

Input array:

```c
char a[4][4] = {
    {' ', ' ', ' ', ' '},
    {' ', ' ', 'h', '<'},
    {'>', '>', '>', '^'},
    {'^', '<', ' ', ' '}
};
```

The head is at `[1, 2]`.

Expected coordinate sequence:

```text
[[1, 2], [1, 3], [2, 3], [2, 2],
 [2, 1], [2, 0], [3, 0], [3, 1]]
```

## Submission

Submit:

- The program’s source code.
- The coordinate sequences produced for both examples.
- A brief explanation of how the algorithm uses the arrows to select the next cell and recognize the tail.

As an optional check, also test a rectangular grid and a snake whose head is on a boundary. Confirm that every snake cell appears exactly once and that all coordinates follow `[row, column]`.