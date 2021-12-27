'''GENERATORS
--> It is the function it need not generate value.they allow to decalre a function which behaves like an iterator
    rather than return it use with 'YEILD'  keyword
    if the body of DEF function contains yeild it means the function converted as generator function
    Generators are mostly used in loops to generate an iterator by returning all the values in the loop
     without affecting the iteration of the loop
example:'''

def simple():
    yield 1
    yield 2
for val in simple():
    print(val)
    print()
 # to print one value:
x = simple()
print(x.next())

# example for using generator function for fibnonacci series
def fibo(func):
    x,y=0,1
    while x<func:
        yield x
        x,y= y,y+x
p = fibo(6)                 # creating generator object
print(p.__next__())
print(p.__next__())
print(p.__next__())
print(p.__next__())           # iterating over generator object

# another example
def squar():
    n =1
    while n<=5:
        sq = n**2
        yield sq
        n+=1
val = squar()
while True:
    try:
       print('received on next', val.__next__())
    except StopIteration:
        break

# reversing a string
def revstr(str1):
    length = len(str1)
    for i in range(length-1,-1,-1):
        yield str1[i]
for char in revstr('sasikanth'):
    print(char)

import random
def luck():
 for i in range(5):
    yield random.randint(1,20)         # in b/w the 1 to 20 , 5 random integers will be generated
for i in luck():
    print('%d'%i)




from random import choice
def song(song_list):
    new = None
    while True:
        if new!= None:
            if new not in song_list:
                song_list.append(new)
            new =yield (new)
        else:
            new = yield (choice(song_list))

songs= ['a','b','c','d','e','f']
program = song(songs)
for i in range(4):
    print(next(program))





