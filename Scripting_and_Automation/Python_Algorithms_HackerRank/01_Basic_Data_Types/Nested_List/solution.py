# HackerRank Challenge: Nested Lists
# Category: Basic Data Types
# Difficulty: Easy

def solve_challenge(students: list[list]) -> list[str]:
    """
    Identifies the names of students who have the second lowest grade.
    
    Args:
        students: A nested list where each element is [name, score].
        
    Returns:
        A list of names sorted alphabetically.
    """
    # Step 1: Extract all scores and find unique values using a set
    scores = sorted(set([student[1] for student in students]))
    
    # Step 2: The second element in the sorted unique scores is the second lowest
    second_lowest_grade = scores[1]
    
    # Step 3: Filter names of students who match the second lowest grade
    result_names = [
        student[0] 
        for student in students 
        if student[1] == second_lowest_grade
    ]
    
    # Step 4: Sort names alphabetically as required by the challenge
    result_names.sort()
    
    return result_names

if __name__ == '__main__':
    try:
        student_data = []
        for _ in range(int(input())):
            name = input()
            score = float(input())
            student_data.append([name, score])
        
        # Execute logic and print results
        for name in solve_challenge(student_data):
            print(name)
            
    except (EOFError, IndexError):
        pass