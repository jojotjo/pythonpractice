'''# Python Program to count the number of digits in a number.
number = int(input("enter the number: "))
#count the digits in number
count = 0
while (number>0):
    count = count + 1
    number = number//10
print("the number of digits in the number are:",count)'''

'''# Python Program to generate all the divisors of an integer
number = int(input("enter the number: "))
print("the divisiors of the number are: ")
for i in range(1,number+1):
    if(number%i==0):
        print(i)'''


'''#Python Program to find the smallest divisor of an integer.
number = int(input("enter the number: "))
a =[]
for i in range(2,number+1):
    if(number%i==0):
        a.append(i)
a.sort()
print("the smallest divisor of an integer: ",a[0])'''

'''#Python Program to find the binary equivalent of a number recursively
l = []
def convert(binary):
    if (binary==0):
        return 1
    dig=binary%2
    l.append(dig)
    convert(binary//2)
a = int(input("enter the number: " ))
convert(a)
l.reverse()
print("binary equivalent: ")
for i in l:
    print(i)'''

''' l=[]
def convert(b):
    if(b==0):
        return l
    dig=b%2
    l.append(dig)
    convert(b//2)
a=int(input("Enter a number: "))
convert(a)
l.reverse()
print("Binary equivalent:")
for i in l:
    print(i)'''


'''#Python Program to Print Binary Equivalent of a Number without Using Recursion
number = int(input("enter the number: "))
a = []
while(number>0):
        dig=number%2
        a.append(dig)
        number =number//2
a.reverse()
print("binary equivalenr is: ")
for i in a:
    print(i,end=" ")'''

'''n=int(input("Enter a number: "))
a=[]
while(n>0):
    dig=n%2
    a.append(dig)
    n=n//2
a.reverse()
print("Binary Equivalent is: ")
for i in a:
    print(i,end=" ")'''

'''#Python Program to Print Table of a Given Number
number = int(input("enter the number: " ))
for i in range(1,11):
    print(number,"x",i ,"=",number*i)'''

'''# Python Program to take in the marks of 5 subjects and display the grade.
num1 = int(input("enter the number: "))
num2 = int(input("enter the number: "))
num3 = int(input("enter the number: "))
num4 = int(input("enter the number: "))
num5 = int(input("enter the number: "))
avg = (num1 + num2 + num3 + num4 + num5) // 5
print(avg)
if (avg>=90):
    print("A")
elif (avg>=80 & avg<90):
    print("B")
elif (avg>=70 & avg<80):
    print("C")
elif (avg >=60 & avg<70):
    print("D")
else:
    print("E")'''

'''#Python Program to check if a date is valid and print the incremented date if it is
date = input("enter the date: ")
dd,mm,yy = date.split('/')
dd = int(dd)
mm = int(mm)
yy = int(yy)
if (mm==1 or mm==3 or mm==5 or mm==7 or mm==8 or mm==10  or mm==12):
           max1 = 31
elif (mm==4 or mm==6 or mm==9 or mm==11):
    max1 = 30
elif (yy%4==0 or yy%100!=0 or yy%400==0):
    max1 = 29
else:
    max1 = 28
if (mm<1 or mm>12):
    print("date is invalid")
elif (dd<1 or dd>max1):
    print("date is invalid")
elif (dd==max1 and mm!=12):
    dd = 1
    mm = mm + 1
    print("the increment date is: " ,dd,mm,yy)
elif (dd==31 and mm==12):
    dd = 1
    mm = 1
    yy = yy + 1
    print("the incremented date is: ",dd,mm,yy)
else:
    dd = dd + 1
    print("the incremented date is: ",dd,mm,yy)

'''

'''#Python Program to Year
from datetime import date
d = date.today()
e = d.strftime("%y")
print(e)
'''

'''#Python Program to Check Leap Year
year = int(input("enter the year: "))
if (year%4==0 and year%100!=0 or year%400==0):
             print("this is leap year",year)
else:
    print("this is not leap year" ,year)
'''

'''#Python Program to Convert Centimeters to Feet and Inches
cm = int(input("enter the height in centimeter: "))
inches = 0.394*cm
feet = 0.0328*cm
print("the length in inches",round(inches,2))
print("the length in feet",round(feet,2))
'''

'''#Python Program to Read a Number n and Compute n+nn+nnn
number = int(input("enter the number: "))
temp = str(number)
t1 = temp + temp
t2 = temp + temp + temp
comp = number + int(t1) + int(t2)
print("the value is: ",comp)
'''
