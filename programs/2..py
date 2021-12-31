'''def rotate_matrix(A):
    # transposing matrix
   for i in range(len(A)):
       for j in range(i,len(A)):
           A[i][j],A[j][i] = A[j][i],A[i][j]  #  swapping the elements of opposite positions
# reversing the matrix
   N = len(A)
   for i in range(N//2):                # half of row elements considering
       for j in range(N):               # along the length of columns
           A[j][i],A[j][N-i-1]= A[j][N-i-1],A[j][i]   # swapping the the first to last and second to third positions
   return A

B =[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(rotate_matrix(B))'''

# zigzag conversion of given string
def conversion(s,n_rows):
    if(n_rows<2) :
        return s
    arr = [''for i in range(n_rows)]
    direction ='down'
    row =0
    for i in s:
        arr[row] = arr[row]+i
        if row ==n_rows-1:
            direction ='up'
        elif row==0:
            direction ='down'
        if(direction=='down'):
            row=row+1
        else:
            row=row-1
    return (''.join(arr))
p = input('enter the string :')
n = int(input('enter the no.of rows :'))
print('the zigzag conversion of given string is :',conversion(p,n))




