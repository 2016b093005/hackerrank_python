if __name__ == '__main__':
    input_data = str(input())
    frequency = 1
    output = ""
    prev = -199
    curr = -198
    for i in input_data:
        prev = curr
        curr = int(i)
        if curr == prev:
            frequency = frequency + 1
        else:
            if int(prev) >= 0:
                output = output + "(" + str(frequency) + ", " + str(prev) + ") "
            frequency = 1
    if curr == prev:
        output = output + "(" + str(frequency) + ", " + str(prev) + ") "
    else:
        output = output + "(" + str(frequency) + ", " + str(curr) + ") "
    print(output)

