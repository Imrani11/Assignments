# program that converts the given list to nxm matrix

'''def matrix(test):
    print('the original list is :', test)
    n = int(input('enter the no.of rows :'))
    m = int(input('enter the no.of columns :'))
    k =0
    resultant=[]
    if n*m!=len(test):
        print('matrix is not possible')
    else:
        for i in range(0,n):
            sub=[]
            for j in range(0,m):
                sub.append(test[k])
                k=k+1
            resultant.append(sub)
    print('the final derived matrix is :',resultant)

matrix([1,2,3,4,5,6,7,8,9])'''


# function to create an acronym
from collections import defaultdict

'''def function(string):
    start = string[0]
    for i in range(1, len(string)):
        if string[i-1] ==' ':
            start= start+string[i]
        next = start.upper()
    return next

inp = input('enter full form :')
print('the acronym is : ',function(inp))'''

# to sort the words in dictionary order
'''def dictionary(string):
    words = string.split()
    words.sort()
    for i in words:
        print(i)

mystring = 'hello this is example how to sort'
dictionary(mystring)'''


# Convert Nested dictionary to Mapped Tuple

'''test_dict = {'gfg': {'x': 5, 'y': 6}, 'is': {'x': 1, 'y': 4},
             'best': {'x': 8, 'y': 3}}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Convert Nested dictionary to Mapped Tuple
# Using defaultdict() + loop
res = defaultdict(tuple)
for key, val in test_dict.items():
    for ele in val:
        #print(val[ele])
        print("res",res[ele])
        res[ele] += (val[ele],)
# printing result
print("The grouped dictionary : " + str(list(res.items())))'''



'''from faker import Faker
fake_info = Faker()
print(fake_info.name())
print(fake_info.email())
print(fake_info.country())
print(fake_info.profile())'''        # fake info generation

import pywhatkit as pw
cop = pw.text_to_handwriting('''my name is sasikanth.i'm from bhimavaram in andhrapradesh''')
print(cop)                      # converting text to handwritten format


