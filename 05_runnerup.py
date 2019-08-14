if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    top = -110
    runner = -110
    for i in arr:
        if i > top:
            runner = top
            top = i
        elif top > i > runner:
            runner = i

    print(runner)


