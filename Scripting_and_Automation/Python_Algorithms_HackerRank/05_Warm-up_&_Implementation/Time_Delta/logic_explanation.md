# Challenge: Time Delta

## Problem Description
The challenge requires calculating the absolute difference in seconds between two social media post timestamps. The timestamps include time zone offsets and follow the structured format: `Day dd Mon yyyy hh:mm:ss +xxxx`.

## Logic & Approach
To accurately calculate the difference between distinct time zones without manual offset arithmetic, I utilized Python's native `datetime` module:

1. **Format Blueprinting:** I mapped out the format string using standard strptime tokens: `%a %d %b %Y %H:%M:%S %z`. The inclusion of the `%z` directive is crucial because it natively parses the UTC offset (like `-0700` or `+0530`).

2. **Timezone-Aware Parsing:** Passing the tokens into `datetime.strptime()` generates timezone-aware object instances. When Python performs subtraction on two timezone-aware objects, it automatically normalizes both to UTC before computing the delta.

3. **Delta Extraction:** Subtraction yields a `timedelta` object. Calling the `.total_seconds()` method provides the exact float representation of the gap, which is then cast to an integer and forced to a positive value via `abs()`.

## Complexity Analysis
* **Time Complexity: O(T)** - Where T represents the number of test cases. Each individual timestamp parsing and subtraction takes O(1) constant time.

* **Space Complexity: O(1)** - The memory consumption remains stable as we only store the input strings and the resulting delta during processing iterations.

## Cybersecurity Perspective
This challenge highlights a vital aspect of **Log Analysis and Incident Response**. During a forensic investigation, an analyst must piece together a **Timeline of Events** by correlating logs from distributed assets worldwide (e.g., firewalls in the US, authentication servers in Europe, and endpoints in Asia). If the timestamps are not parsed with correct timezone awareness (`%z`), the sequencing of an attack chain could be misread entirely, leading to wrong conclusions about the root cause or the initial vector of entry.

**Solved on:** 2026-05-27

*Link to challenge: HackerRank* - [Time Delta](https://www.hackerrank.com/challenges/python-time-delta/problem)