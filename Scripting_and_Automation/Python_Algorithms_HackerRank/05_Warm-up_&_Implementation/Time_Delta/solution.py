# HackerRank Challenge: Time Delta
# Category: Date and Time
# Difficulty: Medium

import os
from datetime import datetime

def time_delta(t1: str, t2: str) -> str:
    """
    Calculates the absolute difference in seconds between two timestamps
    that include time zone offsets.
    
    Args:
        t1: The first timestamp string.
        t2: The second timestamp string.
        
    Returns:
        The absolute difference represented as a string containing an integer.
    """
    # Step 1: Define the formatting tokens matching 'Day dd Mon yyyy hh:mm:ss +xxxx'
    # %a: Abbreviated weekday name
    # %d: Day of the month
    # %b: Abbreviated month name
    # %Y: Year with century
    # %H:%M:%S: Hour, minute, and second (24-hour clock)
    # %z: UTC offset in the form +HHMM or -HHMM
    format_string = "%a %d %b %Y %H:%M:%S %z"
    
    # Step 2: Parse both strings into timezone-aware datetime objects
    date1 = datetime.strptime(t1, format_string)
    date2 = datetime.strptime(t2, format_string)
    
    # Step 3: Compute the delta, calculate total seconds, and apply absolute value
    diff = abs(int((date1 - date2).total_seconds()))
    
    return str(diff)

if __name__ == '__main__':
    try:
        # Check if running within the HackerRank platform environment
        output_path = os.environ.get('OUTPUT_PATH')
        
        t = int(input())
        results = []
        
        for _ in range(t):
            t1 = input()
            t2 = input()
            results.append(time_delta(t1, t2))
            
        if output_path:
            with open(output_path, 'w') as fptr:
                fptr.write('\n'.join(results) + '\n')
        else:
            print('\n'.join(results))
            
    except (EOFError, ValueError):
        pass

"""
Sample Input:
2
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 -0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000
    
Sample Output:
25200
88200
"""