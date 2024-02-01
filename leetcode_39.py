candidates = [2,3,6,7]
target = 7
result = []

def dfs(path):
    if sum(path) == 7:
        result.append(path)
        return
    
    if sum(path) > 7:
        return
    
    for e in candidates:
        path.append(e)
        dfs(path)
        path.pop()
dfs([])
print(result)