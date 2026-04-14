# HackerRank Challenge: Text Wrap
# Category: Strings
# Difficulty: Easy

def wrap(string: str, max_width: int) -> str:
    """
    Wraps a long string into a paragraph with a specified maximum width.
    
    Args:
        string: The input string to be wrapped.
        max_width: The maximum number of characters per line.
        
    Returns:
        A single string with newline characters inserted at the wrap points.
    """
    length = len(string)
    result = ""
    
    # Iterate through the string using a step equal to max_width
    for i in range(0, length, max_width):
        # Slice the string from current index to index + max_width
        # and append a newline character
        result += string[i : i + max_width] + "\n"
        
    return result

if __name__ == '__main__':
    try:
        # Reading the string and the maximum width
        user_string = input()
        user_width = int(input())
        
        # Execute and print result
        print(wrap(user_string, user_width))
            
    except (EOFError, ValueError):
        pass

"""
input:
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
"""