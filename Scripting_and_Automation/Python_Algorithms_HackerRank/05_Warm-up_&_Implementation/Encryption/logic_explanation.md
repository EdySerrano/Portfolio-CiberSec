# Challenge: Encryption

## Problem Description
An English text needs to be encrypted using a grid transposition cipher. After removing spaces from the text, the length $L$ is used to establish grid dimensions such that $\lfloor\sqrt{L}\rfloor \le \text{rows} \le \text{columns} \le \lceil\sqrt{L}\rceil$. The text is written row by row into this matrix layout, and the final encoded message is built by reading the characters column by column, separating each column with a space.

## Logic & Approach
To solve this without constructing an actual 2D matrix in memory, I mapped out the structural pattern using string indexing and arithmetic steps:

1. **Space Stripping & Sizing:** I removed all structural spaces using `.replace(" ", "")` and derived the total boundary length $L$.

2. **Dimension Determination:** I initialized `rows` and `cols` using `math.floor(math.sqrt(n))` and `math.ceil(math.sqrt(n))`. If the calculated area ($\text{rows} \times \text{cols}$) fell short of $L$, `rows` was incremented by 1 to satisfy the container requirements.

3. **Virtual Matrix Slicing:** Instead of iterating through nested loops to write and read from an array of lists, I leveraged Python's **extended slicing syntax** (`s_cleaned[c::cols]`). Starting at each column index `c`, stepping forward by the total number of columns (`cols`) directly extracts the vertical elements of that column in $O(k)$ time.

## Complexity Analysis
* **Time Complexity: O(n)** - Where n is the length of the string. Slicing every column takes linear time total because each character in the cleaned string is visited exactly once during transcription.

* **Space Complexity: O(n)** - We allocate intermediate space to store the stripped string and the resulting list of transposed strings before joining them.

## Cybersecurity Perspective
This challenge is a direct implementation of a **Transposition Cipher**. In classical cryptography, transposition ciphers scramble the order of characters without changing the characters themselves, disrupting **Frequency Analysis** patterns across contiguous blocks of text. While vulnerable to modern cryptanalysis via anagramming, understanding transposition grids is foundational for reverse-engineering legacy firmware protocols, obfuscation layers, or parsing customized data-interleaving schemas in hardware communication channels.

**Solved on:** 2026-06-04

*Link to challenge: HackerRank* - [Encryption](https://www.hackerrank.com/challenges/encryption/problem)