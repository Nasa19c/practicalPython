# prev = 0
# crnt = 1
# for _ in range(10):
#     crnt = prev + crnt
#     prev = crnt
# print(crnt)


def fibonachi(n):
    if n<=2:
        return 1
    else:
        return fibonachi(n-1) + fibonachi(n-2)
print(fibonachi(5))