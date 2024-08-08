# Enter your code here. Read input from STDIN. Print output to STDOUT
t=input()
n=int(input())
d=int(input())
c=0
if(t=='N'):
    if(d<=3):
        c=n*150
    elif(d>3 and d<=6):
        d=d-3
        c=n*150+d*3
    else:
        d=d-6
        c=n*150+(9+d*6)
elif(t=='V'):
    if(d<=3):
        c=n*120
    elif(d>3 and d<=6):
        d=d-3
        c=n*120+d*3
    else:
        d=d-6
        c=n*120+d*6+9
else:
    c=-1
print(c)  
