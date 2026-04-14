# Challenge: String Formatting
## Problem Description
The objective is to print a formatted table showing the decimal, octal, hexadecimal, and binary values for each integer from 1 to a given number n. A key requirement is that each column must be space-padded to match the width of the binary representation of n.

## Logic & Approach
To solve this formatting challenge, I focused on dynamic width calculation and string methods:

1. **Width Determination:** First, I found the maximum width needed by checking the length of the binary string of n. Since Python's `bin()` function includes a `0b` prefix, I used slicing (`[2:]`) to get only the numeric part.

2. **Base Conversion:** Inside a loop from 1 to n, I used the built-in functions `oct()`, `hex()`, and `bin()`.

3. **String Cleaning:** These built-in functions return prefixes (`0o`, `0x`, `0b`). I cut these using slicing and converted the hexadecimal characters to uppercase using `.upper()`.

4. **Justification:** I utilized the `.rjust(width)` method on each string. This ensures that all columns align to the right, creating a clean, readable table regardless of the number of digits.

## Complexity Analysis
* **Time Complexity: O(n)** - The algorithm iterates once through all numbers up to n.

* **Space Complexity: O(1)** - We only store a few string variables at a time during each iteration.

## Cybersecurity Perspective
How does this apply to my career in Security?

When analyzing a malicious binary or a network packet capture (PCAP), data is rarely presented in decimal. Security professionals must constantly switch between Hexadecimal (for memory addresses and shellcode), Binary (for bitwise operations and flag analysis), and Octal (often used in Unix file permissions). Writing scripts that can clean and format these different representations is the first step toward automating reverse engineering tasks.

**Solved on:** 2026-04-13

*Link to challenge: HackerRank* - [String Formatting](https://www.hackerrank.com/challenges/python-string-formatting/problem)