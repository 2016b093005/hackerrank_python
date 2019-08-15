def split_and_join(line):
    # newstr = line.replace(" ", "-")
    # return newstr
    strlist = line.split()
    newstr = "-".join(strlist)
    return newstr

if __name__ == '__main__':
    input_data = input()
    split_and_join(input_data)