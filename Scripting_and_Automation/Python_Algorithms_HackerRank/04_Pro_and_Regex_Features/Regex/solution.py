# HackerRank Challenge: Detect Floating Point Number
# Category: Regex and Parsing
# Difficulty: Easy

import re

def is_valid_float(s: str) -> bool:
    """
    Validates if a string represents a correct floating-point number 
    using Regular Expressions.
    
    Args:
        s: The string to validate.
        
    Returns:
        True if the string meets all float requirements, False otherwise.
    """
    # Pattern breakdown:
    # ^[+-]? : Starts with an optional '+' or '-'
    # \d*    : Zero or more digits before the decimal point
    # \.     : Exactly one literal dot
    # \d+    : At least one digit after the decimal point
    # $      : End of the string
    pattern = r'^[+-]?\d*\.\d+$'
    
    # re.match returns a match object if valid, None otherwise
    return bool(re.match(pattern, s))

if __name__ == '__main__':
    try:
        t = int(input())
        for _ in range(t):
            test_case = input()
            print(is_valid_float(test_case))
            
    except (EOFError, ValueError):  
        pass

    """
    Sample Input:
    4.0O0
    Sample Output:
    False
    """