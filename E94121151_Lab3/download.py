a = input("please input a number: ")
if int(a)//2==0:
    print('this is even')
else:
    print('this is odd')
b=input("please input your student ID first character: ")
c=input("please input your student ID last 8 numbers: ")
if int(c)//2==0:
    print('your student ID number is even')
else:
    print('your student ID number is odd')
print('your student ID number is:'+b+c)