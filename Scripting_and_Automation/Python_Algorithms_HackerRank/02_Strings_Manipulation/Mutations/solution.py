# HackerRank Challenge: Mutations
# Category: Strings
# Difficulty: Easy

def mutate_string(string: str, position: int, character: str) -> str:
    """
    Modifies a string at a specific index by using slicing and concatenation.
    
    Args:
        string: The original immutable string.
        position: The index where the change should occur.
        character: The new character to insert at the specified position.
        
    Returns:
        A new string containing the modification.
    """
    # Since strings are immutable in Python, we cannot perform item assignment.
    # We create a new string by joining the part before the index, 
    # the new character, and the part after the index.
    modified_string = string[:position] + character + string[position+1:]
    
    return modified_string

if __name__ == '__main__':
    try:
        s = input()
        i, c = input().split()
        
        # Call the mutation function and display the result
        s_new = mutate_string(s, int(i), c)
        print(s_new)
        
    except (EOFError, ValueError, IndexError):
        pass


"""
Sample Input:
    abracadabra
    5 k
Sample Output:
    abrackdabra
"""