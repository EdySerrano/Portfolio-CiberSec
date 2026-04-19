# Challenge: Mutations
## Problem Description
In Python, strings are immutable, meaning they cannot be changed once created. Attempting to reassign a character at a specific index (e.g., `string[5] = 'k'`) results in a `TypeError`. This challenge requires implementing a workaround to "mutate" a string at a given index and return the modified version.

## Logic & Approach
To bypass string immutability, I utilized the Slicing and Concatenation method:

1. **Slicing the Prefix:** I extracted the portion of the string from the beginning up to (but not including) the target index: **string[:position]**.

2. **Inserting the Character:** I placed the new character immediately after the prefix.

3. **Slicing the Suffix:** I extracted the remainder of the string starting from the index immediately following the target: string[position+1:].

4. **Reconstruction:** By concatenating these three parts, Python creates a entirely new string object in memory that reflects the desired change.

## Complexity Analysis
* **Time Complexity: O(n)** - Python must copy the characters from the original string into a new memory location to create the new string.

* **Space Complexity: O(n)** - A new string of length n is allocated in memory to store the result.

## Cybersecurity Perspective
How does this apply to my career in Security?

Understanding memory immutability is vital for Binary Exploitation and Secure Coding. In low-level languages like C, strings are mutable, which often leads to Buffer Overflow vulnerabilities if not handled correctly. Python’s immutability is a security feature that prevents accidental data corruption in memory. From an offensive standpoint, string mutation logic is essential when Fuzzing or Crafting Payloads. For instance, when testing a Web Application Firewall (WAF), an analyst might take a known-good payload and programmatically mutate single characters to identify which specific patterns trigger a block or bypass.


**Solved on:** 2026-04-19

*Link to challenge: HackerRank* - [Mutations](https://www.hackerrank.com/challenges/python-mutations/problem)