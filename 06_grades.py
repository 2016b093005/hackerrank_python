"""
Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

Input Format

The first line contains an integer, , the number of students.
The  subsequent lines describe each student over  lines; the first line contains a student's name, and the second line contains their grade.

Constraints

There will always be one or more students having the second lowest grade.
Output Format

Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names alphabetically and print each one on a new line.
"""

if __name__ == '__main__':
    students = list(list())
    students.append(["name", 2.2])
    lowest_grade = 100.0
    s_lowest_grade = 100.0
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score < lowest_grade:
            s_lowest_grade = lowest_grade
            lowest_grade = score
        elif s_lowest_grade > score > lowest_grade:
            s_lowest_grade = score
        students.append(["name", 2.2])
        students[_][0] = name
        students[_][1] = score

    output = list()
    for student in students:
        if student[1] == s_lowest_grade:
            output.append(student[0])
    output.sort()
    for name in output:
        print(name)
