'''def create_adder(x):
    def adder(y):
        return x+y
    return adder
adding = create_adder(10)
print(adding(10))'''
'''-------------------------------------------------------------------------------------------------------------------------------'''

# syntax of decorater:
'''@ gfg_decorator                      # here 'gfg_decorator' is a callable function which add some code 
                                          on the top of another callable function 'hello_decorator' and return wrapper function.
def hello_decorator():
    print('sasikanth')'

 the above code is equivalent to
def hello_decorator():
    print('sasikanth')

hello_decorator = gfg_decorator(hello_decorator)'''
'''---------------------------------------------------------------------------------------------------------------------------'''
# printing addition of two numbers by using decorator toa function

'''def hello_decorator(func):
    def inner(x,y):
        print("before Execution")
        r_val =func(x,y)
        return r_val
    return inner

@hello_decorator
def sum_two_numbers(a, b):
    print("Inside the function")
    return a + b

a= int(input('enter the number :'))
b = int(input('enter the number :'))
print("Sum =", sum_two_numbers(a, b))'''
'''---------------------------------------------------------------------------------------------------------------------------'''

'''def decor1(func):                       # nested decorator
    def inner1():
        x = func()
        return x*x
    return inner1
def decor(func):
    def inner2():
        x = func()
        return 2*x
    return inner2

@ decor
@ decor1
def result():
    return 10

print(result())       # this function calling as like decor(decor1(num))'''
'''-------------------------------------------------------------------------------------------------------------------------'''
'''def parameter(func):
    def welcome(name):
        return 'welcome to th world of\t'+ func(name)
    return welcome

@ parameter
def string(person):
    return person

print(string('sasikanth'))'''
''''-----------------------------------------------------------------------------------------------------------------------'''

# decorators useful to attach data
'''def decor(func):
    func.data= 3
    return func
@ decor
def adding(x,y):
    return x+y
print(adding(2,2))
print(adding.data+adding(4,4))'''
'''---------------------------------------------------------------------------------------------------------------------------'''
'''def str_upper(func):
    def inside():
        str1= func()
        return str1.upper()
    return inside
@ str_upper
def print_str():
    return 'iam sasikanth'

print(print_str())           # changing the string to upper case'''

'''--------------------------------------------------------------------------------------------------------------------------'''
# if we want to pass parameter to decorator function
'''def outer(exp):
    def upper(func):
        def inside():
            return func()+exp
        return inside
    return upper
@ outer('sasikanth')
def function():
    return 'hello iam '
print(function())'''
'''-------------------------------------------------------------------------------------------------------------------------'''
'''def div_decorator(func):
    def inner(*args):
        list1=[]
        list1= args[1:]                    # checking if there is zero in denominators
        for i in list1:
            if i==0:
                return 'give valid input'
            return fun(*args)
        return inner

@ div_decorator
def div1(a,b):
    return a/b

@ div_decorator
def div2(a,b,c):
    return a/b/c

print(div1(10,5))
print(div2(10,10,5))'''
'''-------------------------------------------------------------------------------------------------------------------------'''
def check_name(method):
    def inner(ref_name):
        if ref_name.name =='sasikanth':
            print('my name is also same')
        else:
            method(ref_name)
    return inner

class Print:
    def __init__(self):
        self.name = input('enter the name :')
    @ check_name
    def print_name(self):
        print('entered user name is :', self.name)

p = Print()
p.print_name()





