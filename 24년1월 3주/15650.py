n, m = map(int, input().split())

# 1~n 중복 없이 m개를 고른 수열

temp = []
isUsed = [0] * 10

def dfs(start):
    if len(temp) == m:
        for i in range(len(temp)):
            print(temp[i], end=' ')
        print()
        return
    for j in range(start, n+1):
        if not isUsed[j]:
            temp.append(j)
            isUsed[j] = 1
            dfs(j)
            temp.pop()
            isUsed[j] = 0
    
dfs(1)