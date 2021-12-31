# creating a set
'''thisset = {1,2,2,3,4,4,5,6,7,8,8,9}
print(thisset)    '''                    # A set is a collection which is unordered, unchangeable,and unindexed.

'''--------------------------------------------------------------------------------------------------------------'''
'''class Set:
    def __init__(self,test):
        self.test = test
    def iterate(self):
        for val in self.test:
            print(val)
true = set('sasikanth')
cl = Set(true)
cl.iterate()   '''                         # Iteration over sets.
'''----------------------------------------------------------------------------------------------------------------'''
'''setting = set()
setting.add('ram')             # adding an element to a set
print(setting)
setting.update(['boy','child'])  # updating the elements in the set
print(setting)
setting.remove('child')   # removing a element in the set
print(setting)'''

'''--------------------------------------------------------------------------------------------------------------'''
'''setx = set(["green", "blue"])
sety = set(["blue", "yellow"])
print("Original set elements:")
print(setx)
print(sety)
print("\nIntersection of two said sets:")
setz = setx & sety
print(setz)                                # intersection of two sets
setz = setx.union(sety)
print(setz)                             # union of two sets
setz = sety.difference(setx)            # creating difference between betwwen sets
print(setz)
setz= setx.symmetric_difference(sety)
print(setz)          '''                   # creating symmetric between two sets'

'''-------------------------------------------------------------------------------------------------------------'''
'''class Maxmin:
    def __init__(self):
        self.sett= set([1,2,5,30,6,40,100])
        print('maximum and minimum values of given set',self.sett)
    def calci(self):
        print('the maximum element in set is:',max(self.sett))
        print('the minimum element in set is:', min(self.sett))

cr = Maxmin()
cr.calci()'''

'''------------------------------------------------------------------------------------------------------------'''

'''class Count:
    s= {1,2,3,4,5,6}
    def count(cls):
        le =0
        for i in cls.s:
            le+=1
        print(le)

c= Count()
c.count()'''     # counting number of elements in set