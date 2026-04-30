# HackerRank Challenge: Standardize Mobile Number Using Decorators
# Category: Closures and Decorators
# Difficulty: Easy

def wrapper(f):
    """
    A decorator that standardizes mobile numbers to the format: 
    +91 xxxxx xxxxx before passing them to the sorting function.
    """
    def fun(l):
        standardized = []
        for num in l:
            # Extract only the last 10 digits to handle any prefix (0, 91, +91)
            clean_num = num[-10:]
            
            # Format the number with the standard +91 prefix and required spacing
            formatted_num = f"+91 {clean_num[:5]} {clean_num[5:]}"
            standardized.append(formatted_num)
        
        # Step 3: Pass the standardized list to the original function (f)
        return f(standardized)
    return fun

@wrapper
def sort_phone(l):
    """
    Sorts a list of standardized phone numbers and prints them line by line.
    """
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    try:
        # Reading N numbers from input
        n = int(input())
        phone_numbers = [input() for _ in range(n)]
        
        sort_phone(phone_numbers)
            
    except (EOFError, ValueError):
        pass

    """
    Sample Input:
    3
    07895462130
    919875641230
    9195969878
   
    Sample Output:
    +91 78954 62130
    +91 91959 69878
    +91 98756 41230
    """