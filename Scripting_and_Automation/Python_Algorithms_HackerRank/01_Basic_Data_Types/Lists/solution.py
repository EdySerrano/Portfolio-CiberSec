# HackerRank Challenge: Lists
# Category: Basic Data Types
# Difficulty: Easy

def execute_commands(commands: list[list[str]]) -> None:
    """
    Parses and executes a series of list operations based on string commands.
    
    Args:
        commands: A list of commands where each command is a list of strings 
                  containing the operation name and its arguments.
    """
    result_list = []

    for command in commands:
        action = command[0]
        
        if action == "insert":
            result_list.insert(int(command[1]), int(command[2]))
        elif action == "print":
            print(result_list)
        elif action == "remove":
            result_list.remove(int(command[1]))
        elif action == "append":
            result_list.append(int(command[1]))
        elif action == "sort":
            result_list.sort()
        elif action == "pop":
            result_list.pop()
        elif action == "reverse":
            result_list.reverse()

if __name__ == '__main__':
    try:
        n = int(input())
        all_commands = []
        for _ in range(n):
            all_commands.append(input().split())
        
        execute_commands(all_commands)
            
    except (EOFError, ValueError, IndexError):
        pass

"""
input:
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
"""