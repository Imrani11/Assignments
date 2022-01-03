'''sum = 0
list = [12,24,12,24]
for element in range(0,len(list)):
    sum = sum+list[element]
print("Sum of all elements in given list: ",sum)'''


'''list = [12,24,12,24]
def count(sum):
    soup = 0
    for i in sum:
        soup+=i
    return soup

print(count(list))'''

'''list = [12,24,12,24]
i= 0
result = 0
while i <len(list):
    result = result+list[i]
    i+=1
print(result) '''

'''class List:
    def __init__(self,list):
        self.list = list
    def count(self):
            soup = 0
            for i in self.list:
                soup += i
            print(soup)
add = List([12,12,12,12])
add.count()'''                      # sum of elements in a list
'''-------------------------------------------------------------------------------------------------------------------'''
'''mult= 1
list = [2,3,4]
for element in range(0,len(list)):
    mult = mult*list[element]
print("product of all elements in given list: ",mult)'''

'''list = [2,3,4,5]
def product(mult):
    soup = 1
    for i in mult:
        soup*=i
    return soup
print(product(list))'''

'''import numpy
list1 = [1, 2, 3]
list2 = [3, 2, 4]
result1 = numpy.prod(list1)
result2 = numpy.prod(list2)
print('list1 result :',result1)
print('result of list2 :',result2)'''

'''class Product:
    def __init__(self, list):
        self.list = list
    def multiply(self):
        i = 0
        result = 1
        while i < len(self.list):
            result = result * self.list[i]
            i += 1
        print(result)
final = Product([2,2,3])
final.multiply()'''         # product of elements in list
'''--------------------------------------------------------------------------------------------------------------'''

'''list = [2,10,3,5]
list.sort()
print("Largest element is:", list[-1])'''

'''class Max:
    def __init__(self,list):
        self.list = list
    def maximum(self):
        print("Largest element is:", max(self.list))

find = Max([10, 20, 4, 45, 99])
find.maximum()'''

'''list = []
num = int(input("Enter number of elements in list: "))
for i in range(1, num + 1):
    element = int(input("Enter elements: "))
    list.append(element)
print("Largest element is:", max(list))'''

'''x = 0
list =[1,2,3,4]
lar = list[x]
while x<len(list):
    if list[x]>lar:
        lar = list[x]
    x = x+1
print("Largest number of the list by using while loop:",lar)'''

'''--------------------------------------------------------------------------------------------------------------'''


'''list1 = [2,5,4,1]
list1.sort()
print("Smallest element is:",list1[:1])'''

'''class Min:
    def __init__(self,list):
        self.list = list
    def minimum(self):
        print("smallest element is:", min(self.list))

find = Min([10, 20, 4, 45, 99])
find.minimum()'''

'''list = []
num = int(input("Enter number of elements in list: "))
for i in range(1, num + 1):
    ele= int(input("Enter elements: "))
    list.append(ele)
print("Smallest element is:", min(list))'''

'''x = 0
list =[2,3,4]
small = list[x]
while x<len(list):
    if list[x]<small:
        small = list[x]
    x = x+1
print("small number of the list by using while loop:",small)''' #smallest number from the list
'''------------------------------------------------------------------------------------------------------------'''
'''list = [1, 3, 5, 6, 3, 5, 6, 1]
print ("The original list is : " +  str(list))
res = []
for i in list:
    if i not in res:
        res.append(i)
print("The list after removing duplicates : " + str(res))'''

'''test_list = [1,2,3,4,4,3,2,1]
print ("The original list is : " +  str(test_list))
test_list = list(set(test_list))
print ("The list after removing duplicates : " + str(test_list))'''

'''def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list
duplicate = [2,4,6,4,2,1,6,7,8]
print(Remove(duplicate))'''

'''class Duplicate:
    def __init__(self):
        print('the elements after removing duplication from the list')
    def Remove(self,duplicate):
        final_list = []
        for num in duplicate:
            if num not in final_list:
                final_list.append(num)
        print('the final list :',final_list)

double =  Duplicate()
double.Remove([1,2,4,2,4,6,7,9])      #removing duplicates from the list'''

# a list containing group of strings and converting them into upper case letters

'''def func(lis):
  final =[x.upper() for x in lis]
  print('final upper case string list:',final)

func(['sasi','kanth','sasikanth'])'''

# program to convert month name to a number of days
'''month = input('enter your month :')
if month =='February':
    print('this month has 28 days usually but for leap year it has 29 days')
elif month in ['jan','march','july','august','october','december','may']:
    print('this month has 31 days')
elif month in ['april','june','september','november']:
    print('this month has 30 days')
else:
    print('please enter valid month')'''

# Reverse list of elements and print in upper case
'''name = ['sasi','kanth','sasikanth']
rever = name[::-1]
res = []
for i in rever:
    if i.lower():
        res.append(i.upper())
print(res)'''

# Check if all dictionaries in a list are empty or not
'''l = [{'a':1},{},{}]
for i in l:
  if  not i:
   print(all(i))'''

# Extend a list without append
'''list1 = [1,2,3,4]
list2 = [5,6,7,8,9]
list1[4:] =list2                        # from 4th index of list1 we are assigning elements in list2
print(list1)'''

# Finding all the values in a list are greater than a specified number
'''list1 =[2,3,4,5]
k= int(input('enter the number :'))
count = 0
num=[]
for i in list1:
    if i>k:
        num.append(i)
        count+=1
print('the numbers greater than given number are :',count)
print('the numbers are :',num)'''

# Finding the list in a list of lists whose sum of elements is the highest
'''list1 = [[1,2,3],[3,4,5],[5,6,7]]
res = max(list1)
print("maximum list is :",res)
print("adding the element in list: ",sum(res))'''

# Access dictionary keys element by index

'''def dictionary(a):
    key_list = list(a)
    key = key_list[int(input('enter the index'))]
    print('the required key by index in the dictionary:',key)

dictionary({'a':1,'b':2,'c':3}) '''

# Iterate over two lists simultaneously

'''def iterate(a,b):
    for p,q in zip(a,b):
     print(p,q)

iterate(['m','n'],['k','l'])'''

# Insert a given string at the beginning of all items in a list
'''
def attach(list1,string):
    string = string+'{}'
    final =[string.format(i)for i in list1]
    return final

string1= input("Enter your string")
list2= [1,2,3]
print(attach(list2,string1))'''

# Print a list of space-separated elements

# given =>ar = [1,2,3,4,5]
# needed [1 2 3 4 5]

# Create a list of empty dictionaries
'''res =[]
for i in range(6):
    i= {}
    res.append(i)
print(res)  '''

# Check if the n-th element exists in a given list
'''list1 = [2,3,4,5]
n =int(input('enter the number :'))
result = len(list1)>=n
print(result)'''

# Replace the last element in a list with another list
'''def rep(list1,list2):
    list1[-1:]= list2
    return list1
lis1 = [2,3,4]
lis2 = [5,6]
print(rep(lis1,lis2))'''

#

'''l=[1,2,3,4]
str1=''
for i in l:
    s=str(i)+''
    str1+=s
l1=[]
l1.append(str1)
print(l1)'''

# Shuffle list and print
'''import random
def shuff(list1):
    print('before shuffling :',list1)
    for i in range(len(list1)-1,0,-1):
        j = random.randint(0,i+1)
        list1[i],list1[j] =list1[j],list1[i]
    print('the shuffled list is :',str(list1))

list1 = [1,3,5,7,9]
shuff(list1)'''

# Difference between 2 lists
'''def diff(list1,list2):                                                #lst= [2,3,4]
                                                                          # lst1= [5,7,9]
                                                                           # print(lst+lst1)-->o/p: [2,3,4,5,7,9]
    return(list(set(list1)-set(list2))+list(set(list2)-set(list1)))
lst1= [1,2,3,4]
lst2 = [2,3,8,1]
differ =diff(lst1,lst2)
print(differ)'''

# Select an item randomly from list
'''import random
def rand(list1):
    print('the list is :',list1)
    choose = random.choice(list1)
    print('random element is:',choose)

lst =['sasikanth','hyderabad','bhavya','vijayawada']
rand(lst)'''

# Check circularly identical in two lists
'''def circular(list1,list2):
    list3 = list1*2
    print(list3)
    for i in range(0,len(list1)):
        z=0
        for j in range(i,len(list1)+i):
            if list2[z] == list3[j]:
                z= z+1
            else:
                break
        if z==len(list1):
            return True
        else:
            False

list1 = [10, 10, 0, 0, 10]
list2 = [10, 10, 10, 0, 0]
if(circular(list1, list2)):
    print("Yes")
else:
    print("No")'''

# Generate all sublists of list
'''def sub_lst(list1):
    lists= []
    for i in range(len(list1)+1):
        for j in range(i):
           lists.append(list1[j:i])
    print(lists)

lst =[1,2,3,4]
sub_lst(lst)'''

# Create a list by concatenating a given list which range goes from 1 to n
'''def my_list(list1,m):
    new_list =['{}{}'.format(y,x) for x in range(1,m+1) for y in lst1]
    return new_list

lst1=['p','q']
m= int(input('enter the count :'))
print(my_list(lst1,m))'''

# Split a list based on first character of word
'''from itertools import groupby
from operator import itemgetter
word_list=['a','apple','sasikanth','bhavya','ball','dog','tiger','eagle','cow','vishakaptanam','hyderabad']
for letter,words in groupby(sorted(word_list)), key =itemgetter(0)):
   print(letter)
   for word in words:
      print(word)'''

# Split a list into different variables
'''lst =['blue',(13,22),('ram','sita')]
va1,va2,va3=lst
print(va1,va2,va3)'''

# Generate group of five consecutive numbers in a list

'''p= [[5*i + j for j in range(1,6)] for i in range(5)]
print(p)'''

# Find missing and additional values
'''list1= [1,2,3,4,5,6]
list2 =[4,5,6,7,8,9]
print('missing values in list2 :',(set(list1).difference(list2)))
print('additional values in list2:',(set(list2).difference(list1)))
print('missing values in list1 :',(set(list2).difference(list1)))
print('additional values in list1:',(set(list1).difference(list2)))'''

# Flatten a shallow
'''import itertools
def list1(lst):
    print('the actual list is :',lst)
    flattened_list = list(itertools.chain(*lst))
    return flattened_list

l= [[1,2,3],[4],[5,6,7]]
print('the flattened list is :',list1(l))'''

# Insert an element before each element of a list
'''scope =['sasikanth','binnu','ram','sita']
print('actual list :',scope)
exp= [v for i in scope for v in ('see',i)]
print(exp)'''

# Print a nested lists (each list on a new line) using the print() function
'''color =[['blue'],['black'],['cyan']]
print('\n'.join([str(i)for i in color]))'''

# Split a list every Nth element
'''C = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
'def list_slice(S, step):
    return [S[i::step] for i in range(step)]
print(list_slice(C,3))'''

 # Concatenate elements of a list
'''lst =['13','sasikanth','binnu','22']
sent = ''
for i in lst:
     sent = sent+str(i)+' * '
order = sent[:-1]
print(order)'''


# Printing elements in ascending order
'''def asc_order(lst):

        lst.sort()
        print("The ascending order of the list is: ",lst)

lst = [2,4,5,3,7,9]
asc_order(lst)'''

# Change the position of every nth value with (n+1)th value
'''def change_pos(my_list):

    for i in range(0,len(my_list),2):

        my_list[i],my_list[i+1]=my_list[i+1],my_list[i]
    return my_list

my_list =[1,2,3,4,5,6]
print(change_pos(my_list))'''

# Converting multiple integers into single integer
'''def convert(lst):
   result = int(''.join(map(str,lst)))
   return (result)

lst =[1,2,3,4]
print(convert(lst))'''

# Convert a pair of values into a sorted unique array
'''def sorted_val(lst):
    print('original list :',lst)
    print('sorted unique data :',sorted(set().union(*lst),reverse=True))
lst = [(1,2),(3,4),(5,6)]
sorted_val(lst)'''

# Convert a string to a list
'''def convert(str1):
    string_list = list(str1.split(' '))
    return string_list

stri =convert(input('enter the string :'))
print(stri)'''

# Find the list in a list of lists whose sum of elements is the highest
'''lst= [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
index =0
max_index = 0
sum_max = 0
for i in lst:
    sum_list =0
    for j in i:
        sum_list= sum_list+j
    if sum_list>sum_max:
        sum_max = sum_list
        max_index= index
    index= index+1
print(lst[max_index])'''

# Insert a given string at the beginning of all items in a list
'''def prepend(list1, str1):
    # Using format()
    str1 += '{0}'
    lis = [str1.format(i) for i in list1]
    return (lis)

list1 = [1, 2, 3, 4]
str1 = 'sasikanth'
print(prepend(list1, str1))'''

# Check if the n-th element exists in a given list
'''list1 = [2,4,6,8,10]
print('the given list is :',list1)
n = int(input('enter the number to check :'))
res= len(list1)>=n
print('is the number available :',res)'''

# Check list is empty or not
'''l1 =['sasikanth','binnu','ram','sita']
l2= []
if l1:
    print('the list is not empty')
else:
    print('the list is empty')
if l2:
    print('the list is not empty')
else:
    print('the list is  empty')'''

# Remove specified index from list and print
'''l= [2,3,4,5,6,7]
index= [1,2]
for i in index:
    del l[i]
print('the remaining elements of list :',l)'''

# Finding index of an item in specified list
'''lst1 = [1,2,'sasikanth','3',6]
print(lst1.index('sasikanth'))'''

# Finding a second largest number
'''list1 =[10,20,4,45,99]
maximum = max(list1[0],list1[1])
secomax = min((list1[0],list1[1]))
for i in range(2,len(list1)):
    if list1[i]>maximum:
        secomax= maximum
        maximum=list1[i]
    elif list1[i]>secomax and maximum!=list1[i]:
        secomax=list1[i]
print('the second largest number is :',secomax)'''

# Finding a second smallest number
'''def find_len(list1):
    length = len(list1)
    list1.sort()
    print("Smallest element is:", list1[0])
    print("Second Smallest element is:", list1[1])

find_len([2,45,6,9,8,32])'''

# Get unique values
'''def unique(list1):
    list_case=[]
    for x in list1:
        if x not in list_case:
            list_case.append(x)
    for y in list_case:
            print(y,end='  ')


list1=[1,1,2,3,4,4,5,6,6]
print('the unique vals:')
unique(list1)'''

# Frequency of elements
'''random_list =['a','a','b','b','c','c','c','d']
frequency = {}
for item in random_list:
    if item in frequency:
        frequency[item]+=1
    else:
        frequency[item]=1

print('the frequency of elements are :',frequency)'''

# Find common element from 2 lists
'''def common(a,b):
    a_set = set(a)
    b_set = set(b)
    if (a_set & b_set):
        print(a_set & b_set)
    else:
        print('no common elements available')

x =[1,2,3,4]
y= [4,5,6,7]
common(x,y)'''

# Remove even elements and print list
'''list1 = [1,2,3,4,5,6]
print('the original list :',list1)
for i in list1:
    if i%2==0:
        list1.remove(i)
print('the list after removing elements :',list1)'''

#  To access index of list
'''list1=[1,2,3,4,5]
print(list1.index(2))
list2 = ['aa','ram','ram','sita',1,2,'aa']
print(list2.index('ram',0,5))                # .index(element,start,end)'''

# Clone or copy
# This method is considered when we want to modify a list and also keep a copy of the original.
'''def clonne(list1):
    lst1 = list1[:]
    return lst1
list1= ['ram','sita','binnu','sasikanth']
list2 =clonne(list1)
print('the list after cloning :',list2)'''

# Counting number elements within a specified ranges
'''def count(lis1,ll,ul):
    next = 0
    for i in list1:
        if i>=ll and i<=ul:
            next+=1
    return next
list1 = [10,20,30,40,50,60,70,80]
ll = 30
ul=80
print('the numbers for the range %d and %d'%(ll,ul),':', count(list1,ll,ul))'''

# Check a list contains sublist
'''list1 =[1,2,3,4,5]
list2 =[2,4]
flag = 0
if(all(x in list1 for x in list2)):
    flag =1
    if flag:
        print('yes list2 is in list1')
    else:
        print('list2 not exist in list1')'''

# List of characters into string
'''def change(str1):
    new =''
    for x in str1:
        new =new+x
    return new

str1 = ['s','a','s','i','k','a','n','t','h']
print('the converted list to character is :',change(str1))'''

# Create multiple list
'''obj = [[i]for i in range(4)]
list1,list2,list3,list4 = obj
print('the initialised lists are:')
print('list1 :'+str(list1))
print('list2 :'+str(list2))
print('list3 :'+str(list3))
print('list4 :'+str(list4))'''

# Select odd items of a list
'''def odd(list1):
    list2=[]
    for num in list1:
        if num%2!=0:
            list2.append(num)
    print('the odd items list is :',list2)

list1 =[1,2,3,4,5,6,7]
odd(list1)'''

# Append a list to second list
'''lis1 = [1,2,3,4]
lis2 =[5,6,7,8]
lis1[4:]= lis2
print('the list after extending lis1 with lis2 is :',lis1)'''

# Finding common items from two lists
'''def common(a,b):
    a_set = set(a)
    b_set = set(b)
    if len(a_set.intersection(b_set)) > 0:
        print('the common elements found in both sets are :',a_set.intersection(b_set))
    else:
        print('no common elements in both sets')

a= [1,2,3,4]
b=[4,5,6,7]
common(a,b)'''

# Sort a list of nested dictionaries
'''my_list = [{'name':{'sasikanth':1322}},{'name':{'sasikanth':1345}},{'name':{'sasikanth': 1456}}]
print('actual list:',my_list)
my_list.sort(key = lambda a:a['name']['sasikanth'],reverse=True)
print(my_list)'''

# Create a list with infinite elements
'''c= 0
step_size = float(input('enter the increment of steps :'))
end_point=int(input('enter the boundary :'))
my_list=[]
while c<end_point:
    my_list.append(c)
    c= c+step_size
print('the final infinite list is :',my_list)'''

# Convert list to list of dictionaries
'''test_list =['sasikanth',1322,'binnu',13,'ram',500082]
print("The original list : " + str(test_list))
key_list = ["name", "number"]
n = len(test_list)
res = []
for idx in range(0, n, 2):
    res.append({key_list[0]: test_list[idx], key_list[1] : test_list[idx + 1]})
print("The constructed dictionary list : " + str(res))'''

# compute similarity b/w two sets
'''def compareList(l1,l2):
   l1.sort()
   l2.sort()
   if(l1==l2):
      return "Equal"
   else:
      return "Non equal"
l1=[1,2,3]
l2=[2,1,3]
print("First comparison",compareList(l1,l2))
l3=[1,2,3]
l4=[1,2,4]
print("Second comparison",compareList(l3,l4))'''

# Create a list of empty dictionaries
'''res = [{} for sub in range(6)]

print("The list of empty dictionaries is : " + str(res))'''

# Check if all items of a list is equal to a given string
'''color1 = ["green", "orange", "black", "white"]
color2 = ["green", "green", "green", "green"]

print(all(c == 'blue' for c in color1))
print(all(c == 'green' for c in color2))'''

# Remove key values pairs from a list of dictionaries
'''original_list = [{'key1':'value1', 'key2':'value2'}, {'key1':'value3', 'key2':'value4'}]
print("Original List: ")
print(original_list)
new_list = [{k: v for k, v in d.items() if k != 'key1'} for d in original_list]
print("New List: ")
print(new_list)'''

# Remove duplicates from a list of lists
'''test_list = [[1, 0, -1], [-1, 0, 1], [-1, 0, 1],[1, 2, 3], [3, 4, 1]]
print("The original list : " ,test_list)
res = list(set(tuple(sorted(sub)) for sub in test_list))
print("The list after duplicate removal : " + str(res))'''

# Two digits m (row) and n (column) as input and generates a two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j
'''row_num = int(input("Input number of rows: "))
col_num = int(input("Input number of columns: "))
multi_list = [[0 for col in range(col_num)] for row in range(row_num)]

for row in range(row_num):
    for col in range(col_num):
        multi_list[row][col]= row*col

print(multi_list)'''

# Replace the last element in a list with another list
'''num1 = [1, 3, 5, 7, 9, 10]
num2 = [2, 4, 6, 8]
num1[-1:] = num2
print(num1'''

# Find a tuple, the smallest second index value from a list of tuples
'''list1 =[(1,2),(2,3),(3,4),(2,6)]
print('the original list of tuples :',list1)
list1.sort()
print('the smallest second index value from a list of tuples',list1[1])'''


























