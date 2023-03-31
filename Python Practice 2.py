# print(a,end="") means print on same line for example in a For loop

# -------------------For Loop with multiple variables in an element of any iterable data structure -----------------------
list=[["islamabad","pakistan",12],["peshawar","pakistan",15],["new Delhi","india",5]]
for i,j,k in list:  # the number of variables must match the values in the element of the list. Each Corresponding value will be assigned to the variable
    print(i,"is located in",j,"with a rating of",k)

# ---------------------------------------- Comprehension For Loop -------------------------------------

countries=["Pakistan","Morocco","England","Rio","India"]
list_for_comprehension_loop=[x for x in countries if "a" not in x]
print(list_for_comprehension_loop)

# ---------------------------------------- Extend Keyword with some mistake --------------------------
list1=["a","b"]
list2=["c","d"]
list3=list2.extend(list1) # this will not work as it makes changes to original list
print(list3,"Error")
list2.extend(list1) # this will work
print(list2)

# ----------------------------------------- Checking if a variable is of particular type or not -------
x=2
y=2.0
print(isinstance(x,int))
print(isinstance(y,int))

# ------------------------------------------- Print files in a directory ----------------------------
from os import listdir
from os.path import isfile, join
for f in listdir('/home/yasir/Desktop'):
    print(f)

# ----------------------------------------- CPU count ----------------------------------------------
import multiprocessing
print(multiprocessing.cpu_count())

# ----------------------------------------- Different Elements --------------------------------------

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
not_inc=[]
for n in color_list_1:
    if (color_list_2.__contains__(n)):
        a=2
    else:
        not_inc.append(n)
print(not_inc)

# ----------------------------------------- Histogram --------------------------------------------

def histo(items):
    for n in items:
        output=''
        times=0
        if(n!=0):
            while (times < n):
                output = output + '*'
                times = times + 1
                if times == n:
                    print(output)

histo([2,3,6,0,5])

# -------------------------------------- Checking Vowel -----------------------------------------

alp=['a','e','i','o','u']
letter=input("Enter a single letter : ")
if alp.__contains__(letter):
    print("Vowel Entered !")
else:
    print("Consonant Entered !")

# ------------------------------- Print Calendar of a given year and month -----------------
import calendar
year=int(input("Enter year for a calendar "))
month=int(input("Enter month for calendar "))
print(calendar.month(year,month))


# ---------------------------- Display Time ------------------------------
import datetime
import sys
print("Current Date/Time is ",datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

# ---------------------------- Python Version -------------------------------------
print("Python version",sys.version)

# --------------------------- Calculate Area of Circle on user input ------------
from math import pi
radius=input("Enter Radius")
Area=(float(radius)**2)*pi    # a**3 mean a^3 # Area of Circle= πr2
print("Area of a circle is ",Area)


# ----------------------- Create a list/tuple from comma seperated values ----------------
comma_values=input("Enter comma seperated values")
list=comma_values.split(',')
print("List is ",list)
print("List 0 item ",list[0])
print("Tuple is ",tuple(list))

# ----------------------- find a string in a string ----------------------------------

str1="Hello this is the example of finding a string in a given string"
str2="exam"
print("The text found at: ",str1.find(str2))        # string.find(value, start_search_from, end_index)

# ------------------------- Print Extension of a file -------------------------------

filename=input("Enter filename ")
ext=filename.split(".")
print("Extension is ",ext[-1])

# ----------------------------- Print first and last element -------------------------------

color_list=["black","white","blue","yellow"]
print("First Color is ",color_list[0], " and the last color is ",color_list[-1])

# ------------------------------- Placeholders for integer------------------------------------

exam_st_date = (11,12,2014)
print( "The examination will start from : %i / %i / %i"%exam_st_date)  # "%i" is a placeholder for an integer value

# ------------------------------- Placeholders for string------------------------------------
print("The name of a file is {}".format("XYZ.java"))

# ---------------------------------- Date difference --------------------------------------------

from datetime import date
date1=date(2023,3,3)
date2=date(2022,3,30)
print("Total Gap of Days is :",abs(date2-date1))

# ------------------------------------ Occurence of a string in a string ----------------------------

occ=['1','4','1','4','9','7','4']
print("The occurance of 4 is : ",occ.count("4"))





