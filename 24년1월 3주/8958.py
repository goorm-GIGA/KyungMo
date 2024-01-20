# 연속된 O의 갯수가 문제의 점수

def countScore():
    count = 0
    result = 0
    for i in range(len(problem)):
        if problem[i] == 'O' and problem[i-1] == 'O':
            count += 1
            result += count
        elif problem[i] == 'O':
            count += 1
            result += 1
        else:
            count = 0
    print(result)
    
n = int(input())

for _ in range(n):
    problem = input()
    countScore()