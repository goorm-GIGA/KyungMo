n, m = map(int, input().split())

# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

tmp = [0] * 10
isUsed = [0] * 10

def dfs(start):
    if start == m:
        for i in range(m):
            print(tmp[i], end=" ")
        print("")
        return
    
    for i in range(1, n+1):
        if not isUsed[i]:
            tmp[start] = i
            isUsed[i] = 1
            
            dfs(start+1)
            isUsed[i] = 0

dfs(0)