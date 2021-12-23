# program to multiply two integers in string form and resultant in string
def multiply(str1,str2):
    len1 = len(str1)
    len2 = len(str2)
    str1= list(map(int,reversed(str1)))
    str2 = list(map(int, reversed(str2)))
    res = [0 for i in range(len1+len2)]
    for j in range(len2):
        for i in range(len1):
            res[i+j] = res[i+j]+str1[i]*str2[j]
            res[i+j+1] = res[i+j+1] +res[i+j]//10
            res[i+j] = res[i+j]%10
    i = len(res)-1
    while(res[i]==0 and i>0):
        i=i-1
    return  ''.join(map(str,res[:i+1][::-1]))

st1= input('enter the number :')
st2= input('enter the number :')
result = multiply(st1,st2)
print(result)
print(type(result))




