a = int(input())
k = [str(input()) for _ in range(a)]
z = []

for i,x in enumerate(k):
    if x[-3:] != 'jpg' and x[-3:]!= 'png':
        k.remove(x)
print(k)