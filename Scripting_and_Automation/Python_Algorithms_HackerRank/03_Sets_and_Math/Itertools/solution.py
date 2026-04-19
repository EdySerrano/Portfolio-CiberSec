# HackerRank Challenge: itertools.product()
# Category: Itertools
# Difficulty: Easy

from itertools import product

def solve_cartesian_product(list_a: list[int], list_b: list[int]) -> None:
    """
    Computes the Cartesian product of two lists and prints the resulting 
    tuples separated by spaces.
    
    Args:
        list_a: First list of integers.
        list_b: Second list of integers.
    """
    # Step 1: Compute the Cartesian product using itertools.product.
    # This is equivalent to nested for-loops but more efficient.
    result = product(list_a, list_b)
    
    # Step 2: Use the unpacking operator (*) to print the result 
    # as space-separated tuples.
    print(*result)

if __name__ == '__main__':
    try:
        # Reading two lines of space-separated integers
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        
        solve_cartesian_product(a, b)
            
    except (EOFError, ValueError):
        pass

    """
    Sample Input:
    1 2
    3 4
    Sample Output:
    (1, 3) (1, 4) (2, 3) (2, 4)
    """