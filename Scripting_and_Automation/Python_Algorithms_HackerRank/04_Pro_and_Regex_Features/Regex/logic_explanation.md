# Challenge: Detect Floating Point Number

## Problem Description
The goal is to verify if a given string is a valid floating-point number based on specific rules: it can start with a sign (+ or -), it must contain exactly one decimal point, and it must have at least one decimal value following that point.

## Logic & Approach
To solve this challenge efficiently, I utilized **Regular Expressions (Regex)** to define a strict structural pattern for the input strings:

1. **Sign Handling:** I used `^[+-]?` to account for an optional positive or negative sign at the very beginning of the string.

2. **The Integer Part:** The expression `\d*` allows for zero or more digits before the decimal point, covering cases like `.5` or `-.7`.

3. **The Decimal Requirement:** I used `\.` to require exactly one dot, followed by `\d+` to ensure that there is at least one digit afterward, satisfying the "at least one decimal value" rule.

4. **Boundary Anchors:** By using `^` and `$`, I ensured the regex validates the entire string from start to finish, preventing partial matches.

## Complexity Analysis
* **Time Complexity: O(T * N)** - Where T is the number of test cases and N is the length of each string, as the regex engine scans the string once.

* **Space Complexity: O(1)** - We only store the pattern and a few variables regardless of the input size.

## Cybersecurity Perspective
This challenge is a practical exercise in Input Validation. In a security context, failing to properly validate numerical inputs can lead to logic vulnerabilities, such as "Type Confusion" or "Buffer Overflows" in lower-level languages. Using strict Regex patterns ensures that only sanitized, expected data formats are processed by the application's core logic.

**Solved on:** 2026-05-01

*Link to challenge: HackerRank* - [Detect Floating Point Number](https://www.hackerrank.com/challenges/introduction-to-regex/problem)