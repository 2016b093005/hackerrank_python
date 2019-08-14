"""
CSS colors are defined using a hexadecimal (HEX) notation for the combination of Red, Green, and Blue color values (RGB).

Specifications of HEX Color Code

■ It must start with a '#' symbol.
■ It can have  or  digits.
■ Each digit is in the range of  to . ( and ).
■  letters can be lower case. ( and  are also valid digits).
You are given  lines of CSS code. Your task is to print all valid Hex Color Codes, in order of their occurrence from top to bottom.

CSS Code Pattern
Input Format

The first line contains , the number of code lines.
The next  lines contains CSS Codes.

Constraints



Output Format

Output the color codes with '#' symbols on separate lines.
"""
# fetched_date = date_re_abr2.search(strn).group(1)
# Enter your code here. Read input from STDIN. Print output to STDOUT

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
import sys

[print(j) for i in sys.stdin for j in re.findall('[\s:](#[a-f0-9]{6}|#[a-f0-9]{3})', i, re.I)]