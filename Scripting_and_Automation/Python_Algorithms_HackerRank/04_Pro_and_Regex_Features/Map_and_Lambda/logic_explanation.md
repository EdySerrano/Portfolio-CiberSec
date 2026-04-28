# Challenge: Map and Lambda Function
## Problem Description
The task is to generate the first n numbers of the Fibonacci sequence (starting with 0) and then use the `map()` function alongside a `lambda` expression to compute the cube of each number in that sequence.

## Logic & Approach
I utilized a functional programming approach to handle data transformation efficiently:

1. **Sequence Generation:** I implemented an iterative function using tuple unpacking (`a, b = b, a + b`) to generate the Fibonacci numbers. This is more memory-efficient than recursion for this specific task.

2. **Lambda Expression:** Instead of defining a full function for a simple power operation, I used `lambda x: x3`, which provides a concise way to define one-line anonymous functions.

3. **Functional Mapping:** I used `map()` to apply the cubing logic to the entire list. This separates the generation of data from the transformation of data, making the code more modular.

## Complexity Analysis
* **Time Complexity: O(n)** - We iterate n times to generate the sequence and then once more (internally in map) to apply the cubing logic.

* **Space Complexity: O(n)** - We store n elements in the resulting list.

## Cybersecurity Perspective
Functional programming techniques like map and lambda are essential for Data Normalization. In security, this is used to rapidly transform raw event data (like converting timestamps or hashing strings) across massive datasets before they are ingested into a SIEM (Security Information and Event Management) system.


**Solved on:** 2026-04-28

*Link to challenge: HackerRank* - [Map and Lambda Function](https://www.hackerrank.com/challenges/map-and-lambda-expression/problem)