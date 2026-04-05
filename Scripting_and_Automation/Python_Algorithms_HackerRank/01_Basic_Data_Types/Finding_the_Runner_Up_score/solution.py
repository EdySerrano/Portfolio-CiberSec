# HackerRank Challenge: Find the Runner-Up Score!
# Category: Basic Data Types
# Difficulty: Easy

def solve_challenge(scores: list[int]) -> int:
    """
    Identifies the second-highest unique score from a given list.
    
    Args:
        scores: A list of integers representing participant scores.
        
    Returns:
        The integer value of the runner-up score.
    """
    # Step 1: Remove duplicates by converting the list to a set.
    # Step 2: Convert back to a list and sort in ascending order.
    unique_scores = sorted(list(set(scores)))
    
    # Step 3: Access the second-to-last element using negative indexing.
    return unique_scores[-2]

if __name__ == '__main__':
    try:
        n = int(input())
        arr = map(int, input().split())
        
        # Convert map object to list for the function
        result = solve_challenge(list(arr))
        print(result)
        
    except (EOFError, IndexError):
        # Handling potential empty or single-element lists
        pass