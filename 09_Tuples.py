if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    tuple_list = list()
    for value in integer_list:
        tuple_list.append(value)
    print(hash(tuple(tuple_list)))

