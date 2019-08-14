import re

if __name__ == '__main__':
    input_data = input("Enter camel cased string : ")
    # test_data = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    test_data2 = re.compile(' +')
    i = 0
    for c in input_data:
        if test_data2.search(c):
            i = i+1
    print(i)


