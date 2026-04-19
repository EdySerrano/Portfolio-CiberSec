
# Challenge: itertools.product()
## Problem Description
The task is to compute the Cartesian Product `(A×B)` of two provided lists. The output must consist of all possible pairs `(a,b)` where `a ∈ A` and `b ∈ B`, printed as space-separated tuples in sorted order.

## Logic & Approach
Instead of manual nested loops, I used Python's itertools library:

1. **Itertools Utility:** The `product()` function lazily generates the Cartesian product, which is memory-efficient for large datasets.

2. **Unpacking for Output:** To meet the specific output format (tuples separated by spaces), I used the asterisk operator `(*)` in the `print()` function. This unpacks the generator directly into the function arguments, automatically applying the default space separator.

## Complexity Analysis
* **Time Complexity: O(n×m)** - Where n and m are the lengths of lists A and B respectively, as every combination must be generated.

* **Space Complexity: O(1)** - Since `itertools.product` returns an iterator, it does not store the entire product in memory unless converted to a list.

## Cybersecurity Perspective
`itertools.product` is a standard tool for Brute-Force and Fuzzing scripts. It is used to generate exhaustive combinations of characters for password cracking or to test all possible parameter combinations in a web form to identify injection vulnerabilities.


**Solved on:** 2026-04-19

*Link to challenge: HackerRank* - [HackerRank - itertools.product()](https://www.hackerrank.com/challenges/itertools-product/problem)