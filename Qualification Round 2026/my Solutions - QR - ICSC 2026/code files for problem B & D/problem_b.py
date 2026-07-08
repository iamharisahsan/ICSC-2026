def generate_shape(n: int, shape: str) -> list[list[int]]:

    """
    Generates specific geometric patterns on an N x N grid.
    
    Parameters:
    n (int): The grid size (5 <= n <= 51, always odd for the diamond).
    shape (str): Either "checkerboard" or "diamond".
    
    Returns:
    list[list[int]]: A 2D list representing the grid filled with 0s and 1s.
    """

    grid = [[0 for _ in range(n)] for _ in range(n)]
    
    if shape == "checkerboard":
        for r in range(n):
            for c in range(n):
                if (r + c) % 2 != 0:
                    grid[r][c] = 1
                    
    elif shape == "diamond":
        center = n // 2
        for r in range(n):
            for c in range(n):
                
                if abs(r - center) + abs(c - center) <= center:
                    grid[r][c] = 1
                    
    return grid

def print_grid(grid: list[list[int]]):
    for row in grid:
        print(" ".join(map(str, row)))
