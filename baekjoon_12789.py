a = int(input())
lst = list(map(int, input().split()))
rev_lst = list(reversed(lst))
stack = []
def snack(a, rev_lst):
    for i in range(1,a+1):
        while rev_lst:
            k = rev_lst.pop()
            if k == i:
                break
            if stack and stack[-1] == i:
                stack.pop()
                break
            stack.append(k)
    
    if stack:
        return print('Sad')
    else:
        return print('Nice')
snack(a, rev_lst)