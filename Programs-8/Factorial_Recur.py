def rfact(n):
   if n==0:
      return 1
   else:   
      return n*rfact(n-1)
x=int(input("Enter a Number : "))
print("Factorial of ",x,"is: ",rfact(x))  
