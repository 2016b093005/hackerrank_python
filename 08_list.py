if __name__ == '__main__':
    N = int(input())
    my_list = list()
    for i in range(int(N)):
        input_data = input()
        input_data = input_data.split()
        if input_data[0] == 'insert' or input_data[0] == 'append':
            if len(input_data) == 3:
                my_list.insert(int(input_data[1]), int(input_data[2]))
            else:
                my_list.append(int(input_data[1]))
        elif input_data[0] == 'print':
            print(my_list)
        elif input_data[0] == 'remove':
            my_list.remove(int(input_data[1]))
        elif input_data[0] == 'sort':
            my_list.sort()
        elif input_data[0] == 'pop':
            my_list.pop()
        elif input_data[0] == 'reverse':
            my_list.reverse()
        else:
            print('Given wrong input')
