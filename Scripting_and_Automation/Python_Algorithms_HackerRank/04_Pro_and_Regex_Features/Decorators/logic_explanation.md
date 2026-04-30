# Challenge: Standardize Mobile Number Using Decorators
## Problem Description
The task is to take a list of mobile numbers with varying prefixes (0, 91, +91, or none) and format them into a uniform standard: `+91 xxxxx xxxxx`. Once standardized, the numbers must be sorted in ascending order and printed.

## Logic & Approach
To solve this, I used a **Python Decorator** to separate the formatting logic from the sorting logic:

1. **The Decorator (`wrapper`):** This higher-order function takes the `sort_phone` function as an argument. Inside its inner function (`fun`), it iterates through the raw input list.

2. **String Slicing:** To handle different prefixes, I used negative slicing `[-10:]` to grab only the actual phone digits.

3. **Standardization:** I reconstructed the strings using the `+91` prefix and sliced the 10 digits into two groups of five.

4. **Final Execution:** The decorated function sorts the now-uniform strings, ensuring they are ordered correctly before printing.

## Complexity Analysis
* **Time Complexity: O(nlogn)** - While formatting is O(n), the final sorting of the list takes nlogn time.

* **Space Complexity: O(n)** - We maintain a list of n formatted strings in memory.

## Cybersecurity Perspective
This challenge demonstrates Data Sanitization and Normalization. In security, decorators are used to wrap functions with input-validation logic, ensuring data is in a safe, expected format before processing to prevent injection attacks or logic errors.


**Solved on:** 2026-04-30

*Link to challenge: HackerRank* - [Standardize Mobile Number Using Decorators](https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem)