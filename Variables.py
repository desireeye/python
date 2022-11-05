#workimg with strings

#slice a string x[startIndex : endIndex]

x="ARZOONAIN"
print(x[1:6])
print(x[:6]) #if we want it to start from the starting 
print(x[3: ]) #frm thr index to last element
print(x[-4:-2])#indexing from back 

#modify the strings 

x="my name is arzoo nain"
print(x.upper()) # all the letter in uppercase 
print(x.lower())#all the letter in lowercase
 
splittedText=x.split()
print(splittedText[2])# it separates the word of the sentance

#replace a string with another one

x="arzoo nain"
print(x.replace("a","z"))

#addinig  two strings 
x="arzoo"
y="nain"
print(x+y)
 
 
 #booleans
  
  #true or false

print(23>11)
print(22==11)
print(30<19)
#exceptions for bool 
#1.. almost any kind of value will reasult  in true  if it has some comotent
#2..any stirng passed is true except empty string
#3..any number passed true except 0
#4..any list tuple dictionary will result in true except the empty ones

#python lists

#creating list 
#1..simple way 
mylist=[1,2,3,"arzoo","nain"]
print(mylist)
#length of list
print(len(mylist))
#2..using a list constructor 
mylist=list((1,2,3,55))
print(mylist)
#access list items
mylist=[10,34,53,"false","arzoo"]
print(mylist[4]) #selcting a single element
print(mylist[-4]) #indexing from backside 
print(mylist[1:5]) #a set of elements 

#changing  the value at a index 
mylist=[10,20,30,40,50]
mylist[3]=4735
mylist[2:4]=[234,834]
print(mylist)
#insewrting a new items
#1..using insert 
my_list=[10,20,30,40]
my_list.insert(4,60)
print(my_list)

#3..using extend function 
list1=[1,2,3]
list2=[4,5,6]
list1.extend(list2)
print(list1)
print(list2)



#remove  list items
#1..remove by elment
mylist=[1,2,3,4,3]
mylist.remove(3)
print(mylist)
#2..remove by index using pop
mylist.pop(2)#if we don't pass any index here then it remove the last element
print(mylist)
