cube = lambda x: x ** 3  # complete the lambda function


def fibonacci(n):
    # return a list of fibonacci numbers
    fib_list = list()
    if n == 0:
        return fib_list
    fib_list.append(0)
    if n == 1:
        return fib_list
    fib_list.append(1)
    for i in range(2, n):
        fib_list.insert(i, fib_list[i - 1] + fib_list[i - 2])
    return fib_list


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
