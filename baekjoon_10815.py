import sys

a = int(sys.stdin.readline())
data1 = list(map(int, sys.stdin.readline().split()))
b = int(sys.stdin.readline())
data2 = list(map(int, sys.stdin.readline().split()))

# result = [False]*b
# for i, x in enumerate(data2):
#     if x in data1:
#         result[i] = True

# print(list(map(int, result)))
# 시간초과...

dic = {}
for o in data2:
    dic[o] = 0

for c in data1:
    if c in dic:
        dic[c] = 1

for d in dic:
    print(dic[d], end = ' ')

# 시간에 되게 오래 걸렸지만 정답

# 이진탐색을 이용하면 되게 작은 시간복잡도를 가지고 구할 수 있다.

