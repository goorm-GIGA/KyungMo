hashmap = {1 : 'a', 2 : 'b', 3 : 'c', 4 : 'd',
           5 : 'e', 6 : 'f', 7 : 'g', 8 : 'h',
           9 : 'i', 10 : 'j', 11 : 'k', 12 : 'l',
           13 : 'm', 14 : 'n', 15 : 'o', 16 : 'p',
           17 : 'q', 18 : 'r', 19 : 's', 20 : 't',
           21 : 'u', 22 : 'v', 23 : 'w', 24 : 'x',
           25 : 'y', 26 : 'z'}

hashmap_2 = {'a': 1, 'b': 2, 'c': 3, 'd': 4,
           'e': 5, 'f': 6, 'g': 7, 'h': 8,
           'i': 9, 'j': 10, 'k': 11, 'l': 12,
           'm': 13, 'n': 14, 'o': 15, 'p': 16,
           'q': 17, 'r': 18, 's': 19, 't': 20,
           'u': 21, 'v': 22, 'w': 23, 'x': 24,
           'y': 25, 'z': 26}

def wordToNumber(word):
    result = []
    for i in word:
        result.append(hashmap_2[i])
    return result

def numberToWord(number):
    result = []
    for i in number:
        result.append(hashmap[i])
    return result

def findNum(word):
    return hashmap_2[word]

def increaseList(list):
    for i in range(len(list)):
        list[i] += 1
        if list[i] == 27:
            list[i] = 1

def is_sublist(password, sublist):
    for i in range(len(password) - len(sublist) + 1):
        if password[i:i+len(sublist)] == sublist:
            return True
    return False

password = input()
n = int(input())

dict = []

for _ in range(n):
    dict.append(input())

for i in range(len(dict)):
    word = []
    for j in dict[i]:
        word.append(findNum(j))
    dict[i] = word

password = wordToNumber(password)

while True:
    for i in dict:
        if is_sublist(password, i):
            for j in numberToWord(password):
                print(j, end='')
            break
    else:
        increaseList(password)
        continue
    break