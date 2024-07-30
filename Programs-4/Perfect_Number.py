n=int(input("Enter value to find Perfect Number or Not :"))
sum=0
for i in range(1,n):
       if n%i==0:
          sum+=i
if (n==sum):
	print("It is an Perfect Number")	
else:
	print("Not a Perfect Number ")	





	
