'''ITERATORS
--> an iterator is an object which contain countable number of objects
    an iterator can be ierated upon i.e we can access through each value in all values
    it implements iterator protocol consisting of methods __iter__ and __next__ .for loop works on this type.
    Anything we can loop over is called iterables
    iterators defined to give the next element present in iterables such as list,tuples,sets etc seqquential datatypes

example '''
mylist= [1,2,3,4]                      # here 'mylist' is an iterator
for i in mylist:
    print(i)                   # using for loop to iterate over mylist and printing values in it

myiter = mylist.__iter__()
print(myiter)
# here iter() will only give you the object of iterator
# if we want to extract the first value only of list then
print(myiter.__next__())
# here next() will give you the next value or element in iteration
print(myiter.__next__())      # gives the second value in iteration'''


# another method
'''my = [2,3,4]
myl = iter(my)
myt = next(myl)
print(myt)'''

n = [1,2,'sasi']
i_n = iter(n)
while True:
    try:
        ne = next(i_n)
        print(ne)
    except StopIteration:
        break

# creating an own iterator
 class Ten:
    def __init__(self):
        self.num= int(input('enter the value to initiate :'))
    def __iter__(self):
        return self
    def __next__(self):
        if self.num <= 10:
           val = self.num
           self.num+=1
           return val
        else:

            raise StopIteration                   # inorder to stop the loop raising the exception




values = Ten()
print(values.__next__())            # return the first value in iteration order
print(values.__next__())            # return the second value

# another example
def print_each(iterable):
    iterator = iter(iterable)
    while True:
        try:
            item = next(iterator)
        except StopIteration:
            break
        else:
            print(item)

print_each(['sasikanth',13,22])


'''**some useful iterators***
 ACCUMULATE  : this iterator takes 2 arguments iterable target and function followed at each each value iteration in iteration
                .If no  function addition takes place default 
                .If i/p iterable is empty then o/p iterable is also empty
                
 example:'''
import itertools
import operator
list1 = [1,2,3,4]
list2 = [2,3,4,5]
print ("The sum after each iteration is : ",end="")
print (list(itertools.accumulate(list2)))                # here we are not passing function addition of every iterator
                                                          # with preceeding ones takes place

print ("The product after each iteration is : ",end="")
print (list(itertools.accumulate(list1,operator.mul)))         # passing multiplication operation ,succesive product of every iterator takesplace

'''CHAIN:
this will print all iterable targets one after one mentioned in its arguments'''
list3 =['sasikanth','bhavya','AA']
print ("All values in mentioned chain are : ",end="")
print (list(itertools.chain(list1,list2,list3)))


''''chain.from_iterable():
this function similar as chain but here arguments must be list of lists or any other iterable conatainer'''
list4 =[list1,list2,list3]
print ("All values in mentioned chain are : ",end="")
print (list(itertools.chain.from_iterable(list4)))

'''COMPRESS
this iterator selectively picks the values to print from container passed 
according boolean list value passed as other argument i.e The arguments corresponding to boolean true are printed 
else all are skipped
example:'''
print ("The compressed values in string are : ",end="")
print (list(itertools.compress('sasikanth and his friend',[1,0,0,0,0,1,0,0,1,0,0,0,0])))

'''dropwhile :- This iterator starts printing the characters only after the func. in argument 
                returns false for the first time
                example :'''
print ("The values after condition returns false : ",end="")
list5=[2,4,6,9]
print (list(itertools.dropwhile(lambda x : x%2==0,list5)))

''' filterfalse :-  this iterator prints only values that return false for the passed function.
example:'''
list6= [17,2,4,5,8,9,18,11,13]
print (list(itertools.filterfalse(lambda x : x%2==0,list6)))





