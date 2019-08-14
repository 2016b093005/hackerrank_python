if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    query_list = student_marks.get(query_name)
    total_mark = 0.0
    for mark in query_list:
        total_mark += mark
    average = '{0:.2f}'.format(total_mark / len(query_list))
    print(average)
