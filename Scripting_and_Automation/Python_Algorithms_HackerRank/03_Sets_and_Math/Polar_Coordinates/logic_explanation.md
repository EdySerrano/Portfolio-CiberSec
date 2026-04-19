# Challenge: Polar Coordinates
## Problem Description
A complex number `z=x+iy` can be represented in Cartesian coordinates `(x,y)` or in polar coordinates `(r,ϕ)`. The task is to take a complex number as input and output its modulus r (distance from the origin) and its phase angle ϕ (angle from the positive x-axis).

## Logic & Approach
Python provides the cmath module specifically for complex mathematical operations:

1. **Complex Object Creation:** I used the complex() constructor to parse the input string into a format Python understands as a complex number.

2. **Modulus (r):** The modulus is calculated using the built-in abs() function, which for complex numbers follows the formula: $r = \sqrt{x^2 + y^2}$.

3. **Phase (ϕ):** I used cmath.phase() to calculate the phase angle in radians. This function is more reliable than manual `atan2` implementations as it handles the signs of the real and imaginary parts automatically.

## Complexity Analysis
* **Time Complexity: O(1)** - Mathematical transformations and function calls take constant time regardless of the input size.

* **Space Complexity: O(1)** - No additional data structures are required to store the result.

## Cybersecurity Perspective
Polar coordinates are fundamental in Digital Signal Processing (DSP) and RF Analysis. When analyzing wireless security (Wi-Fi, Bluetooth), signals are often represented as complex numbers. Converting these to polar form allows an analyst to identify Signal Jamming patterns or perform Side-Channel Analysis by measuring phase shifts in electromagnetic emissions.


**Solved on:** 2026-04-19

*Link to challenge: HackerRank* - [Polar Coordinates](https://www.hackerrank.com/challenges/polar-coordinates/problem)