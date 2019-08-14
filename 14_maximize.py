# # Enter your code here. Read input from STDIN. Print output to STDOUT
# if __name__ == '__main__':
#     num = input().split()
#     list_num = int(num[0])
#     modulo_num = int(num[1])
#     total = 0
#     out_list = list()
#     for i in range(list_num):
#         max_element = -200
#         for element in map(int, input().split()):
#             if element > max_element:
#                 max_element = element
#         total = total + (max_element**2)
#     print(total % modulo_num)
from itertools import product

K,M = map(int,input().split())
N = (list(map(int, input().split()))[1:] for _ in range(K))
results = map(lambda x: sum(i**2 for i in x)%M, product(*N))
print(max(results))