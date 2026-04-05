# HackerRank Challenge: List Comprehensions
# Category: Basic Data Types
# Difficulty: Easy

def solve_challenge(x: int, y: int, z: int, n: int) -> list[list[int]]:
    """
    Generates a 3D grid of coordinates [i, j, k] where the sum 
    of the elements is not equal to a specific integer n.
    
    Args:
        x, y, z: Integers representing the dimensions of the cuboid.
        n: The integer sum threshold to exclude.
        
    Returns:
        A list of lists containing the valid coordinate permutations.
    """
    # Using a nested list comprehension to iterate through all possible 
    # values of i, j, and k within the given ranges, filtering out 
    # those where the sum equals n.
    coordinates = [
        [i, j, k] 
        for i in range(x + 1) 
        for j in range(y + 1) 
        for k in range(z + 1) 
        if i + j + k != n
    ]
    
    return coordinates

if __name__ == '__main__':
    try:
        # Reading dimensions and the exclusion integer n
        x = int(input())
        y = int(input())
        z = int(input())
        n = int(input())
        
        result = solve_challenge(x, y, z, n)
        print(result)
        
    except EOFError:
        pass