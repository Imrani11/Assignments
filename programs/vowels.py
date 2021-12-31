name = input('enter the string :')
vowels = 'aeiou'
playerA =[]
playerB =[]
'''for v in name:
    if v in vowels:
        playerA.append(v)
    else:
        playerB.append(v)
import itertools'''
string = name
'''words =set([''.join(p) for p in itertools.combinations(string,2)])
order = list(words)
for i in order:
  if i[0] in vowels or i[1] in vowels:
    playerA.append(i)
  else:
    playerB.append(i)'''

res = [string[i: j] for i in range(len(string))
          for j in range(i + 1, len(string) + 1)]
print(res)
for char in res:
    if char[0] in vowels:
       playerA.append(char)
    else:
        playerB.append(char)
print(playerA)
print(playerB)
if len(playerA) > len(playerB):
    print('playerA is the winner')
else:
    print('playerB is the winner')



















