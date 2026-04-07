# Challenge: Finding the percentage
## Problem Description
This challenge requires storing a record of student names and their corresponding grades in a dictionary. Given a specific student's name, the goal is to calculate the average of their grades and print the result with exactly two decimal places.

## Logic & Approach
To solve this efficiently, I utilized Python’s built-in data structures and formatting tools:

1. **Dictionary Mapping:** I stored the data in a dictionary (student_marks), where the student's name acts as a unique key. This allows for O(1) (constant time) retrieval of marks.

2. **Iterable Unpacking:** I used the *line syntax to dynamically handle the input, separating the name from an arbitrary number of scores.

3. **Arithmetic Mean:** The average was calculated using the formula $\frac{\sum \text{scores}}{n}$.

4. **Precision Formatting:** Since the output requires specific precision (e.g., 56.00 instead of 56.0), I used Python’s f-string formatting (:.2f) to ensure the output always displays two decimal points.

## Complexity Analysis
Understanding the performance of dictionary-based lookups is essential:

* **Time Complexity: O(n)** - We iterate through n students to build the dictionary. However, the final lookup and average calculation are O(1) and O(k) respectively (where k is the number of marks, usually a small constant).

* **Space Complexity: O(n)** - The dictionary scales linearly with the number of students stored in the system.

## Cybersecurity Perspective
How does this apply to my career in Security?

This problem highlights the importance of Data Integrity and Precision Formatting. In security automation, we often parse logs where a "Key" (like a UserID or IP address) is associated with multiple "Values" (like login timestamps or failed attempts). Furthermore, when generating Security Metrics Reports, ensuring numerical precision is vital; presenting an average "Time to Remediate" (TTR) with consistent decimal formatting ensures that automated parsing tools and human auditors receive standardized, professional-grade data.

**Solved on:** 2026-04-06

*Link to challenge: HackerRank* - [Finding the percentage](https://www.hackerrank.com/challenges/finding-the-percentage/problem)

