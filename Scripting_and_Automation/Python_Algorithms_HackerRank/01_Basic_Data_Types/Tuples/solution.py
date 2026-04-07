# HackerRank Challenge: Tuples
# Category: Basic Data Types
# Difficulty: Easy

def solve_challenge(elements: list[int]) -> int:
    """
    Converts a list of integers into a tuple and computes its hash value.
    
    Args:
        elements: A list of integers provided by the input.
        
    Returns:
        The integer result of the hash function applied to the tuple.
    """
    # Step 1: Create an immutable tuple from the list of integers.
    # Tuples are hashable, whereas lists are not.
    t = tuple(elements)
    
    # Step 2: Compute and return the hash value.
    return hash(t)

if __name__ == '__main__':
    try:
        # Reading the number of elements (n) and the space-separated integers
        n = int(input())
        integer_list = map(int, input().split())
        
        # Execute logic and print the resulting hash
        result = solve_challenge(list(integer_list))
        print(result)
        
    except (EOFError, ValueError):
        pass

"""
input:
2
1 2
"""