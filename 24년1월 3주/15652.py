n, m = map(int, input().split())

comb = []

for _ in range(m):
    comb.append(1)
    

result = [comb[:]]

while True:
    for idx in range(m-1, -1, -1):
        if comb[idx] < n:
            comb[idx] += 1
            for j in range(idx + 1, m):
                comb[j] = comb[idx]
            result.append(comb[:])
            break
    else:
        break

for node in result:
    print(" ".join(map(str, node)))