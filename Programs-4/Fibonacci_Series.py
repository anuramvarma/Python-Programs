T=int(input("Enter a value "))
n1,n2=0,1
while T>0:
      print(n1,end=" ")
      n3=n1+n2
      n1=n2
      n2=n3
      T-=1
