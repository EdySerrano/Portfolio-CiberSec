# Challenge: Lists
## Problem Description
The task is to initialize an empty list and perform a series of n commands provided as strings. These commands include standard list operations such as insert, append, remove, sort, pop, reverse, and print. The goal is to maintain the state of the list through these sequential operations.

## Logic & Approach
I implemented a command-driven logic to interact with Python’s built-in list methods:

1. **Command Parsing:** I used input().split() to tokenize each line into an "action" and its corresponding "arguments."

2. **Dispatcher Pattern:** Using a series of conditional statements (if-elif), the script identifies the action and maps it to the appropriate method (e.g., list.insert(i, e) or list.sort()).

3. **Dynamic Type Conversion:** Since input is read as strings, I ensured that arguments used for indexing and mathematical values were converted to int before being processed by the list methods.

## Complexity Analysis
The performance depends on the specific command being executed:

* **Time Complexity: O(n⋅m)** - where n is the number of commands and m is the complexity of the specific list operation. For example, sort() is O(LlogL) and insert() is O(L), where L is the current length of the list.

* **Space Complexity: O(L)** - We store L elements in memory, representing the current state of the list.

## Cybersecurity Perspective
How does this apply to my career in Security?

This challenge simulates Command Parsing and Input Validation, which are critical in building secure Command Line Interfaces (CLI) or APIs. In a security context, allowing a user to provide "commands" as strings is a potential vector for Command Injection. A robust implementation must strictly validate that the input matches an allowed list of actions (an "allowlist") and that the arguments are of the expected type and range. This prevents unauthorized memory access or logic errors that could lead to a Denial of Service (DoS).

**Solved on:** 2026-04-07

*Link to challenge: HackerRank* - [Lists](https://www.hackerrank.com/challenges/python-lists/problem)