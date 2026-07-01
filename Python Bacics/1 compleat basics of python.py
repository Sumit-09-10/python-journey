#Basics 
print("Hallow world")

# Arithematic oprator
#let 
a=4
b=6
print(a+b)     # gives addition 
print(a-b)     # gives subtraction
print(a*b)     # gives multipication
print(a/b)     # gives divition
print(a% b)    # gives remainder 
print(a**b)    # gives a^b

# relational oprator
print(a==b)
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)


# practice 
name=input("Enter your name :" ,)
p=int(input("Enter your phy marks :" ,))
c=int(input("Enter your chem marks :" ,))
m=int(input("Enter your maths marks :" ,))
print("Your name is :" ,name )
print("Your phy marks is : " , p )
print("Your chem marks is: " , c)
print("Your maths marks is :", m)
x=int(p+c+m)
print("obtain marks :" , x) 
print("Avg marks :" , x/3)            # gives avg of pcm

# strings 
str1="Sumit"
str2="Harkal"
print(str1+str2)                           # returns  SumitHarkal
print(str1+ " " + str2)                    # returns  Sumit Harkal
print(len(str1))                           # returns  5
print(len(str2))                           # returns  6

str="sumit harkal"
print(str[0])                              # returns  s
print(str[1])                              # returns  u
print(str[2])                              # returns  m
print(str[2:5])                            # returns  mit 
print(str[:10])                            # returns  sumit hark
print(str[5:10])                           # returns   harkal
print(str[3:])                             # returns  it harkal
print(str[-12:-7])                         # returns  sumit

#some meathods
print(str.endswith("kal"))       # gives true 
print(str.capitalize())          # returns  Sumit harkal
print(str.replace("a" , "aa"))   # returns  sumit haarkaal                 

# conditionls IF / ELSE
y =int(input())
if (y>0):
    print("it is a positive no" )
if (y==0):
    print("its 0")
if (y<0):
    print("it is a negative no" )            


#Lists 
marks=[87,85,64,64,84,15,56,65,45]
print(len(marks))                        # returns    9

print(marks[0])                          # returns    87
print(marks[1])                          # returns    85
print(marks[2])                          # returns    64
print(marks[2:5])                        # returns    [64,64,84]
print(marks[:8])                         # returns    [87,85,64,64,84,15,56,65]
print(marks[5:8])                        # returns    [15,56,65]
print(marks[3:])                         # returns    [64,84,15,56,65,45]
print(marks[-9:-3])                      # returns    [87,85,64,64,84 ,15]

student=["sumit", 93 , 2 , "parbhani"]
print(student)                           # returns    [sumit , 93 , 2 , parbhani
student[0]="rajveer"                     # it repaces [sumit
print(student)                           # returns    [rajveer , 93 , 2 , parbhani
#some meathods
#let
list=[2,1,3]                             
list.append(4)                           # it adds 4in list at last
print(list)                              # returns [2, 1, 3, 4]
list.sort()                              # returns list in assending order
print(list)                              # returns [1, 2, 3, 4]
list.sort(reverse=True)                  # returns list in desending order
print(list)                              # returns [4, 3, 2, 1]

# Tuples
tup=[87,85,64,64,84,15,56,65,45]
print(len(tup))                            # returns 9

print(tup[0])                              # returns 87
print(tup[1])                              # returns 85
print(tup[2])                              # returns 64
print(tup[2:5])                            # returns [64, 64, 84]
print(tup[:8])                             # returns [87, 85, 64, 64, 84, 15, 56, 65]
print(tup[5:8])                            # returns [15, 56, 65]
print(tup[3:])                             # returns [64, 84, 15, 56, 65, 45]
print(tup[-9:-3])                          # returns [87, 85, 64, 64, 84, 15]

#some meathods

print(tup.index(85))                       # returns  1
print(tup.index(64))                       # returns  2

print(tup.count(64))                       # returns  2
print(tup.count(65))                       # returns  1

# dictionary 
dict={
    "name":"sumit" ,
    "class":"frst year",
    "marks":"92" ,
}

print(dict)                 # returns {'name': 'sumit', 'class': 'frst year', 'marks': '92'}

print(dict["name"])         # returns  sumit
print(dict["class"])        # returns  frst year
print(dict["marks"])        # returns  92

dict["name"] = "rajveer"                
print(dict)                 # returns  {'name': 'rajveer', 'class': 'frst year', 'marks': '92'}


# LOOPS
# while loops

i=1
while i<=5:
    print("Hi")
    i+=1

# print no 1 to 100

i=1
while i<=100 :
    print(i)
    i+=1

# print no 1 to 100

i=100
while i>=1 :
    print(i)
    i-=1

# print multiplication table of no n 

i=1
while i<=10 :
    print(3*i)
    i+=1

# example 

i=1
while i<=10 :
    print(i**2)
    i+=1

# key words

i=1
while (i<=5) :
    print(i)
    if (i==3):
        break
    i+=1

i=0
while (i<=5) :
    if (i==3):
        i+=1
        continue
    print(i)
    i+=1

# FOR LOOPS 

list= [1,2,3,4,5,6,7]
for x in list :
    print(x)

str = "sumit"
for x in str: 
    print (x)

seq= range(5)

for i in seq :
    print(i)

# ex

for i in range(10):
    print(i)

for i in range(2,10):
    print(i)

for i in range(2,10 ,2):
    print(i)

for i in range(2,10 ,3):
    print(i)

for i in range(2,101 ,2):
    print(i)

for i in range(1,101 ,2):
    print(i)

for i in range(100,0 ,-1):
    print(i)


# Functions 
def sum(a,b):
    s=a+b
    print(s)
    return sum

print(sum(3,4))

# EX qudratic eqn 

def qe(a,b,c):
    x=(-b+(b**2-4*a*c)**1/2)/2*a
    y=(-b-(b**2-4*a*c)**1/2)/2*a
    print("First root of eqn is :" , x)
    print("second root of the eqn is: " , y)
    return qe

print(qe(405,46,1))

list1 =[1,2,3,4,5,6,]
list2 =[56,1,8,2,4,8,5,5,9,65,5,5,5,5,5,55]
def out_len(list):
    print(len(list))
    
out_len(list1)
out_len(list2)



def nature(a):
    if a%2==0:
        print("even")
    if a%2==1:
        print("odd")

nature(117)

#ZIP Function
list1=["sumit" , "yash" , "bhagwan"]
list2=[20, 15, 51]
print(list(zip(list1,list2)))

# [('sumit', 20), ('yash', 15), ('bhagwan', 51)]


mat=[(1,2,3),(4,5,6),(7,8,9)]
print([list(row) for row in zip(mat)])
print(mat)

#[[1, 4, 7], [2, 5, 8], [3, 6, 9]]


mat=[(1,2,3),(4,5,6),(7,8,9)]
print([list(row) for row in zip(*[list(row) for row in zip(*mat)])])

# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


mat=[(1,2,3),(4,5,6),(7,8,9)]
a=([list(row) for row in zip(*mat)])
b=([list(row) for row in zip(*[list(row) for row in zip(*mat)])])
print(b)

# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


list1=[1,2,3]
list2=[4,-5,6]
a=([l1*l2 for l1,l2 in zip(list1,list2)])
print(a)
print(sum(a))

# [4, -10, 18]
# 12



##Filter function

l1=[5,9,6,7,4,7,5,6,7,5,7,8,5,1]
def true(x):
    return x%2==0
print(list(filter(true,l1))) 

# [6, 4, 6, 8]


## LAMBDA FUNCTION

a= lambda x,y: x*y 
print(a(5,2))

# 10

##Map
num=[1,2,3,4,5,6,7,8,9]
def sqr(x):
    return x**2
print(list(map(sqr,num)))

# [1, 4, 9, 16, 25, 36, 49, 64, 81]


# Recursion
def show (n):
    if(n==0):
        return
    print(n)
    show(n-1)

show(9)

def show (n):
    if(n==-1):
        return
    print(n)
    show(n-1)

show(9)


# FILE I/O
f=open("data.txt","r")
data=f.read()
print(data)
f.close()

# Python is powerful.
# File handling is essential.
# Practice makes perfect.
# Learning programming is fun.



f=open("data.txt")
for i in range (1,5,1):
    print(f"{i} : {f.readline()}")
f.close

# 1 : Python is powerful.

# 2 : File handling is essential.

# 3 : Practice makes perfect.

# 4 : Learning programming is fun.


f=open("data.txt","a")
f.write("\nConsistency builds mastery.")
f.close()
f=open("data.txt","r")
print(f.read())
f.close()

# Python is powerful.
# File handling is essential.
# Practice makes perfect.
# Learning programming is fun.
# Consistency builds mastery


print("Write the 3 sentenses below to appent in data.txt")
s1=input("Sen 1")
s2=input("Sen 2")
s3=input("Sen 3")
f=open("data.txt","a")
f.write(f"\n{s1}\n{s2}\n{s3}")
f.close()
f=open("data.txt")
print(f.read())
f.close()

# Write the 3 sentenses below to appent in data.txt
# Sen 1 Discipline creates results.
# Sen 2 Small steps lead to big success.
# Sen 3 Never stop improving.
# Python is powerful.
# File handling is essential.
# Practice makes perfect.
# Learning programming is fun.
# Consistency builds mastery.
# Discipline creates results.
# Small steps lead to big success.
# Never stop improving.


file = open("data.txt", "r")

text = file.read()

# Count characters
characters = len(text)

# Count lines
lines = text.split("\n")
number_of_lines = len(lines)

# Count paragraphs
paragraphs = text.split("\n\n")
number_of_paragraphs = len(paragraphs)

# Count words
words = text.split()
number_of_words = len(words)

file.close()

print("Characters:", characters)
print("Lines:", number_of_lines)
print("Paragraphs:", number_of_paragraphs)
print("Words:", number_of_words)

# Characters: 211
# Lines: 8
# Paragraphs: 1
# Words: 29




# "r"                 open for reading
# "w"                 opens the file erases it first and writes
# "x"                 creat a new file and open it for writing
# "a"     (apends)    open for writing after the data writen in file  ,, apending at the end
# "b"                 binory mode
# "t"                 text mode (default)
# "+"                 open for writing (reading or writing )


#OOPs 
class car:
    color = "blue"
    brand# = "mercedes"

car1 = car()

print (car1.color)
print (car1.brand)


class student :
    name = "sumit"

s1 = student()
print(s1.name)

s2 = student()
print(s2.name)



class student :
    def __init__(self ,name):
        self.name = name 
        print ("adding new student in database ")

s1 = student("sumit")
print(s1.name)



class student :
    def __init__(self ,name , marks):
        self.name = name 
        self.marks =marks
        print ("adding new student in database ")

s1 = student("sumit" , 92)
s2 = student("yash" , 99)

print(s1.name)
print(s1.marks)
print(s1.name , s1.marks)

print(s2.name)
print(s2.marks)
print(s2.name , s2.marks)

print(s1.name , s2.marks)



class student :
    def __init__(self, name,phy, chem , maths):
        self.name = name 
        self.sub1 =phy
        self.sub2 =chem
        self.sub3 =maths
s1 = student("sumit" , 92  ,6 ,45)
s2 = student("yash" , 99 ,54 ,94)

print(s1.name , s1.sub1 ,s1.sub2 ,s1.sub3)
print(s2.name , s2.sub1 ,s2.sub2 ,s2.sub3)
