# creating a tuple
'''thistuple = ('apple', 1, [2.5,'ram'])
print(type(thistuple))'''

'''----------------------------------------------------------------------------------------------------------------'''
# creating atuple with numbers and printing one of them
'''tuplex = 5,10,100,3
print(tuplex)
print(tuplex[2])'''

'''------------------------------------------------------------------------------------------------------------'''
'''from copy import deepcopy

# by using deepcopy() any changes made to a copy of object do not reflect in the original object

tuplex = ("HELLO", 5, [], True)
print('normal tuple',tuplex)
tuplex_colon = deepcopy(tuplex)
tuplex_colon[2].append(50)         # copy of tuplex created in tuplex_colon and in the 3rd element we are appending integer 50
print(tuplex_colon)
print(tuplex)'''
'''-------------------------------------------------------------------------------------------------------------'''
 #remove an item from a tuple
'''tuplex = 's','a','s','i','k','a','n','t','h'
print(tuplex)
tuplex1 = tuplex[:2] + tuplex[3:]
print(tuplex1)
list1 = list(tuplex)
list1.remove('k')
tuplex = tuple(list1)
print(tuplex)'''

'''------------------------------------------------------------------------------------------------------------'''
'''class Tuple:
    def __init__(self,tu1,tu2):
        self.tu1 = tu1
        self.tu2 = tu2
        print("The original key tuple is : " + str(tu1))
        print("The original value tuple is : " + str(tu2))
    def convert(self):
        if len(self.tu1) == len(self.tu2):
            res = dict(zip(self.tu1,self.tu2))
        print("Dictionary constructed from tuples : " + str(res))


tup1 = ('sasi', 'roll', 'category')
tup2 = (1, 2, 3)
tuple = Tuple(tup1,tup2)
tuple.convert()    '''                    # convert a tuple to a dictionary

'''--------------------------------------------------------------------------------------------------------------'''
#  unzip a list of tuples into individual lists.
'''li = [(1,2), (3,4), (8,9)]
print(list(zip(*li)))'''


