# Create an array of 5 integers and display the array items. Access individual element through indexes
'''from array import *
array_numbers = array('i',[1,2,3,4])
print('the array elements are :')
for i in array_numbers:
    print(i, sep='  ')
print('\n')
for j in range(0,4):
    print('th element present in index',j,'is',array_numbers[j])'''


# Append a new item to the end of the array.
'''from array import *
array_numbers = array('i',[2,4,6,8])
print('original array is:\t'+str(array_numbers))
array_numbers.append(10)
print('new array is :',array_numbers)'''

# Reverse the order of the items in the array.
'''from array import *                                    # * symbol is use to print the list elements in a single line with space
array_numbers = array('i',[2,4,6,8,10,12])
print('original array is:\t'+str(array_numbers))
#array_numbers.reverse()
#print('new array in reverse order is :',array_numbers)
x = array_numbers[::-1]
print('new array in reverse order is :',x)'''

# Get the length in bytes of one array item in the internal representation.
'''from array import *
array_numbers = array('i',[2,4,6,8,10,12])
print('Length of one array element in bytes :',array_numbers.itemsize)'''

# Get the current memory address and the length in elements of the buffer used to hold an arrays contents and also find the size
#  of the memory buffer in bytes
'''from array import *
arr =array('b',[1,4,11,2,8,34,22,56])
print('the current memory address and length in elements of buffer :',arr.buffer_info())
print('the size of memory buffer in bytes :',arr.buffer_info()[1] * arr.itemsize)'''

# Get the number of occurrences of a specified element in an array
'''from array import *
arr = array('b',[1,2,3,1,4,5,6,5])
x= arr.count(int(input('enter the number to count in the array :')))
print('the given number occured in the array',x,'times')'''

# Append items from inerrable to the end of the array
'''from array import *
arr = array('l',[1,2,3,4])
print('original array :',arr)
arr.extend(arr)
print('extended array is :', arr)
arr1 = array('l',[2,3,4,1])
arr.extend(arr1)
print(arr)'''

# Convert an array to an array of machine values and return the bytes representation
'''from array import *
print('bytes in string form:\n')
p = array('b',[98,104,97,118,121,97])
s = p.tobytes()
print(s)'''







