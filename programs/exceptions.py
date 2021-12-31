'''def division(a, b):
    try:
        print(a/b)
    # if the error occurs, handle it !!
    except ZeroDivisionError as ze:
        print("Cannot divide by Zero!!",ze)
	# if no error occurs
    else:
        print("No Error occured!!")

division(10,2)
division(10,0)'''

'''--------------------------------------------------------------------------------------------------------------'''
# program to divide two numbers using exception handling

'''def division(a, b):
    # use the try statement where error may occur
    try:
        print(a/b)
    # if the error occurs, handle it !!
    except ZeroDivisionError:
        print("Cannot divide by Zero!!")
    else:
        print("No Error occured!!")
    finally:
        print('Value of a', a, 'and b', b)

division(10,0)  
division(10,2)'''

'''------------------------------------------------------------------------------------------------------------'''
'''import pandas as pd

# create a list to store the dataframes
dataframe_list = []

# iterate through folder 1 to 34
for folder in range(1, 35):
    # try we are able to read the file
    try:
        ### notice that for folder i, we have file name "region_i"
        ### create the file name
        file_name = 'region_' + str(folder) + '.csv'

        ### read the file if possible
        data = pd.read_csv('dataset/' + str(folder) + '/' + file_name)
        dataframe_list.append(data)

    # if any error occurs, skip this step and continue reading other files.
    except FileNotFoundError:
        print('File not found!!', file_name)

    # If any other error occurs, print the file name
    except Exception as e:
        print('Another Error!!', e)
        continue'''
'''--------------------------------------------------------------------------------------------------------------'''

'''amount = int(input('enter amount :'))
try:
    if amount<1000:
        print('please check your balance')
    else:
        print('sorry we have insufficient funds')

except SyntaxError as se:
    print('please follow the syntax',se)

else:
    print('no error found')

finally:
    print('the amount asked is :',amount)'''



