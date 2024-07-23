#SUM OF NATURAL NUMBERS
#i) FOR LOOP
n=int(input("Enter n :"))
sum=0
for i in range(1,n+1):
     sum=sum+i
print("Sum ",sum)	

#MULTIPLICATION TABLE i) FOR LOOP
n=int(input("Enter n :"))
for i in range(1,11): 
	print(n,"x",i,"=",n*i)      

#STRING LENGTH
n=input()
count= 0
for i in n:
	print(i)
	count+=1
print("String Length ",count)	

#PRIME or NOT PRIME
n=int(input("Enter a value of n  : "))
count=0
for i in range(1,n+1):
   if (n%i==0):
     count+=1
if(count==2):  
	print("It is a PRIME ")
else:
	print("NOT PRIME")

#PALINDROME or NOT
n=int(input("Enter the Number: "))
org=n
num=0
while n!=0:
     ream=n%10
     num=(num*10)+ream
     n=n//10

if(num==org):
   print(num,"is a palindrome number")
else:      
   print(num,"is not a palindrome")

#REVERSE OF A NUMBER
n=int(input("Enter the Number: "))
org=n
num=0
while n!=0:
     ream=n%10
     num=(num*10)+ream
     n=n//10
print("The Reverse of ",org,"number is:",num)






  

  
	  	
