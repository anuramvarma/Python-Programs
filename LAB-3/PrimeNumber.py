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
