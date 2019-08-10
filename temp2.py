#calculate the area and the perimeter of the rectangle

a=int(input("enter the value of a"))
b=int(input("enter the value of b"))
area=a*b
perimeter=2*(a+b)
print("area of the rectangle",area)
print("perimeter of the rectangle",perimeter)


#calculate the area of the triangle
import math as m
a=int(input("enter the value of a"))
b=int(input("enter the value))alue of b"))
c=int(input("enter the value of c"))
s=(a+b+c)/2
area=m.sqrt(s*(s-a)*(s-b)*(s-c))
print("area of the triangle is :",area)

#calculate simple interest
p=int(input("enter the principle"))
r=int(input("enter the rate"))
t=int(input("enter the time"))
simple_interest=(p*r*t)/100
print("simple interest is",simple_interest)


#swap two variable using third variable
a=int(input("enter the number"))
b=int(input("enter the number"))
c=a
a=b
b=c
print("number in a:",a)
print("number in b:",b)

#swap two variable without third variable
a=int(input("enter the number"))
b=int(input("enter the number"))
a=a+b
b=a-b
a=a-b
print("number in a:",a)
print("number in b:",b)


#reverse of a number
a=int(input("enter the number"))
b1=a%10
b2=a//10
b=b1*10+b2
print("reverse of a number:",b)

#check wheather a character is in upper case or in lower case
a=input("enter the character:")
print(a.isupper())

#convert lower case into upper case and vice_versa
a=input("enter the character")
print(a.upper())
print(a.lower())

#ASCII value of a character
a=input("enter the character")
print("the ASCII value of a character",ord(a))

#ASCII value of a number
a=int(input("enter the number"))
print("ASCII value of a number is:",chr(a))


#To check wheather a character is vowel or consonant
k=input("enter the character")
if(k=='a' or k=='e' or k=='i' or k=='o' or k=='u'):
    print("vowel")
else:
    print("consonant")
    

#To check a character is in uppercase or lowercase
a=input("enter the character")
if(a.isupper()):
    print("upper case")
else:
   if(a.islower()):
     print("lower case")
     
     
#To check a number is even or odd
a=int(input("enter the number:"))
if(a%2==0):
 print("even")
else:
     print("odd")
     
     
     
#To check wheather a number is positive,negative or zero
a=int(input("enter the number"))
if(a>0):
 print("positive")
else:
 if(a<0):
  print("negative")
 else:
     print("zero")
     
     
#To claculate the total marks and and the division     
a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
t=a+b+c
percent=(t/300)*100
print("percentage is:",percent)
if(percent>=60):
 print("first division")
else:
 if(percent>=60):
  print("second division")
 else:
  if(percent>=60):
    print("third division")
  else:        
     print("fail")
    
    
#eligible for voting
age=int(input("enter the age"))
if(age>=18):
     print("eligible to vote")
else:
    print("not eligible to vote")
    
    
#greatest among three numbers
a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
if(a>b):
    print("a is greater")
else:
 if(b>c):
     print("b is greater")
 else:
     print("c is greater")
     
     

    