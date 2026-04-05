# Challenge: Find the Runner-Up Score!
## Problem Description
The objective is to find the "runner-up" (second highest) score from a sheet of n participants. Since multiple participants can share the same top score, we must ensure we identify the second-highest unique value.

## Logic & Approach
To solve this efficiently, I followed a three-step process:

1. **Duplicate Removal:** I converted the input array into a set. This is a critical step because if the highest score appears multiple times (e.g., [6, 6, 5]), simply sorting and picking the second element would incorrectly return 6 instead of 5.

2. **Sorting:** I converted the unique elements back into a list and applied Python’s sort() method (Timsort), which organizes the values in ascending order.

3. **Negative Indexing:** By using the index [-2], I directly accessed the second-to-last element of the sorted list, which represents the runner-up.

## Complexity Analysis
This approach balances readability with performance:

* **Time Complexity: O(nlogn)** - Sorting the unique elements is the most computationally expensive part of the process.

* **Space Complexity: O(n)** - We create a temporary set and a new list to store the unique scores.

## Cybersecurity Perspective
How does this apply to my career in Security?

Identifying the "Runner-Up" is a common task in Threat Hunting and Log Analysis. When reviewing firewall logs or authentication attempts, the "Top" activity is often known noise (like a common system heartbeat). Security analysts must frequently filter out these unique "Top 1" noise patterns to investigate the "Top 2" or "Top 3" most frequent events, which are more likely to represent lateral movement or stealthy exfiltration attempts.

**Solved on:** 2026-04-05

*Link to challenge: HackerRank* - [Find the Runner-Up Score!](https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem)