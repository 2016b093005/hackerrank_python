from sys import exit


def is_unique(input_string=None):
    if input_string is None:
        exit(1)
    unique_chars = []
    for c in input_string:
        if c in unique_chars:
            return False
        else:
            unique_chars.append(c)
    return True


def reducer(input_string=None):
    if input_string is None:
        exit(0)
    i = 0
    return_str = ''
    for element in range(0, len(input_string)):
        if i >= len(input_string) - 1:
            if i == len(input_string)-1:
                return_str = return_str + input_string[-1]
            break
        if input_string[i] == input_string[i + 1]:
            i = i + 2
        else:
            return_str += input_string[i]
            i = i + 1
    return return_str


if __name__ == '__main__':
    test_string = input("Enter test string : ")
    process = True
    reduced_str = test_string
    while process:
        if not is_unique(reduced_str):
            temp_str = reduced_str
            reduced_str = reducer(reduced_str)
            if reduced_str == temp_str:
                process = False
        else:
            process = False
    print(f'Reduced string : {reduced_str}')
