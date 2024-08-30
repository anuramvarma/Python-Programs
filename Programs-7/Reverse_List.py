def Rev(l):
	n=len(l)
	l2=[]
	while(n>=0):
		l2.append(l[n-1])
		#print(l[n-1])
		n-=1
	return l2
l=[]
n=int(input("Enter the size of list"))
for i in range(n):
	ele=int(input())
	l.append(ele)
print(l)
print("After reversing")
print(Rev(l))	
