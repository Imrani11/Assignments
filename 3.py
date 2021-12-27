'''def pascal_triangle(M):                    # total no.of inputs to form triangle
    a= [[]for i in range(M)]
    for i in range(M):
        for j in range(i+1):                 # whenever row increases columns needs to be incremented
            if (j<i):
                if(j==0):
                    a[i].append(1)
                else:
                    a[i].append(a[i-1][j]+a[i-1][j-1])
            elif (j==i):
                a[i].append(1)
    print(a)
    for p in range(M):
        for q in range(M-p-1):
            print(' ',end='')
        for q in range(p+1):
            print(a[p][q],end=' ')
        print()

S= int(input('enter the number of terms :'))
print('the pascal triangle formed is :',pascal_triangle(S))'''
'''---------------------------------------------------------------------------------------------------------------------------'''
'''def heart_shape(R,C):
    print('the heart shape required is :')
    for row in range(R):
        for col in range(C):
            if (row==0 and col%3!=0) or (row==1 and col%3==0) or (row-col==2) or (row+col==8):
                print('*',end='')
            else:
                print(' ',end='')
        print()
A = int(input('enter the no.of rows :'))
B =int(input('enter the no.of columns :'))
heart_shape(A,B)'''
