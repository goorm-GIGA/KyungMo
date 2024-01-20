n, m = map(int, input().split())

temp = []

def dfs(start):
    if len(temp) == m:
        for i in range(m):
            print(temp[i], end=' ')
        print()
        return
    
    for j in range(start, n+1):
        temp.append(j)
        dfs(j)
        print(temp.pop())
    
dfs(1)