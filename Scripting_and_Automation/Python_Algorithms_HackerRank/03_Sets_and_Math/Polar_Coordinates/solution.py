# HackerRank Challenge: Polar Coordinates
# Category: Math
# Difficulty: Easy

import cmath

def convert_to_polar(complex_str: str) -> tuple[float, float]:
    """
    Converts a complex number string into polar coordinates (r, phi).
    
    Args:
        complex_str: A string representation of a complex number (e.g., '1+2j').
        
    Returns:
        A tuple containing the modulus (r) and the phase angle (phi).
    """
    # Step 1: Convert the input string into a complex number object
    z = complex(complex_str)
    
    # Step 2: Use built-in abs() for the modulus (r)
    r = abs(z)
    
    # Step 3: Use cmath.phase() for the phase angle (phi)
    phi = cmath.phase(z)
    
    return r, phi

if __name__ == '__main__':
    try:
        # Reading input complex number
        num_z = input().strip()
        
        # Calculation
        modulus, phase = convert_to_polar(num_z)
        
        # Output results
        print(modulus)
        print(phase)
            
    except (EOFError, ValueError):
        pass

    """
    sample input:
    1+2j
    sample output:
    2.23606797749979
    1.1071487177940904
    """