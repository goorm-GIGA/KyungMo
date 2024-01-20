x = int(input())

# 연산 횟수를 저장할 배열 초기화
dp = [0] * (x + 1)

# 2부터 x까지 각 숫자에 대해 최소 연산 횟수 계산
for i in range(2, x + 1):
    # 1을 뺀 경우의 연산 횟수
    dp[i] = dp[i - 1] + 1

    # 2로 나누어 떨어지는 경우, 최소값 비교
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

    # 3으로 나누어 떨어지는 경우, 최소값 비교
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[x])
