import re

if __name__ == '__main__':
    num_test_case = int(input())
    out_list = list()
    for i in range(0,num_test_case):
        temp_pat = input()
        try:
            re.compile(temp_pat)
            out_list.append(True)
        except:
            out_list.append(False)
    for i in out_list:
        print(i)
