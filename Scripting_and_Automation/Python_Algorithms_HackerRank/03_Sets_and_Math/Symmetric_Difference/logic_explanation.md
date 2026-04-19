# Challenge: Symmetric Difference
## Problem Description
The goal is to find the symmetric difference between two sets of integers. The symmetric difference consists of values that exist in either set M or set N, but not in both. The final output must be displayed in ascending order.

## Logic & Approach
This solution leverages the fundamental properties of Sets in Python, which are unordered collections of unique elements:

1. **Set Creation:** Input strings are split and mapped to integers before being converted into set objects to ensure uniqueness.

2. **Difference Calculation:** I used the .difference() method to find elements unique to each set.

3. **Union and Sorting:** By performing a .union() on the two differences, I gathered all unique non-overlapping values. Finally, the sorted() function ensures the output meets the ascending order requirement.

## Complexity Analysis
* **Time Complexity: O(LlogL)** - Where L is the number of elements in the final symmetric difference (due to the sorting step).

* **Space Complexity: O(M+N)** - We store the unique elements of both input sets in memory.

## Cybersecurity Perspective
In cybersecurity, set operations are vital for Indicator of Compromise (IOC) Analysis. Analysts use symmetric difference to compare logs from two different timeframes or environments to quickly isolate unique suspicious activities, such as new IP addresses or file hashes, while filtering out known baseline "noise" present in both datasets.


**Solved on:** 2026-04-19

*Link to challenge: HackerRank* - [Symmetric Difference](https://www.hackerrank.com/challenges/symmetric-difference/problem)