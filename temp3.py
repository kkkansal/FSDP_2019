#To find the even number upto n
kunal=int(input("enter the number"))
kunal1=int(input("enter the number"))
for num in range(kunal,kunal1+1):
    if(num%2==0):
        print(num)
 
#To find the odd number upto n       
kunal=int(input("enter the number"))
kunal1=int(input("enter the number"))
for num in range(kunal,kunal1):
  if(num%2==1):
    print(num)        
    
#Print the number upto n using foor loop    
kunal=int(input("enter the number"))
kunal1=int(input("enter the number"))
for num in range(kunal,kunal1+1):
    print(num)
     #or
kunal=int(input("enter the number "))
for i in range(0,kunal,+1):
 print(i)     
     
     

#Print the natural number in reverse order
kunal=int(input("enetr the number"))
for i in range(kunal,0,-1):
     print(i)
    
#To print natural number and find their sum
kunal=int(input("enter the number"))
s=0
for i in range(0,kunal+1,+1):
    s=s+i
    print(i)
print("total sum of the above number",s)    

#To print the table of a particular number
kunal=int(input("enter the number"))
for i in range(1,10+1):
    print(kunal*i)
    
#To reverse a particular number
kunal = int(input("enter the number"))
kunal1=kunal%10
kunal2=kunal//10
kunalk=kunal1*10+kunal2
print(kunalk)

#To find the number is a prime number or not
n=int(input("enter the number:"))
f=0
for i in range(2,n,+1):
    if(n%i==0):
        f=1
        break
if(f==0):
 print("prime number")
else:
 print("not prime")    


n=int(input("enter the number"))
for i in range(1,n,+1):
     m=i
     f=0
     for j in range(2,m,+1):
         if(m%j==0):
             f=1
             break
     if(f==0):
         print("prime number",m)
         
     
