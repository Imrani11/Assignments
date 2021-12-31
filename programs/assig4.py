'''test_dict = { 'id' : 10, 'tag' : 15, 'age' : 20, 'token' : 10}
print("The original dictionary is : " + str(test_dict))
temp = []
res = dict()
for key, val in test_dict.items():
    if val not in temp:
        temp.append(val)
        res[key] = val
print("The dictionary after values removal : " + str(res))'''

'''class Dictionary:
    def __init__(self):
        self.dict = dict([('age',10),('roll',10),('lane',13),('route',10)])
        print("The original dictionary is : " + str(self.dict))
    def dictt(self):
        temp = {val: key for key, val in self.dict.items()}
        res = {val: key for key, val in temp.items()}
        print("The dictionary after values removal : " + str(res))
removal = Dictionary()
removal.dictt()'''   # removing duplicates from a dictionary

'''-------------------------------------------------------------------------------------------------------'''
'''dict1 = {'a': 12, 'b': 25, 'c': 9}
dict2 = {'c': 100, 'd': 200, 'e': 300}
for key in dict2:
    if key in dict1:
        dict2[key] = dict2[key] + dict1[key]
    else:
        pass

print(dict2)'''


'''class Dictionary:
    def __init__(self):
        self.dict1 = dict([('a',10),('b',10),('c',13),('d',10)])
        self.dict2 = dict([('b',10),('c',10),('d',13),('e',10)])
    def func(self):
        for key in self.dict2:
            if key in self.dict1:
                self.dict2[key] = self.dict2[key] + self.dict1[key]
            else:
                pass

        print(self.dict2)
next = Dictionary()
next.func()'''         # Combining two dictionary adding values for common keys.

'''--------------------------------------------------------------------------------------------------------'''
'''L = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
print("Original List: ",L)
u_value = set( val for dic in L for val in dic.values())
print("Unique Values: ",u_value)'''

'''class Dictionary:
    def __init__(self):
        self.dic = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
    def recur(self):
        print("Original List: ", self.dic)
        u_value = set(val for v in self.dic for val in v.values())
        print("Unique Values: ", u_value)

u = Dictionary()
u.recur()
                                                   # error program



--------------------------------------------------------------------------------------------------------------------------------------------------------'''

'''class Item_Type:
    def __init__(self,list):
        self.list = list
    def find(self):
        for i in list:
            print("Item of",i,"type of",type(i))

list = [1452, 11.23, 3+4j, True, 'eagle', (0, -3), [5, 1], {"class":'V', "section":'A'}]
i = Item_Type(list)
i.find()'''                      # Prints each item and its corresponding type from the following list.
'''___________________________________________________________________________________________________________________________________________'''

'''import operator
class Ascen_Desen:
    def _init_(self):
        print('To sort (ascending and descending) a dictionary by value')
    def value(self,d):
        ascen = dict(sorted(d.items(),key=operator.itemgetter(1)))
        print(ascen)
        desen = dict(sorted(d.items(), key=operator.itemgetter(1),reverse=True))
        print(desen)

a = Ascen_Desen()
a.value({1: 2, 3: 4, 4: 3, 2: 1, 0: 0})'''
'''------------------------------------------------------------------------------------------------------------------------------------------------------'''

'''class Add_Key(dict):
    def _init_(self):
        self = dict()
    def final(self,key,value):
        self[key] = value
a = Add_Key()
a.final(1,'one')
a.final(2,'two')
print(a)                               # addind a key to dictionary'''


'''-------------------------------------------------------------------------------------------------------------------------------------------------------'''

'''class Key:
    def _init_(self):
        print('Checking if a given key already exists in a dictionary')
    def check(self,dict,key):
        self.dict = dict
        self.key = key
        if key in dict:
            print("present",end=" ")
            print("value =",dict[key])
        else:
            print("not present")
dict = {'a': 100, 'b':200, 'c':300}
key = input("enter your key:")
k = Key()
k.check(dict,key)'''

'''------------------------------------------------------------------------------------------------------------------------------------------------------'''

'''class Multi:
    def __init__(self,d):
        self.d = d
    def result(self):
        for i in range(1,n+1):
            d[i] = i*i
        print(d)
d = dict()
n = int(input("enter ur number:"))
m = Multi(d)
m.result()'''                                  # Generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x)

'''----------------------------------------------------------------------------------------------------------------------------------------------------'''

'''class Square(dict):
    def __init__(self):
        self = dict()
    def square(self):
        for x in range(1,n+1):
            self[x] = x**2
        print(self)

n= int(input('enter the value :'))
sq = Square()
sq.square()'''              #Printing a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys
'''--------------------------------------------------------------------------------------------------------------------------------------------------'''

'''class Add:
    def __init__(self):
        print('merging two python dictionaries')
    def fusion(self,dict1,dict2):
        di = dict1.update(dict2)
        print(dict1)

dic1 = dict([('a',2),('b',3)])
dic2 = dict([('c',4),('d',5)])
c = Add()
c.fusion(dic1,dic2)'''

'''-------------------------------------------------------------------------------------------------------------------------------------------------------'''

'''class Sum:
    def __init__(self):
        print('sum of all items in given dictionary')
    def giveSum(self,dictionary):
        list =[]
        for i in dictionary:
            list.append(dictionary[i])
        result = sum(list)
        print("Sum  :",result)

d = dict([('a',40),('p',80),('x',40)])
s = Sum()
s.giveSum(d)'''

'''----------------------------------------------------------------------------------------------------------------------------------------------------'''

'''class Product:
    def __init__(self):
        print('product of all items in given dictionary')
    def giveproduct(self,dictionary):
          answer= 1
          for i in dictionary:
            answer = answer * dictionary[i]
          print('product is :',answer)

d = dict([('a',40),('p',1),('x',10)])
s = Product()
s.giveproduct(d)'''

'''------------------------------------------------------------------------------------------------------------------------------------------------------'''

'''class Trans:
    def __init__(self,key,values):
       self.key = key
       self.values = values
    def mapping(self):
        dictionary = dict(zip(self.key,self.values))
        print(dictionary)

p = ['a','b','c']
q = [1,2,3]
z= Trans(p,q)
z.mapping()                       # Mapping two lists into a dictionary'''

'''------------------------------------------------------------------------------------------------------------------------------------------------------'''

'''
from collections import OrderedDict
class Arrange:
    def __init__(self,dic):
        self.dic =dic
    def order(self):
        print('the sorted dictionary by key :',(OrderedDict(sorted(self.dic.items()))))

d = {'ravi': 10, 'ram': 9, 'sanjeev': 15, 'bhanu': 2, 'lilly': 32}
create = Arrange(d)
create.order()'''

'''------------------------------------------------------------------------------------------------------------------------------------------------------'''


'''class Max:
    def __init__(self,dic):
        self.dic = dic
    def find(self):
        keymax= max(zip(self.dic.values(),self.dic.keys()))[1]
        keymin = min(zip(self.dic.values(),self.dic.keys()))[1]
        print(keymax,keymin)

vt = {'Badnews': 100, 'Goodnews': 1292, 'funnynews': 88}
a = Max(vt)
a.find()'''                                              # Get the maximum and minimum value in a dictionary.

'''--------------------------------------------------------------------------------------------------------------------------------------------------------'''



'''class Adict:
    def __init__(self,dic):
        self.dic = dic
    def var(self):
        print("The original dictionary is : " + str(self.dic))
        temp = []
        res = dict()
        for key, val in self.dic.items():
            if val not in temp:
                temp.append(val)
                res[key] = val
        print("The dictionary after values removal : " + str(res))

di = dict([('age',10),('roll',10),('number',20),('form',20)])
q = Adict(di)
q.var()      '''                                          #removing duplicate values in a dictionary
'''---------------------------------------------------------------------------------------------------------------------------------------------------------'''


'''class High:
    def __init__(self,dic):
        self.dic = dic
    def val(self):
        my_keys = sorted(self.dic, key = self.dic.get, reverse= True)[0:3]
        print(my_keys)

v = High({'A':3,'B':4,'H':1,'K':8,'T':0})
v.val()'''                              #Find the highest 3 values in a dictionary.
'''--------------------------------------------------------------------------------------------------------------------------------------------------------'''

'''class Convert:
    def __init__(self):
        self.string=input('enter the string :')
    def convert(self):
        q= dict((k, int(v)) for k,v in (e.split(' - ') for e in self.string.split(',')))
        print(q)

cl = Convert()
cl.convert() '''                                       # converting a string into a dictionary


'''def dict_depth(dic):                                   # Get the depth of a dictionary

    str_dic = str(dic)
    counter = 0
    for i in str_dic:
        if i == "{":
            counter += 1
    return(counter)

dic = {1:'kanth', 2: {3: {4: {}}}}
print(dict_depth(dic))
    


dic = {1: 'sasi', 2: {3: {4: {}}}}
print(dict_depth(dic))'''
