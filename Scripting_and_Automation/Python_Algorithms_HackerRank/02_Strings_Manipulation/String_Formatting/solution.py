# HackerRank Challenge: String Formatting
# Category: Strings
# Difficulty: Easy

def print_formatted(number: int) -> None:
    """
    Prints decimal, octal, hexadecimal, and binary representations 
    of numbers from 1 to 'number', right-justified based on the 
    width of the binary representation of the maximum value.
    
    Args:
        number: The maximum integer to reach in the sequence.
    """
    # Step 1: Calculate the width for padding based on the binary 
    # representation of the largest number.
    # bin(number) returns '0b...', so we slice from index 2.
    width = len(bin(number)[2:])
    
    for i in range(1, number + 1):
        # Step 2: Convert the integer to different bases and strip prefixes
        decimal = str(i)
        octal = oct(i)[2:]
        # Hexadecimal should be capitalized
        hexa = hex(i)[2:].upper()
        binary = bin(i)[2:]
        
        # Step 3: Print each value right-justified to 'width'
        print(decimal.rjust(width),
              octal.rjust(width),
              hexa.rjust(width),
              binary.rjust(width))

if __name__ == '__main__':
    try:
        n = int(input())
        print_formatted(n)
    except (EOFError, ValueError):
        pass


"""
input:
17
"""