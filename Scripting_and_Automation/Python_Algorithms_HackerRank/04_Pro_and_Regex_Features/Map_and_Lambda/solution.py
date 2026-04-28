# HackerRank Challenge: Map and Lambda Function
# Category: Functional Programming
# Difficulty: Easy

# Defining a lambda function to calculate the cube of a number
cube = lambda x: x**3

def fibonacci(n: int) -> list[int]:
    """
    Generates a list of the first n Fibonacci numbers.
    
    Args:
        n: The number of Fibonacci elements to generate.
        
    Returns:
        A list containing the sequence starting from 0 and 1.
    """
    fib_sequence = []
    a, b = 0, 1
    
    for _ in range(n):
        fib_sequence.append(a)
        # Using tuple unpacking to update Fibonacci values
        a, b = b, a + b
        
    return fib_sequence

if __name__ == '__main__':
    try:
        n = int(input())
        
        # Using map() to apply the lambda 'cube' to each element in the sequence
        result = list(map(cube, fibonacci(n)))
        print(result)
            
    except (EOFError, ValueError):
        pass

    """
    Sample Input:
    5
    Sample Output:
    [0, 1, 1, 8, 27]
    """