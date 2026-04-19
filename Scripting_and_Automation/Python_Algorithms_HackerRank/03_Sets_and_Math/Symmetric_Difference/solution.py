# HackerRank Challenge: Symmetric Difference
# Category: Sets
# Difficulty: Easy

def get_symmetric_difference(set_a: set[int], set_b: set[int]) -> list[int]:
    """
    Calculates the symmetric difference between two sets.
    
    Args:
        set_a: The first set of integers.
        set_b: The second set of integers.
        
    Returns:
        A sorted list of integers present in either set but not both.
    """
    # Mathematical definition: (A - B) union (B - A)
    diff_a = set_a.difference(set_b)
    diff_b = set_b.difference(set_a)
    
    # Combine differences and sort the result
    return sorted(diff_a.union(diff_b))

if __name__ == '__main__':
    try:
        # Input handling for Set M
        m_size = int(input())
        m_set = set(map(int, input().split()))
        
        # Input handling for Set N
        n_size = int(input())
        n_set = set(map(int, input().split()))
        
        # Calculate and display results line by line
        for value in get_symmetric_difference(m_set, n_set):
            print(value)
            
    except (EOFError, ValueError):
        pass

"""
sample input:
4
2 4 5 9
4
2 4 11 12
sample output:
5
9
11
12
"""