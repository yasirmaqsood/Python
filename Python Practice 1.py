# -*- coding: utf-8 -*-

# -- Editor --

print("Hello from Datalore!")

x="What is this"
test="he","l","lo"
print(test)

test=["a","b","c"]
type(test)
x=test
y=test
print(x[0]+"\n"+y[1])

global u
def myfunc():
    global y
    y="Internal"
myfunc()
print(y)

a=5
b="5" 
c="1","2","3" #Tuple
d=("1","2","3") #Tuple
e=["1","2","3"] #List : A list can contain different data types:
f={"Name":"Yasir","Job":"JRO"} #Dictionary
g=False
h=range(10)
i=memoryview(bytes(5))

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i))

print(f.values)
j=str(a)
print(j)
print((type(j)))

import random
print(random.randrange(0,10))

td=3.0
hg=int(td)
print(hg)

bh="""  this is a multiline test
    where a string value is 
    assigned using 3 quotes, and its over  """
print(bh)

if "6h" in bh:
    print("Present")
else :
    print("NOt Present")

print(bh[5:19])
print(bh[:19])
print(bh[:-6])

jh=bh.upper()
print(jh)
print(jh.lower())

#strip() removes whitespaces from start and end
print(bh.split(","))

print(bh.split(","))

#This is used to concatenate string and int using placeholder and then usig format() method
age=26
sal=74
yasir="My age is {} and sal is {}"
print(yasir.format(age,sal))

#This is used to concatenate string and int using placeholder and then usig format() method by using index
age=26
sal=75
yasir="My sal is {1} and age is {0}"
print(yasir.format(age,sal))

#Escape Character
string="we are the \"Developers\" of CRDC"
print(string)
string="we are the \nDevelopers of CRDC"
print(string)

kl=bh.strip()
print(kl.capitalize())
print(kl.casefold()) #Converts to lowercase
print(kl.count("is")) #Counts an occurance of specified word in a string
print(kl.find("assigned")) #Finds the word and returns its position
print((kl.islower()))
print((kl.rfind("is"))) #Searches the string for a specified value and returns the last position of where it was found
e.append("Appended_value") #Append to LIST
print(e)

if kl.endswith("ove"):
    print("Ends with over")
else:
    print("Does not end with over")

x = 200
y=20.9
print(isinstance(x, int)) #Check if an object is an integer or not:
print(isinstance(y, int))

print(e[-1])
print(e[1:6]) #The search will start at index 2 (included) and end at index 6 (not included).
print()

e[2]="Frog","Bat"
print(e)

e.insert(0,"First Element")
e.append("Last Element")
print(e)

list1=["Apple","Peach"]
list2=["Orange","Grape"]
tuple1=("Cherry","Banana")
list1.extend(list2) #To append elements from another list to the current list, use the extend() method.
print(list1)

list1.extend(tuple1) #The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
print(list1)

list1.append("Cherry")
print(list1)
list1.remove("Cherry")
print(list1)

list1.insert(0,"Apple")
print(list1)
list1.pop(0) #The pop() method removes the specified index.
print(list1)

list1.pop() #If you do not specify the index, the pop() method removes the last item.
print(list1) 

list1.clear() #Empties the list
del list1[0] #Deletes specified item
del list1 #Deletes the list

length=len(list1)
print(length)

for x in list1:
    print(x)

for x in range(length):
    print(list1[x])

[print(x) for x in list1] #Comprehension for loop

i=0
while i < length:
    print(list1[i])
    i=i+1

#List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
mylist=["America","Pakistan","Sweden","Rio","Germany","Belgium"]
list_without_a=[x for x in mylist if "a" not in x]
print(list_without_a)

list_with_upper=[x.upper() for x in mylist]
print(list_with_upper)

list_with_upper.sort()
print(list_with_upper)

list_with_upper.sort(reverse=True) #Sort the list descending:
print(list_with_upper)

list_without_a.reverse() #reverse the order of a list, regardless of the alphabet
print(list_without_a)

#A tuple is a collection which is ordered and unchangeable.
myTuple=("apple",) #This is a tuple with single item. NOTE: Remember to put a comma at the end for a single item tuple

#Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called
firstTuple=("First","Second","Third")
print(firstTuple)
tuple_converted_to_list=list(firstTuple) #Convert tuple to List to make changes
tuple_converted_to_list.append("New Item added")
print(tuple_converted_to_list)

back_to_tuple=tuple(tuple_converted_to_list)
print(back_to_tuple)

