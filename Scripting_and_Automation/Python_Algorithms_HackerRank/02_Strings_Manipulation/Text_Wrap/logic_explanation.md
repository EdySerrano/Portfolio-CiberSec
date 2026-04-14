# Challenge: Text Wrap
## Problem Description
The goal is to take a long string and wrap it into a paragraph of a fixed width w. Each line of the resulting paragraph, except possibly the last one, must contain exactly w characters.

## Logic & Approach
To solve this problem without relying entirely on external libraries, I implemented a manual slicing approach:

1. **Stepped Iteration:** I used a `for` loop with a "step" argument in the `range()` function. By setting the step to `max_width`, the loop index jumps directly to the start of each new line.

2. **String Slicing:** Inside the loop, I utilized Python’s slicing feature `string[start:end]` to extract a chunk of the string of the required length.

3. **Concatenation:** I appended each slice to a result string, followed by a newline character `(\n)`. This transforms a single continuous string into a vertically formatted block of text.

## Complexity Analysis
* **Time Complexity: O(n)** - The algorithm processes each character of the string once during the slicing and concatenation process.

* **Space Complexity: O(n)** - A new string is created to store the formatted output, which is proportional to the size of the input.

## Cybersecurity Perspective
How does this apply to my career in Security?

Text wrapping is a fundamental aspect of Log Normalization and Report Generation. In a Security Operations Center (SOC), raw data from network sensors or syslogs can be incredibly long and difficult to read. Automating the formatting of these strings into readable paragraphs is essential for human analysts to quickly spot anomalies.

**Solved on:** 2026-04-14

*Link to challenge: HackerRank* - [Text Wrap](https://www.hackerrank.com/challenges/text-wrap/problem)