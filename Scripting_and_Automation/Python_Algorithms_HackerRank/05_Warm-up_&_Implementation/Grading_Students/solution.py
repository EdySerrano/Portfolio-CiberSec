# HackerRank Challenge: Grading Students
# Category: Algorithms - Implementation
# Difficulty: Easy

import os

def gradingStudents(grades: list[int]) -> list[int]:
    """
    Automates the university rounding policy for student grades.
    
    Args:
        grades: Array of integers representing the grades before rounding.
        
    Returns:
        Array of integers representing the rounded grades.
    """
    result = []
    
    for grade in grades:
        # Rule 1: Failing grade below 38 receives no rounding
        if grade < 38:
            result.append(grade)
        # Rule 2: Grade is 38 or higher and eligible for potential rounding
        else:
            # Find the next multiple of 5 using floor division
            next_multiple_of_five = ((grade // 5) + 1) * 5
            
            # If the difference is less than 3, round up
            if next_multiple_of_five - grade < 3:
                result.append(next_multiple_of_five)
            # Otherwise, keep the original grade
            else:
                result.append(grade)
    
    return result

if __name__ == '__main__':
    try:
        output_path = os.environ.get('OUTPUT_PATH')
        grades_count = int(input().strip())

        grades = [int(input().strip()) for _ in range(grades_count)]
        result = gradingStudents(grades)

        if output_path:
            with open(output_path, 'w') as fptr:
                fptr.write('\n'.join(map(str, result)) + '\n')
        else:
            print('\n'.join(map(str, result)))
            
    except (EOFError, ValueError):
        pass

"""
Sample Input:
4
73
67
38
33
Sample Output:
75
67
40
33
"""