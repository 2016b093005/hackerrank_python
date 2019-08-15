import re


def fun(s):
    # return True if s is a valid email, else return False
    ar = s.replace('@', '.').split('.')
    for ele in ar:
        if ele == '':
            return False
    if len(ar) != 3:
        return False
    if re.match("^[a-zA-Z0-9_-]*$", ar[0]) and re.match("^[a-zA-Z0-9]*$", ar[1]) \
            and int(len(ar[2])) > 0 and int(len(ar[2]) < 4):
        return True
    else:
        return False


def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
