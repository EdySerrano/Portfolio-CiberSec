# HackerRank Challenge: Finding the percentage
# Category: Basic Data Types
# Difficulty: Easy

def solve_challenge(student_marks: dict[str, list[float]], query_name: str) -> str:
    """
    Calculates the average score for a specific student and returns it
    formatted to two decimal places.
    
    Args:
        student_marks: A dictionary where keys are names and values are lists of scores.
        query_name: The name of the student to look up.
        
    Returns:
        A string representing the average score formatted to .2f.
    """
    # Step 1: Retrieve the list of scores using the query_name as the key
    scores = student_marks[query_name]
    
    # Step 2: Calculate the average (Sum of elements / Total count)
    average = sum(scores) / len(scores)
    
    # Step 3: Format the result to exactly 2 decimal places using an f-string
    return f"{average:.2f}"

if __name__ == '__main__':
    try:
        n = int(input())
        student_marks = {}
        for _ in range(n):
            # Using iterable unpacking to separate the name from the list of scores
            name, *line = input().split()
            scores = list(map(float, line))
            student_marks[name] = scores
            
        query_name = input()
        
        # Execute and print result
        print(solve_challenge(student_marks, query_name))
            
    except (EOFError, KeyError):
        pass

# input
"""
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika
"""