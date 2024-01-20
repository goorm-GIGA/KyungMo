from collections import deque

cards = deque()

def moving():
    cards.popleft()
    cards.append(cards.popleft())
    
n = int(input()) 

for i in range(n):
    cards.append(i+1)
    
while len(cards) > 1:
    moving()
    
print(cards[0])