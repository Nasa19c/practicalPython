import sys
# baekjoon 10773

# k = int(sys.stdin.readline())
# lst = []
# for _ in range(k):
#     n = int(sys.stdin.readline())
#     if n == 0:
#         lst.pop()
#     else:
#         lst.append(n)
# print(sum(lst))
# 진짜 쉬운 stack 문제..

# baekjoon 1764
n,m = map(int, sys.stdin.readline().split())
dic = {}
z = 0
for _ in range(n):
    name_n = sys.stdin.readline()
    dic[name_n] = False

for _ in range(m):
    name_m = sys.stdin.readline()
    if name_m in dic:
        z+=1
        dic[name_m] = True
        
print(z)
dic = dict(sorted(dic.items()))
for x in dic:
    if dic[x] == True:
        print(x)