# HackerRank Challenge: Encryption
# Category: Algorithms - Implementation
# Difficulty: Medium

import os
import math

def encryption(s: str) -> str:
    """
    Encrypts a text string using a grid-based transposition cipher scheme.
    
    Args:
        s: The original string containing lowercase letters and spaces.
        
    Returns:
        The encrypted string with space-separated column texts.
    """
    # Step 1: Remove all spaces from the text and find its length
    s_cleaned = s.replace(" ", "")
    n = len(s_cleaned)

    # Step 2: Determine grid dimensions using floor and ceil of the square root
    rows = math.floor(math.sqrt(n))
    cols = math.ceil(math.sqrt(n))

    # Step 3: Ensure the grid area is large enough to contain all characters
    if rows * cols < n:
        rows += 1

    # Step 4: Transpose the grid by reading columns natively using step slicing
    encrypted_words = []
    for c in range(cols):
        # Slice the string starting at column index 'c' up to 'n', stepping by 'cols'
        column_word = s_cleaned[c::cols]
        encrypted_words.append(column_word)

    # Step 5: Join the extracted columns with a space
    return " ".join(encrypted_words)
    
if __name__ == '__main__':
    try:
        output_path = os.environ.get('OUTPUT_PATH')
        s = input()

        result = encryption(s)

        if output_path:
            with open(output_path, 'w') as fptr:
                fptr.write(result + '\n')
        else:
            print(result)
            
    except (EOFError, ValueError):
        pass

"""
Sample Input:
have a nice day
Sample Output:
hce akd via ecy
"""