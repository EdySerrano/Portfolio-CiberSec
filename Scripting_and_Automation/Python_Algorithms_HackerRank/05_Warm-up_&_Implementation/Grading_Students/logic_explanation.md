# Challenge: Grading Students

## Problem Description
HackerLand University automated its grading system based on specific rounding rules. Any grade below 40 is a failing grade. A professor rounds a student's grade up to the next multiple of 5 only if the difference between the grade and that next multiple is less than 3. However, if a grade is less than 38, no rounding occurs as the result would still be a failing grade.

## Logic & Approach
To automate this rounding policy, I iterated through the list of grades and applied conditional mathematical checks:

1. **Failure Boundary Exclusion:** The code checks if a grade is strictly less than 38. If true, the grade is directly appended to the results without modification, as it cannot be rounded up to a passing score.

2. **Next Multiple Calculation:** For grades 38 or higher, I calculated the next immediate multiple of 5 using integer floor division: `((grade // 5) + 1) * 5`.

3. **Delta Check and Reassignment:** I calculated the delta between this next multiple and the original grade. If the delta is less than 3 (i.e., 1 or 2 points away), the grade is rounded up to that multiple. Otherwise, the original grade is maintained.

## Complexity Analysis
* **Time Complexity: O(n)** - Where n is the number of student grades in the array. We loop through the list exactly once executing basic arithmetic comparisons.

* **Space Complexity: O(n)** - A new list of size n is allocated to store and return the modified or preserved student records.

## Cybersecurity Perspective
This challenge reflects principles of **Business Logic Validation and Integrity Control**. In educational platforms or enterprise payroll systems, modifying numeric variables based on automated thresholds is common. An application security analyst must ensure that calculations like rounding cannot be manipulated via integer overflows or negative inputs. Implementing strict conditional checks prevents attackers from exploiting flaw boundaries to artificially inflate scores, financial balances, or privilege levels.

**Solved on:** 2026-06-02

*Link to challenge: HackerRank* - [Grading Students](https://www.hackerrank.com/challenges/grading/problem)