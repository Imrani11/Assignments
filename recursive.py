'''def factorial(num):
    if num==1:
        return num
    else:
        return(num*factorial(num-1))

x = factorial(int(input('enter the number')))
print('the factorial of given number is',x)     '''       # factorial of given number using recursive function

'''def recursive(num):
    if num<=1:
        return num
    else:
        return(recursive(num-1)+recursive(num-2))

n = int(input('enter the terms'))
if n<=0:
    print('enter a positive value')
else:
    print('the fibonacci series:')
    for i in range(n):
        print(recursive(i))'''                             # fibonacci series using recursive function

'''def count_down(start):
    if start<0:
        print('enter a positive number')
    else:
        print(start)
        next = start-1
        if next>0:
            count_down(next)
print('the required countdown is :')
count_down(int(input('enter the number')))'''             # countdown of numbers

'''def count(num):
    if num>0:
        return num+count(num-1)
    else:
        return 0
result = count(int(input('enter the number :')))
print(result)'''                                          # counting the sequence of numbers of given range

'''def pattern(num):
    if num<=0:
        print(num)

    else:
        print(num)
        print(pattern(num-5))

n = int(input('enter the number'))
pattern(n) '''                                    # printing the numbers in 10 5 0 sequence from 10



