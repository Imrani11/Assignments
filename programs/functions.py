#check given word is palindrome or not
'''class Palindrom:
     def __init__(self):
         self.name = input('enter the name please to check for palindrome :')
     def check(self):
         answer = self.name[::-1]
         if self.name==answer:
             print('yes its palindrome')
         else:
             print('this is not palindrome')

sup = Palindrom()
sup.check()'''
'''--------------------------------------------------------------------------------------------------------------'''

# print even and odd numbers

'''class Check:
    def __init__(self):
        self.number = int(input('enter your to check:'))
    def count(self):
        if (self.number%2)==0:
            print('this is even')
        else:
            print('this is odd')

cu = Check()
cu.count()'''

'''--------------------------------------------------------------------------------------------------------------'''

# printing prime numbers between 10 to 50

'''class Prime:
    start = 10
    end = 50
    def calculate(cls):
        for i in range(cls.start,cls.end+1):
            if i>1:
                for j in range(2,i):
                    if(i%j==0):
                        break
                else:
                     print(i)

pr = Prime()
pr.calculate()'''

'''---------------------------------------------------------------------------------------------------------------'''
# factorial of given number
'''class Factorial:
    def __init__(self):
        self.num = int(input('enter the number for factorial:'))
    def fact(self,factorial):
        if self.num<0:
            print('factorail cannot be given for -ve values')
        elif  self.num==0:
            print('the factorial for 0 is 1')
        else:
            for i in range(1,self.num+1):
                factorial = factorial*i
            print('the factorail of given number',self.num,'is',factorial)

facti =Factorial()
facti.fact(1)'''

'''--------------------------------------------------------------------------------------------------------------'''
# to find the square and cube of given number
'''class Sc:
    def __init__(self):
        self.num = int(input('enter the number'))
    def square(self):
        return self.num**2
    def cube(self):
        return self.num**3

s = Sc()
print('square of the number',s.square())
print('cube of the number',s.cube())'''

'''--------------------------------------------------------------------------------------------------------------'''

# table of the given number
'''class Table:
     def __init__(self):
         self.num = int(input('enter the number :'))
     def table(self,count):
         while count<=10:
             self.num =self.num*1
             count+=1
             print(self.num,'x',count,'=',self.num*count)

tab = Table()
tab.table(1)'''
'''-------------------------------------------------------------------------------------------------------------'''
# to find the maximum of given three numbers
'''class Max:
    def __init__(self):
        self.a = int(input('enter the number a :'))
        self.b = int(input('enter the number b :'))
        self.c = int(input('enter the number c :'))
    def max(self):
        if self.a>=self.b and self.a>=self.c:
            print('the largest is %d'%self.a)
        elif self.b>=self.a and self.b>=self.c:
            print('largest number is %d '%self.b)
        else:
            print('largest number is %d'%self.c)

max_of_three = Max()
max_of_three.max()'''

'''-------------------------------------------------------------------------------------------------------------'''

# fibonacci series
'''class Fibbonacci:
    def __init__(self):
        print('fibonacci series for given series')
        self.num = int(input('enter the number of terms :'))
    def terms(self,n1,n2,count):
        if self.num<=0:
            print('enter positive number :')
        elif self.num==1:
            print('Fibonacci sequence upto',self.num, ':',end='')
            print(n1)
        else:
            while count<self.num:
                print(n1)
                num = n1+n2
                n1=n2
                n2=num
                count+=1

fib = Fibbonacci()
fib.terms(0,1,0)'''

'''---------------------------------------------------------------------------------------------------------------'''
# sum and product of all numbers in a list
'''class Sumprod:
    def __init__(self,li):
        self.li=li
    def sum(self,total):
        for i in range(0,len(self.li)):
            total = total+self.li[i]
        print("Sum of all elements in given list: ", total)
    def product(self,tot):
        for i in range(0, len(self.li)):
            tot = tot*self.li[i]
        print("product of all elements in given list: ", tot)

find = Sumprod([2,3,5])
find.sum(0)
find.product(1)'''
'''--------------------------------------------------------------------------------------------------------------'''
# check whether a number is in a given range
'''class Range:
     def __init__(self):
         self.n = int(input('enter the number :'))
     def sequence(self,num):
            if self.n in range(0,num):
                  print('yes the number is in the range')
            else:
                  print('the number is out of range')

call = Range()
call.sequence(7)'''
'''------------------------------------------------------------------------------------------------------------'''
# print the even numbers from a given list
'''class List:
     def __init__(self,lis):
         self.lis = lis
         print('the given list is :',self.lis)
     def func(self):
         for num in self.lis:
             if num%2==0:
                print(num)
ci = List([2, 4, 5, 9, 10])
ci.func()'''
'''-------------------------------------------------------------------------------------------------------------'''
# program to reverse a string

'''class String:
    def __init__(self):
        pass
    def reverse(self):
        step= ''
        for word in words:
            step = word+step
        print('the reverse order for given string is :',step)

words = input('enter your string :')
run = String()
run.reverse()'''

'''------------------------------------------------------------------------------------------------------------'''
# calculating no .of upper and lower case letters in given string
'''class Ul:
    def __init__(self):
        self.string = input('enter the string :')
    def uplo(self):
        upper = 0
        lower = 0
        for c in self.string:
            if c.isupper():
                upper= upper+1
            elif c.islower():
                lower = lower+1
            else:
                pass
        print('the string is :',self.string)
        print('total upper case characters  :',upper)
        print('total lower case characters  :',lower)

char = Ul()
char.uplo()'''

'''------------------------------------------------------------------------------------------------------------'''
 # takes a list and returns a new list with unique elements of the first list.
'''class Unique:
    def __init__(self,li):
        self.li = li
        print('the original list is :',self.li)
    def level(self):
        empty=[]
        for i in self.li:
            if i not in empty:
                empty.append(i)
        print('the new list created is :',empty)

integer = Unique([1,2,2,3,4,5,5,6])
integer.level()'''
'''-------------------------------------------------------------------------------------------------------------'''
# pascals traingle:
'''from math import factorial
class Pascal:
    def __init__(self):
        self.n = int(input('enter the sequence terms :'))
    def fact(self):
        for i in range(self.n):
            for j in range(self.n-i+1):
                print(end=' ')
            for j in range(i+1):
                print(factorial(i) // (factorial(j) * factorial(i - j)), end=" ")
            print()

triangle = Pascal()
triangle.fact()'''
'''-------------------------------------------------------------------------------------------------------------'''
  # function to check whether a string is a pangram or not
'''import string

class Panagram:
    def __init__(self):
        self.stringg = input('enter your sentence :')
    def check(self,alphabet = string.ascii_lowercase):
        alphaset = set(alphabet)
        return alphaset<=set(self.stringg.lower())

st = Panagram()
print(st.check())'''



