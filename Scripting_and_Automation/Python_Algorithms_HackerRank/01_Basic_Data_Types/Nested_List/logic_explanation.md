# Challenge: Nested Lists
##  Problem Description
The task involves processing a class of N students to find those who share the second lowest grade. If multiple students have the same second lowest grade, their names must be printed in alphabetical order, each on a new line.

## Logic & Approach
To solve this problem, I implemented a workflow that manages both numerical filtering and string sorting:

* **Data Collection:** I stored student data in a nested list format: [[name, score], ...].

* **Identifying the Target Grade:** I used a list comprehension to extract all scores, converted them to a set to remove duplicates, and then sorted them. This allowed me to reliably identify the second lowest unique score at index [1].

* **Filtering & Sorting:** I used another list comprehension to find all names associated with that specific grade. Finally, I applied the .sort() method to ensure the output met the lexicographical requirement.

## Complexity Analysis
Efficiently handling nested structures is key for performance:

* **Time Complexity: O(nlogn)** - Primarily due to the sorting of scores and the final sorting of names.

* **Space Complexity: O(n)** - We store the input records and a list of unique scores, both proportional to the number of students.

# Cybersecurity Perspective
How does this apply to my career in Security?

This logic is directly applicable to Vulnerability Management. In a large-scale environment, vulnerabilities are often assigned scores (like CVSS). A security analyst might need to filter out the "Low" (lowest) severity noise to focus on the "Medium" (second lowest/next tier) vulnerabilities that meet specific criteria. Being able to programmatically group, filter, and sort these threats allows for more organized incident response and patch management.

Solved on: 2026-04-05

*Link to challenge: HackerRank* - [Nested Lists](https://www.hackerrank.com/challenges/nested-list)