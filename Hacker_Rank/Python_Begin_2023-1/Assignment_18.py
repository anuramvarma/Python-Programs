# Enter your code here. Read input from STDIN. Print output to STDOUT
c=float(input())
a=input()
if(a=="British Pound"):
    c=c*0.0100
    print(c)
elif(a=="Euro"):
    c=c*0.01417
    print(c)
elif(a=="Australian Dollar"):
    c=c*0.02140
    print(c)
elif(a=="Canadian Dollar"):
    c=c*0.02027
    print(c)
else:
    print("Invalid currency name")
