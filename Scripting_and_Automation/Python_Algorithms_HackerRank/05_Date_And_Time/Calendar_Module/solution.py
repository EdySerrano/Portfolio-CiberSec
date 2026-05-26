# HackerRank Challenge: Calendar Module
# Category: Date and Time
# Difficulty: Easy

import calendar

def get_day_of_week(month: int, day: int, year: int) -> str:
    """
    Finds the day of the week for a given date and returns it in uppercase.
    
    Args:
        month: The month component of the date.
        day: The day component of the date.
        year: The year component of the date.
        
    Returns:
        The name of the day in uppercase (e.g., 'WEDNESDAY').
    """
    # Step 1: Get the day index (0 = Monday, 6 = Sunday) using calendar.weekday()
    day_index = calendar.weekday(year, month, day)
    
    # Step 2: Retrieve the day name from calendar.day_name and convert to uppercase
    return calendar.day_name[day_index].upper()

if __name__ == '__main__':
    try:
        # Input format: MM DD YYYY
        m, d, y = map(int, input().split())
        
        # Execute logic and print the uppercase day name
        print(get_day_of_week(m, d, y))
            
    except (EOFError, ValueError, IndexError):
        pass

    """
    Sample Input:
    08 05 2015
    Sample Output:
    WEDNESDAY"""