from itertools import combinations

N = int(input())
L = input().split()
K = int(input())
print(f' {N}, {L}, {K}')

C = list(combinations(L, K))
print(C)
F = filter(lambda c: 'a' in c, C)
print("{0:.3}".format(len(list(F))/len(C)))