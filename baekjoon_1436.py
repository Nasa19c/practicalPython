# import sys
# a = int(sys.stdin.readline())

# k = 0
# for i in range(10000):
#     if a == 0:
#         print(k)
#         break

#     if '666' in str(i):
#         k = i
#         a -= 1


# 백준 2839
a =  int(input())

count = 10e8
for i in range(5000//5 +1):
    for j in range(5000//3):
        if 5*i + 3*j == a:
            count = min(count, i+j)
if count == 10e8:
    count = -1
print(count)