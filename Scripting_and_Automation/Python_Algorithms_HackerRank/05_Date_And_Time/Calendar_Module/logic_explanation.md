# Challenge: Calendar Module

## Problem Description
Given a specific date containing a month, day, and year, the task is to determine which day of the week that date corresponds to and output the name of the day in full uppercase letters.

## Logic & Approach
To solve this cleanly, I used Python's built-in `calendar` module, which encapsulates complex leap year and calendar grid math:

1. **Input Parsing:** I mapped the single-line input containing space-separated characters directly into three integers representing `month`, `day`, and `year`.

2. **Index Retrieval:** I passed the inputs to `calendar.weekday(year, month, day)`. It is important to note that this function expects the arguments in `YYYY, MM, DD` order. It returns an integer index from `0` (Monday) to `6` (Sunday).

3. **String Mapping:** I used the `calendar.day_name` array container to automatically map the resulting index to its English name equivalent and applied `.upper()` to meet the formatting constraints.

## Complexity Analysis
* **Time Complexity: O(1)** - Calculating the day of the week uses Zeller's congruence or a similar mathematical algorithm internally, taking constant time.

* **Space Complexity: O(1)** - No dynamic or growing data structures are used.

## Cybersecurity Perspective
This challenge is a practical reminder of **Time-of-Check to Time-of-Use** principles and **Timestamp Analysis**. Understanding how systems natively translate timestamps to week structures allows analysts to correlate network logs with human physical schedules helping differentiate automated cron-job attacks (which run identically regardless of the day) from active, human-driven insider threats.

**Solved on:** 2026-05-26

*Link to challenge: HackerRank* - [Calendar Module](https://www.hackerrank.com/challenges/calendar-module/problem)