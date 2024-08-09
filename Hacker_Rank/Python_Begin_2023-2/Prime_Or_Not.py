import math
n = int(input())
if n <=1:
    print("Not a Prime number")
else:
    count=0
    for i in range(1,int(math.sqrt(n))+1):
        if n%i==0:
            count+=1
            if i!=n//i:
                count+=1
    if count==2:
        print("Prime number")
    else:
        print("Not a Prime number")
