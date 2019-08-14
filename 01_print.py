"""
Read an integer .

Without using any string methods, try to print the following:


Note that "" represents the values in between.

Input Format

The first line contains an integer .

Output Format

Output the answer as explained in the task.
"""
if __name__ == '__main__':
    n = int(input("Enter a number : "))
    for n1 in range(0, n):
        print(n1 + 1, end="")
