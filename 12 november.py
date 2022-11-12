#find sum of numbers from 1 to n 
#find out the sum of numbers from 1 to n like 1+2+3+4+, etc
 
a=int(input("Enter the value of n:"))
s=0
for i in range(1,a+1):
    s+=i
print("sum is:",s)

#reverse a string
a=input("Enter the string:")
for i in range(1,len(a)+1):
    print("Reversed string is ",a[-i],end="")

#Adding all numbers in a list 

a=eval (input("Enter the list:"))
s=0
for i in a:
    s+=i
print("Sum of elements is:",s)


#python practice question 
#1 we need to write a python program to find the power of a number using recursion 
#input:num=2, power=3
#output:8

a=int(input("Enter the number:"))
b=int(input("Enter the power:"))
p=a
for i in range(1,b):
    p=p*a
print(a,"^",b,"=",p)

#2 assign a diffferent name to function and call it through the new name 

def display_student(name,place):
    print(name,place)
display_student("ARZOO","HARYANA")
showstudent  = display_student
showstudent("ARZOO","HARYANA")

#3Python Program to print all odd numbers in a range
a=int(input("Enter the lower limit:"))
b=int(input("Enter the upper limit:"))
s=0
for i in range(a,b+1):
    if i%2==0:
        continue
    else:
        s+=i
print("Sum of all odd numbers between",a,"and",b,"is:",s)


#4 python program to check whether a given number is even or odd using recursion

a=int(input("Enter the number:"))
o=True
for i in range(1,a):
    if i**2==a:
        o=False
        print("Even number")
        break
    else:
        o=True
if o==True:
    print("Odd number")

#5 python program to check wheather a number is prime or not using recursion

a=int(input("Enter the number:"))
p=True
if a==1:
    print(a,"is neither prime nor composite")
elif a==2:
    print(a,"is a prime number")
else:
    for i in range(2,a):
        if a%i==0:
            print(a,"is a composite number")
            p=False
            break
        else:
            p=True
if p==True:
    print(a,"is a prime number")

#6 python program to print all integers that aren't divisible by either 2or3
a=int(input("Enter the lower limit:"))
b=int(input("Enter the upper limit:"))
for i in range(a,b+1):
    if i%2==0 or i%3==0:
        continue
    else:
        print(i,end=",")

#7 pyhton program to check if a number is a palindrome
a=int(input("Enter the number"))
b=str(a)
p=True 
for i in range (0,len(b)):
    if b[i]==b[-(i+1)]:
        p=True
    else:
        p=False
        break 
if p==True:
    print(a,"is a palindrome number ")
else:
    print(a,"is not a plaindrome number")

#8 python program to count the number of vowels in a string
a=input("Enter the string :")
b="aeiouAEIOU"
count=0
for i in a:
    if i in b:
        count+=1
    else:
        continue
print("Number of vowels in",a,"are:",count)

#9 python program to remove odd indexed characters in a string
a=input("Enter the string:")
b=""
for i in range(0,len(a)):
    if i%2==0:
        b+=a[i]
    else:
        continue
print(b)

#10 python program to remove the nth index character from a non-empty string
a=input("Enter the string:")
b=int(input("Enter the value of n:"))
s=""
for i in a:
    if i==a[b]:
        continue
    else:
        s+=i
print(s)

#11 python program replace every blank space with hyphen in a string
a=input("Enter the string:")
b=" "
s=""
for i in a:
    if i==b:
        s+="-"
    else:
        s+=i
print(s)

#12 python program to calculate the length of a string without using library functions

a=input("Enter the string:")
count=0
for i in a :
    count+=1
print("Length of the string",a,"is:",count)

#13 python program to  count the number of lowercase character in a string
a=input("Enter the string:")
count=0
for i in a:
    if i.isupper():
        continue
    else:
        count+=1
print("No of lowercase character in the string",a,"is:",count)

#14 python program  to count the number of vowels in a string
a=input("Enter the string:")
b="aeiouAEIOU"
count=0
for i in a:
    if i in b:
        count+=1
    else:
        continue
print("Number of vowels in",a,"is:",count)

#15python program  to count number of upercase and loweercase letters in a string

a=input("Enter the string:")
u=0
l=0
for i in a:
    if i.isupper():
        u+=1
    elif i.islower():
        l+=1
print("Number of lowercase letters are:",l)
print("Number of uppercase leeteters are:",u)

#16 python program to find comman charcters in two strings 
a=input("Enter the first string:")
b=input("Enter the second string:")
for i in a:
    if i in b:
        print(i,end="")
    else:
        continue

#17 string palindrome program in python 
a=input("Enter the string:")
p=True 
for i in range(0,len(a)):
    if a[i]==a[-(i+1)]:
        continue
    else:
        p=False
        break
if p==True:
    print(a,"is a palindrome number")
else:
    print(a,"is not a palindrome number")

#18 pyhton program to determine how many times a given letter occurs in a string recursively
a=input("Enter the string:")
b=input("Enter the character  to check:")
count=0
for i in a:
    if i==b:
        count+=1
print("Number of times",b,"has occured in",a,"is:",count)








